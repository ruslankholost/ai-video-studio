#!/usr/bin/env python3
"""Check a Seedance 2.5 JSON video prompt before it is pasted into Higgsfield.

Usage:
    python scripts/check_prompt.py prompt.json    print each problem, exit 1; or print OK
    python scripts/check_prompt.py --selftest     run a good and a bad sample

The rules come from templates/video-prompt-seedance.md. Standard library only.
"""
import json
import re
import sys

LIMIT_CHARS = 5000
MAX_SECONDS = 30      # one Seedance 2.5 pass
ADVISED_SECONDS = 15  # advised batch size, longer only gets a note

TOP_ORDER = ["概述", "参考素材分工", "角色固定", "物体固定与朝向", "整体风格",
             "场景", "人声", "分镜", "声音", "负面提示"]
TOP_REQUIRED = ["概述", "分镜", "负面提示"]
SHOT_ORDER = ["时间", "衔接", "机位", "画面", "表演", "台词"]
SHOT_REQUIRED = ["时间", "机位", "画面", "表演"]

TIME_RE = re.compile(r"^(\d+)s-(\d+)s$")
REF_RE = re.compile(r"@(?:Image|Video|Audio)\d+")
FRACTION_RE = re.compile(r"\d+[.,]\d+\s*(?:s(?![A-Za-z])|秒)")
ESCAPE_RE = re.compile(r"\\u[0-9a-fA-F]{4}")
DURATION_RE = re.compile(r"(\d+)\s*秒")


def check_order(keys, order, where, problems):
    unknown = [k for k in keys if k not in order]
    for k in unknown:
        problems.append(f"{where}: unknown field {k!r}, allowed: {' '.join(order)}")
    known = [order.index(k) for k in keys if k in order]
    if known != sorted(known):
        problems.append(f"{where}: fields are out of order, expected {' '.join(k for k in order if k in keys)}")


def check_timeline(items, where, problems):
    """Whole seconds, contiguous from 0. Returns the end of the last block."""
    prev_end = 0
    for i, item in enumerate(items):
        t = item.get("时间", "") if isinstance(item, dict) else ""
        m = TIME_RE.match(t) if isinstance(t, str) else None
        if not m:
            problems.append(f"{where}[{i}].时间 = {t!r}: use whole seconds like \"0s-3s\"")
            continue
        start, end = int(m[1]), int(m[2])
        if end <= start:
            problems.append(f"{where}[{i}]: end {end}s is not after start {start}s")
        if start != prev_end:
            problems.append(f"{where}[{i}]: starts at {start}s but the previous block ended at {prev_end}s")
        prev_end = end
    return prev_end


def check(text):
    """Return a list of problems for the prompt text (empty list = OK)."""
    problems = []
    text = text.strip()
    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        return [f"not valid JSON: {e.msg} at line {e.lineno}, column {e.colno} "
                "(a straight \" inside a line of dialogue is the usual cause, use « »)"]
    if not isinstance(data, dict):
        return ["top level must be a JSON object { ... }"]

    # length
    compact = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    if len(text) > LIMIT_CHARS:
        hint = f"compact form is {len(compact)}, paste that" if len(compact) <= LIMIT_CHARS \
            else "still too long compact, cut text"
        problems.append(f"{len(text)} characters, limit {LIMIT_CHARS} ({hint})")
    if ESCAPE_RE.search(text):
        problems.append("Chinese is written as \\uXXXX escapes, write the characters themselves")
    if FRACTION_RE.search(text):
        problems.append(f"fractional seconds found ({FRACTION_RE.search(text)[0]!r}), Seedance reads whole seconds only")

    # top-level fields
    for k in TOP_REQUIRED:
        if k not in data:
            problems.append(f"missing required field {k}")
    check_order(list(data), TOP_ORDER, "top level", problems)

    # references: every @ used must be declared in 参考素材分工
    block = data.get("参考素材分工")
    declared = set()
    if isinstance(block, dict):
        for key in block:
            declared.update(REF_RE.findall(key))
    used = set(REF_RE.findall(text))
    for ref in sorted(used - declared):
        problems.append(f"{ref} is used but not declared in 参考素材分工")

    # shots
    shots = data.get("分镜")
    total = 0
    if shots is not None:
        if not isinstance(shots, list) or not shots:
            problems.append("分镜 must be a non-empty list of shots")
        else:
            for i, shot in enumerate(shots):
                if not isinstance(shot, dict):
                    problems.append(f"分镜[{i}] must be an object")
                    continue
                check_order(list(shot), SHOT_ORDER, f"分镜[{i}]", problems)
                for k in SHOT_REQUIRED:
                    v = shot.get(k)
                    if not isinstance(v, str) or not v.strip():
                        problems.append(f"分镜[{i}]: {k} is missing or empty"
                                        + (" (a shot with nobody in it says 画面中没有人物。)" if k == "表演" else ""))
            total = check_timeline([s for s in shots if isinstance(s, dict)], "分镜", problems)

    # total length
    if total > MAX_SECONDS:
        problems.append(f"total {total}s is over the {MAX_SECONDS}s limit of one pass, split into batches")
    m = DURATION_RE.search(data["概述"]) if isinstance(data.get("概述"), str) else None
    if m and total and int(m[1]) != total:
        problems.append(f"概述 says {m[1]}秒 but the shots end at {total}s")

    # sound segments follow the same timeline rule
    sound = data.get("声音")
    if isinstance(sound, dict) and isinstance(sound.get("分段"), list):
        end = check_timeline([s for s in sound["分段"] if isinstance(s, dict)], "声音.分段", problems)
        if total and end != total:
            problems.append(f"声音.分段 ends at {end}s but the shots end at {total}s")
    return problems


