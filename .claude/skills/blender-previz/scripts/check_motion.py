"""Motion sanity check for a previz scene: characters (objects named CHR_*) and the active camera.

Run in background Blender, the whole shot is checked in seconds:
  blender -b scene.blend --python check_motion.py -- --runners Hero,Friend --allow 10-20,40-50

Flags
  characters: walking faster than --walk m/s (horizontal) unless listed in --runners;
              teleports (more than --teleport metres in one frame, anyone).
  camera:     speed over --cam-speed m/s; position jump (more than --cam-jump m in one frame);
              sharp rotation (more than --cam-turn degrees in one frame);
              lens jump (more than --lens-jump mm in one frame; zoom should take 24+ frames).
Frames inside --allow ranges (inclusive, e.g. 10-20,40-50) are skipped, for planned whips and bumps.
"""
import sys
import math
import argparse

import bpy
from mathutils import Vector


def parse_args():
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    p = argparse.ArgumentParser(prog="check_motion.py")
    p.add_argument("--runners", default="", help="comma list of characters allowed to run (CHR_ prefix optional)")
    p.add_argument("--allow", default="", help="frame ranges to skip, e.g. 10-20,40-50")
    p.add_argument("--walk", type=float, default=1.8, help="max walking speed, m/s")
    p.add_argument("--teleport", type=float, default=0.8, help="character jump per frame, m")
    p.add_argument("--cam-speed", type=float, default=4.0, help="max camera speed, m/s")
    p.add_argument("--cam-jump", type=float, default=0.5, help="camera position jump per frame, m")
    p.add_argument("--cam-turn", type=float, default=15.0, help="camera rotation per frame, degrees")
    p.add_argument("--lens-jump", type=float, default=2.0, help="lens change per frame, mm")
    p.add_argument("--start", type=int, default=None)
    p.add_argument("--end", type=int, default=None)
    return p.parse_args(argv)


def parse_ranges(text):
    out = []
    for part in filter(None, (s.strip() for s in text.split(","))):
        lo, _, hi = part.partition("-")
        out.append((int(lo), int(hi or lo)))
    return out


def characters(scene):
    """Top-level CHR_* objects (children like CHR_Name_Body are not tracked separately)."""
    return [o for o in scene.objects
            if o.name.startswith("CHR_") and not (o.parent and o.parent.name.startswith("CHR_"))]


def print_runs(title, hits):
    """hits: {frame: value}. Print consecutive frames as ranges with the worst value."""
    frames = sorted(hits)
    if not frames:
        return
    runs, start, prev = [], frames[0], frames[0]
    for f in frames[1:]:
        if f != prev + 1:
            runs.append((start, prev))
            start = f
        prev = f
    runs.append((start, prev))
    print(f"  {title}")
    for lo, hi in runs:
        worst = max(hits[f] for f in range(lo, hi + 1))
        label = f"frame {lo}" if lo == hi else f"frames {lo}-{hi}"
        print(f"    {label}: peak {worst:.2f}")


def main():
    a = parse_args()
    scene = bpy.context.scene
    fps = scene.render.fps / scene.render.fps_base
    dt = 1.0 / fps
    f0 = scene.frame_start if a.start is None else a.start
    f1 = scene.frame_end if a.end is None else a.end
    allow = parse_ranges(a.allow)
    runners = {r.strip().removeprefix("CHR_") for r in a.runners.split(",") if r.strip()}
    chars = characters(scene)
    cam = scene.camera
    original_frame = scene.frame_current

    issues = {}  # (subject, kind) -> {frame: value}

    def flag(subject, kind, frame, value):
        issues.setdefault((subject, kind), {})[frame] = value

    prev_pos, prev_fwd, prev_lens = {}, None, None
    for f in range(f0, f1 + 1):
        scene.frame_set(f)
        bpy.context.view_layer.update()
        skip = any(lo <= f <= hi for lo, hi in allow)

        for o in chars:
            pos = o.matrix_world.translation.copy()
            if o.name in prev_pos and not skip:
                d = pos - prev_pos[o.name]
                horiz = math.hypot(d.x, d.y) / dt
                if d.length > a.teleport:
                    flag(o.name, "teleport (m in one frame)", f, d.length)
                elif horiz > a.walk and o.name.removeprefix("CHR_") not in runners:
                    flag(o.name, f"faster than walking, limit {a.walk} m/s", f, horiz)
            prev_pos[o.name] = pos

        if cam is not None:
            pos = cam.matrix_world.translation.copy()
            fwd = cam.matrix_world.to_3x3() @ Vector((0, 0, -1))
            fwd.normalize()
            lens = cam.data.lens
            if prev_fwd is not None and not skip:
                d = (pos - prev_pos["__cam"]).length
                if d > a.cam_jump:
                    flag("camera", "position jump (m in one frame)", f, d)
                elif d / dt > a.cam_speed:
                    flag("camera", f"speed over {a.cam_speed} m/s", f, d / dt)
                turn = math.degrees(fwd.angle(prev_fwd))
                if turn > a.cam_turn:
                    flag("camera", "sharp rotation (deg in one frame)", f, turn)
                if abs(lens - prev_lens) > a.lens_jump:
                    flag("camera", "lens jump (mm in one frame)", f, abs(lens - prev_lens))
            prev_pos["__cam"], prev_fwd, prev_lens = pos, fwd, lens

    scene.frame_set(original_frame)

    print(f"check_motion: frames {f0}-{f1} at {fps:g} fps, {len(chars)} characters, "
          f"camera {'yes' if cam else 'NONE (no active camera)'}")
    if not issues:
        print("  no problems found")
        return
    for (subject, kind), hits in sorted(issues.items()):
        print_runs(f"{subject}: {kind}", hits)
    print("Fix the motion or add the frames to --allow if the move is planned.")


main()
