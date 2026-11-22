"""Render presets for a previz scene. Changes settings in memory only; never saves the .blend.

Run (order matters: script first, then output/frame flags, then script args after "--"):
  blender -b scene.blend --python render_preset.py -o //render/ref_#### -a -- previz
  blender -b scene.blend --python render_preset.py -o //sheet/f_#### -f 1 -f 48 -- check
  blender -b scene.blend --python render_preset.py -o //render/ref_#### -a -- previz --samples 16

Presets:
  check   Workbench, short side 480 px. Blocking, frame grids, checks. Fastest.
  previz  EEVEE, short side 480 px (vertical 480x854), no shadows, 8 samples. Default for
          drafts and for the final reference.
  hq      EEVEE, short side 1080 px, 16 samples, shadows on the N strongest lights.
          Only when the user asks for it.
"""
import sys
import argparse

import bpy

PRESETS = ("check", "previz", "hq")
DEFAULTS = {"check": (480, 0), "previz": (480, 8), "hq": (1080, 16)}  # (short side px, samples)


def parse_args():
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    p = argparse.ArgumentParser(prog="render_preset.py")
    p.add_argument("preset", nargs="?", default="previz", choices=PRESETS)
    p.add_argument("--samples", type=int, default=0, help="EEVEE samples (0 = preset default)")
    p.add_argument("--short", type=int, default=0, help="short side in px (0 = preset default)")
    p.add_argument("--key", type=int, default=6, help="hq only: lights that keep shadows")
    return p.parse_args(argv)


def set_short_side(render, px):
    """Keep the aspect ratio, make the short side px, round both sides to even numbers."""
    x, y = render.resolution_x, render.resolution_y
    k = px / min(x, y)
    render.resolution_x = max(2, round(x * k / 2) * 2)
    render.resolution_y = max(2, round(y * k / 2) * 2)
    render.resolution_percentage = 100


def set_eevee(render):
    """EEVEE id is BLENDER_EEVEE in 5.x, BLENDER_EEVEE_NEXT in 4.2-4.5. Try both."""
    for name in ("BLENDER_EEVEE", "BLENDER_EEVEE_NEXT"):
        try:
            render.engine = name
            return name
        except TypeError:
            continue
    raise RuntimeError("No EEVEE engine id accepted by this Blender build")


def set_samples(scene, n):
    ev = scene.eevee
    if hasattr(ev, "taa_render_samples"):
        ev.taa_render_samples = n


def set_shadows(scene, keep):
    """keep = 0: shadows off on every light. keep = N: only suns and the N strongest lights keep them."""
    lights = [o for o in scene.objects if o.type == "LIGHT"]
    non_sun = sorted((o for o in lights if o.data.type != "SUN"), key=lambda o: o.data.energy, reverse=True)
    kept = set()
    if keep > 0:
        kept = {o.name for o in lights if o.data.type == "SUN"} | {o.name for o in non_sun[:keep]}
    for o in lights:
        o.data.use_shadow = o.name in kept
    return sorted(kept)


def main():
    a = parse_args()
    scene = bpy.context.scene
    render = scene.render
    short, samples = DEFAULTS[a.preset]
    short = a.short or short
    samples = a.samples or samples

    if a.preset == "check":
        render.engine = "BLENDER_WORKBENCH"
        shading = scene.display.shading
        shading.light = "STUDIO"
        shading.color_type = "MATERIAL"
        shading.show_shadows = False
    else:
        set_eevee(render)
        set_samples(scene, samples)
        kept = set_shadows(scene, a.key if a.preset == "hq" else 0)
        if a.preset == "hq":
            print("shadows kept on:", ", ".join(kept) or "none", flush=True)
    set_short_side(render, short)

    extra = f", {samples} samples" if a.preset != "check" else ""
    print(f"preset {a.preset}: {render.engine} {render.resolution_x}x{render.resolution_y}{extra}", flush=True)


main()