SELFTEST_GOOD = """{
  "概述": "10秒，竖屏9:16，剧情片，傍晚室内暖光",
  "参考素材分工": {"@Image1": "女主角，只提供外貌和服装，不提供姿势和表情。", "@Video1": "只提供镜头运动、人物位置、路线和时间。"},
  "分镜": [
    {"时间": "0s-5s", "机位": "正面平视中景，离人物三米，高度一米四，35毫米，焦点在人物。", "画面": "@Image1 的女主角站在窗边。", "表演": "女主角：双臂交叉，眉头微蹙，嘴唇抿紧，目光看向窗外。"},
    {"时间": "5s-10s", "衔接": "硬切到", "机位": "面部特写，高度一米六，85毫米，焦点在眼睛。", "画面": "她转过头。", "表演": "画面中没有人物。"}
  ],
  "声音": {"总则": "真实音效，没有背景音乐。", "分段": [{"时间": "0s-10s", "内容": "室内安静的环境声。"}]},
  "负面提示": "避免面部漂移，避免背景音乐，避免字幕"
}"""

SELFTEST_BAD = """{
  "概述": "9秒，竖屏",
  "分镜": [
    {"时间": "0s-3s", "画面": "@Image1 和 @Image9 在房间里。", "表演": "站着。"},
    {"时间": "4.5s-9s", "机位": "特写。", "画面": "她说话。", "表演": ""}
  ],
  "参考素材分工": {"@Image1": "角色。"}
}"""


def selftest():
    good = check(SELFTEST_GOOD)
    assert good == [], good
    bad = " | ".join(check(SELFTEST_BAD))
    for needle in ("missing required field 负面提示", "out of order", "分镜[0]: 机位 is missing",
                   "分镜[1]: 表演 is missing", "fractional seconds", "@Image9 is used but not declared",
                   "分镜[1].时间", "概述 says 9秒"):
        assert needle in bad, f"expected {needle!r} in: {bad}"
    gap = " | ".join(check(SELFTEST_GOOD.replace('"5s-10s"', '"6s-10s"')))
    assert "starts at 6s but the previous block ended at 5s" in gap, gap
    assert any("not valid JSON" in p for p in check("{bad"))
    print("selftest OK")


def main(argv):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    if len(argv) == 2 and argv[1] == "--selftest":
        return selftest()
    if len(argv) != 2:
        print(__doc__)
        return 2
    with open(argv[1], encoding="utf-8-sig") as f:
        text = f.read()
    problems = check(text)
    for p in problems:
        print(f"PROBLEM: {p}")
    if problems:
        return 1
    print(f"OK ({len(text.strip())} / {LIMIT_CHARS} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
