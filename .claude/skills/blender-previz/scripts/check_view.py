"""Framing check for a previz scene: is the hero inside the camera frame, and does anything block the view?

Run in background Blender:
  blender -b scene.blend --python check_view.py -- --hero CHR_Name --step 2

For each checked frame the script tests the hero's world-space bounding-box centre:
  OUT      the point is outside the camera frustum (or behind the camera)
  BLOCKED  a ray from the camera to the point first hits some other object (named in the report)
  ok       visible
Consecutive frames with the same state are printed as one range. Compare OUT ranges with the
planned cut-aways in the script: every one of them must be intentional.
"""
import sys
import argparse

import bpy
from bpy_extras.object_utils import world_to_camera_view
from mathutils import Vector


def parse_args():
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    p = argparse.ArgumentParser(prog="check_view.py")
    p.add_argument("--hero", required=True, help="object name, e.g. CHR_Name")
    p.add_argument("--step", type=int, default=2, help="check every Nth frame")
    p.add_argument("--start", type=int, default=None)
    p.add_argument("--end", type=int, default=None)
    p.add_argument("--margin", type=float, default=0.0, help="shrink the frame by this fraction on each side")
    return p.parse_args(argv)


def hero_objects(hero):
    return {hero.name} | {c.name for c in hero.children_recursive}


def hero_centre(hero):
    """Centre of the world-space bounding box of all meshes in the hero hierarchy."""
    pts = []
    for o in [hero, *hero.children_recursive]:
        if o.type == "MESH":
            pts += [o.matrix_world @ Vector(c) for c in o.bound_box]
    if not pts:
        return hero.matrix_world.translation.copy()
    lo = Vector((min(p[i] for p in pts) for i in range(3)))
    hi = Vector((max(p[i] for p in pts) for i in range(3)))
    return (lo + hi) / 2


def first_blocker(scene, depsgraph, origin, target, own):
    """Walk the ray from origin to target; return the name of the first object not in `own`, else None."""
    direction = target - origin
    remaining = direction.length
    direction.normalize()
    start = origin.copy()
    for _ in range(16):
        hit, loc, _n, _i, obj, _m = scene.ray_cast(depsgraph, start, direction, distance=remaining)
        if not hit:
            return None
        if obj.name not in own:
            return obj.name
        step = (loc - start).length + 1e-3  # pass through the hero's own parts
        start = loc + direction * 1e-3
        remaining -= step
        if remaining <= 0:
            return None
    return None


def print_runs(rows):
    """rows: list of (frame, state). Group consecutive checked frames with the same state."""
    if not rows:
        return
    runs, (start, state), prev = [], rows[0], rows[0][0]
    for f, s in rows[1:]:
        if s != state:
            runs.append((start, prev, state))
            start, state = f, s
        prev = f
    runs.append((start, prev, state))
    for lo, hi, s in runs:
        label = f"frame {lo}" if lo == hi else f"frames {lo}-{hi}"
        print(f"  {label}: {s}")


def main():
    a = parse_args()
    scene = bpy.context.scene
    hero = bpy.data.objects.get(a.hero)
    cam = scene.camera
    if hero is None:
        sys.exit(f"check_view: no object named {a.hero}")
    if cam is None:
        sys.exit("check_view: scene has no active camera")
    own = hero_objects(hero)
    f0 = scene.frame_start if a.start is None else a.start
    f1 = scene.frame_end if a.end is None else a.end
    original_frame = scene.frame_current
    lo, hi = a.margin, 1.0 - a.margin

    rows = []
    for f in range(f0, f1 + 1, max(1, a.step)):
        scene.frame_set(f)
        bpy.context.view_layer.update()
        depsgraph = bpy.context.evaluated_depsgraph_get()
        centre = hero_centre(hero)
        uv = world_to_camera_view(scene, cam, centre)
        if uv.z <= 0 or not (lo <= uv.x <= hi and lo <= uv.y <= hi):
            rows.append((f, "OUT of frame"))
            continue
        blocker = first_blocker(scene, depsgraph, cam.matrix_world.translation.copy(), centre, own)
        rows.append((f, f"BLOCKED by {blocker}" if blocker else "ok"))

    scene.frame_set(original_frame)
    print(f"check_view: hero {a.hero}, frames {f0}-{f1}, every {max(1, a.step)}")
    print_runs(rows)
    bad = sum(1 for _, s in rows if s != "ok")
    print(f"{bad} of {len(rows)} checked frames are not clean")


main()
