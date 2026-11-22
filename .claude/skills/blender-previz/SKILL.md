---
name: blender-previz
description: Build a previz (greybox reference video) in Blender through Claude Code, to be used later as @Video1 in a Seedance omni-reference generation. Use when the user says "build the previz", "greybox in Blender", "reference video for Seedance", "camera in Blender", "block the scene", "rebuild the set from photos", "one-take previz", "time the previz to my voice recording", "check the camera move", or complains that a Blender render is slow or the computer runs hot. Covers the default decisions (480x854 vertical, 24 fps, EEVEE without shadows), can-shaped characters, a handheld camera rig, blocking before animation, speed and framing checks, render, and the report.
---

# Blender previz

A previz is a cheap grey render of the shot: where people stand and walk, how the camera moves, how long each beat lasts. Seedance copies the motion of the reference video almost exactly, camera best of all. So the previz must move like real life: a slow, smooth, game-like previz becomes a slow, game-like generated video.

Most re-renders on past projects came from the same ten mistakes (table below). This skill front-loads the checks that remove them.

## Default decisions

Use these unless the user asks for something else.

- Format: vertical 9:16, 480x854, 24 fps, one continuous take. The generator cuts the take into pieces (Seedance 2.5 takes up to 30 s per piece), and the join is hidden in a blur.
- Render: EEVEE, no shadows, 8 samples (`render_preset.py previz`). This is both the draft and the final reference. More resolution, shadows or samples only if the user asks.
- Checks and frame grids: Workbench (`render_preset.py check`), not EEVEE.
- Characters are "cans": a cylinder body, a sphere head, a dark cone nose that points where the face looks. Colour identifies the character. Add arms only for a character whose gesture matters to the story (a punch, a raised fist, three fingers).
- Timing follows the voice recording. Put the audio in the scene from the first pass. No recording yet: say so, and mark all timing as temporary.
- Real-world speeds for people and objects (see the speed table).
- Camera is a human operator: noise, a walking bob, bumps, cut-aways to events, focus drift. Not a drone and not a robot.
- No intersections: bodies do not pass through each other, furniture, doors, walls or the operator. The character reacts to every touch.
- Heavy work (build, animate, render) runs in background Blender, one process at a time, on a copy of the `.blend`.
- Never overwrite a version: `ref_v1.mp4`, `ref_v2.mp4`, `ref_v3.mp4`.
- The final report lists every deviation from the brief, a ready-made fix for the brief, and "site facts" measured in the scene.

## Setup

Blender: 4.2 or newer, 5.x preferred. Download from blender.org, or install with the system package manager.

| System | Blender command | Install |
|---|---|---|
| Windows | `"C:\Program Files\Blender Foundation\Blender 5.x\blender.exe"` (use the real folder name) | `winget install BlenderFoundation.Blender` |
| macOS | `/Applications/Blender.app/Contents/MacOS/Blender` | `brew install --cask blender` |

Check it runs headless: `blender -b --version`. Everything below uses background mode:

```
blender -b scene.blend --python script.py
blender -b scene.blend --python script.py -- --my-args      # args after "--" go to the script
blender -b --factory-startup --python build_all.py          # build a scene from nothing
```

Order of flags matters: `--python` first, then `-o`/`-f`/`-a`, then `--` and the script's own args.

Optional live link: an MCP server for Blender (the add-on listens on port 9876, started from the add-on panel in the N sidebar) lets Claude look at the open scene and make small edits. Use it for viewing only. Builds, animation and renders go through background Blender: the same script that took 10+ minutes over the bridge and hung the add-on ran in seconds in background mode.

If the user has the scene open in a Blender window, do not edit that file. The window holds its own copy and can save over your work. Work on a copy, and ask the user to use File, Revert (or File, Open) to see the new version.

Scripts live in `scripts/` next to this file:

- `render_preset.py`: presets `check`, `previz`, `hq`.
- `check_motion.py`: speeds, teleports, camera jumps.
- `check_view.py`: hero in frame, line of sight.

## Workflow

1. Voice first. Get the recording, even a rough one. Put a marker at the start of every line. No recording: warn that timing is temporary.
2. Read the whole brief and every column of the storyboard before asking anything. Ask all questions in one batch, each with a default answer.
3. Set. Build from photos or from the generated reference images (details below). Ask for three reference sizes: ceiling height, door size, room length. Ask where mirrors and glass are: a reflected door looks like a second door. Fix one coordinate system for the whole take (origin, axes, "we look from here"), and state how locations join. Leave room for the operator: the body is about 0.15 m behind the lens, plus space to step back. A corridor for the camera may be wider than the real one. For doors: hinge side, swing direction, open or closed at the start, and check the leaf does not block a path.
4. Blocking before any animation. Produce a table (time, where, who, facing what, what must be visible), a top view with the paths of people and camera, and 5-6 key frames in `check` mode. Show them and wait for the user's "ok".
5. Check the script against physics, before animating. For each move, speed = distance / time. List every conflict as "brief line, what the scene shows, what I propose". Words with two readings ("spins", "shot", "sign") get a question or both versions shown. Never silently speed something up or pick a reading.
6. Animate in dependency order: hero path, supporting characters, camera (its keys are computed from the people), gaze and props, everyone else. All by script, in background Blender.
7. Checks: `check_motion.py`, `check_view.py`, a collision script, and a frame grid (every 24th frame plus key frames, `check` preset). Look at the frames yourself first, then show the user and wait for "ok".
8. Render with `previz`. Say how long it will take before starting.
9. Report: what was done; every deviation from the brief and why; a ready-made fix for the brief (which lines to replace); site facts from the scene (sizes, doors, coordinates).

The user's "ok" is needed after step 4 (blocking) and step 7 (checks), and again on the rendered video.

### Reference speeds

| Move | Speed |
|---|---|
| Walk | 1.2-1.5 m/s |
| Fast walk | up to 1.8 m/s |
| Run | 3-5 m/s |
| Operator walking backwards | up to about 1.2 m/s |
| Handheld camera, hard limit | about 4 m/s |

## The ten mistakes

| Mistake | Rule |
|---|---|
| Timing from the text, voice recorded later | Voice first. Without it the running time changed twice (58 s, 67 s, 60 s). |
| Sizes by eye, camera cramped | Take reference sizes from a person who knows the place. Size a hall from the action (speed x time). |
| "Left/right" with no reference point | One coordinate system. Gaze is "facing <object>", never "looking left". |
| Someone blocks the hero | For every beat, write what must be visible. Run `check_view.py`. |
| Game-like movement | Give speeds as numbers. Run `check_motion.py`. Test intersections by script. |
| Hidden jumps in a "single take" | Lens change by a zoom of at least 24 frames. No teleports, no appearing within one frame. |
| Words with two meanings | Describe the action through the body. Keep a glossary in the brief. |
| No agreement on what the previz shows | Cans by default, arms only where a gesture matters, state changes shown by colour. |
| Robot camera | Leave the hero for an event (a person, a prop, a sound), never for a point in space. No "empty wall" frames. |
| Expensive rounds | Use the plan and the frame grid instead of a render. Put the fix in the report. |

## Characters (cans)

- `CHR_<Name>` is an empty on the floor that carries heading and tilt. Children:
  - `_Body`: cylinder, radius 0.16-0.18 m, height 1 m, stretched on Z;
  - `_Head`: sphere, radius 0.12 m;
  - `_Nose`: dark cone. Where it points, the face looks.
- Poses:
  - sitting: shorter body standing on the seat;
  - crouching: head at about 0.85 m;
  - lying or being dragged: tilt about 75 degrees, head toward whoever drags;
  - handstand: 180 degree flip.
- Arms are boxes, only for story-critical gestures.
- Colour equals character. Pick colours that contrast with the set: a light can on a white wall disappears.
- A costume change is a colour change plus an action (throws it on, wraps it, morph), never a pop within one frame.
- A prop that faces the camera (a screen, a glass) is rotated toward the camera, not along the hero's heading.
- Dragging by clothing: model a rope. The dragged character's feet stay put while the distance to the puller is under about 1.3 m, then follow. Otherwise they cut furniture corners or slide under the puller.
- Rotation mode: composite objects made of cylinders may use quaternion rotation, and setting an Euler angle then silently does nothing. Catch it on the top view.

## Handheld camera rig

- Rig: `CAM_RIG` (empty: path and fly-arounds), `CAM` (tilt, pan, lens), `FOCUS` (empty: the point of focus for depth of field).
- Shake: Noise modifiers on the F-curves, so they stay visible and editable in the Graph Editor. Operator steps: a sine on Z.
- Bump: keyed, a 10-20 cm jolt and 8-15 degrees over 3-4 frames, then about 8 frames to settle.
- Lens change: a smooth zoom of 24 frames or more, while moving. Between locations the camera goes through the door, no teleport.
- A camera looking almost straight down rolls unpredictably. Keep pitch within 75-80 degrees.
- Every cut-away from the hero goes to an object (person, prop, event). During a drift with a focus pull, the hero's face stays at the edge of the frame.
- Joins for the generator:
  - the join frame is fully covered by a body right at the lens, plus blur;
  - on a whip-pan with a running body, no pitch, or the body leaves the axis and the frame is not fully covered;
  - last frame of piece 1 equals first frame of piece 2.

## Set from photos or images

1. Put all photos in one grid and describe the layout in words: what is at each wall.
2. One line at the top of the build script holds axes and dimensions (W x L x H). Everything else is computed from it.
3. One build script, one function per object. Fix by editing the script and rebuilding from scratch, no hand tweaks.
4. Put cameras where the photos were taken. A phone ultra-wide is about 13 mm in a vertical frame, 2-2.3 m high. If the floor line at the far wall sits near frame centre, the camera looks nearly level (about 15-17 degrees down).
5. Render the same angles, make a "photo / render" grid, fix, repeat. Three or four rounds are usually enough.
6. A top view (orthographic, no ceilings) is the best check of how rooms connect and what faces where. A flipped object hides in a perspective view.
7. Furniture as small functions, not boxes: a chair with legs, an office chair with a star base, a table, a tripod, a light stand, a bike. One line each: coordinates and rotation.
8. A cyclorama is a wall-curve-floor profile swept along a line in plan, not a half cylinder.
9. Doors the camera or a character passes through are built open (a script parameter).
10. From a single generated image: the user gives the size ("bigger, 5 m ceiling"), you read the layout from the picture.
11. Comparing with a photo: Workbench gives a dark ceiling, so use EEVEE with a white world and window light for that comparison only.
12. Match a start frame to a viewport screenshot by marking about 7 points with known coordinates (chair back corners, table corner) and fitting the camera until they land on their marks. A 50 mm viewport equals a 25 mm camera.

## Checks

Run all in background Blender. A whole take takes seconds.

```
blender -b scene.blend --python .claude/skills/blender-previz/scripts/check_motion.py -- --runners Hero,Friend --allow 369-378,714-726
blender -b scene.blend --python .claude/skills/blender-previz/scripts/check_view.py -- --hero CHR_Hero --step 2
```

- `check_motion.py`: character speeds (walk, run, teleport) and camera position jumps, sharp turns, lens jumps, speed.
- `check_view.py`: frames where the hero is out of frame (compare with the planned cut-aways) and frames where something blocks the line to the hero, with the blocker's name.
- Intersections, per scene (write a short script):
  - a person is a capsule: axis from the bottom of the body to the head centre, body radius;
  - furniture and walls: `mathutils.bvhtree.BVHTree.FromPolygons` on the object's mesh. Bounding boxes lie: it is empty under a table;
  - the operator is a cylinder behind the lens;
  - touches of 3-7 cm are fine in grabs.

## Render and load

Rough timings from a laptop with 16 GB RAM, a 13k polygon scene with 22 lights, depth of field and motion blur, 1441 frames (60 s). Measure on your own machine before promising a time.

| Preset | Settings | s/frame | 60 s clip |
|---|---|---|---|
| `check` | Workbench, short side 480 | 0.03 | about 1 min |
| `previz` (default) | EEVEE 480x854, no shadows, 8 samples | 0.17 | about 4 min |
| `previz --samples 16` | same, 16 samples, if blur looks grainy | 0.33 | about 8 min |
| `hq` (only on request) | EEVEE 1080x1920, 16 samples, shadows on 6 lights | 0.74 | about 18 min |

```
blender -b scene.blend --python .claude/skills/blender-previz/scripts/render_preset.py -o //render/ref_v1_#### -a -- previz
blender -b scene.blend --python .claude/skills/blender-previz/scripts/render_preset.py -o //sheet/f_#### -f 1 -f 48 -- check
```

Then encode the image sequence to `ref_v1.mp4` with ffmpeg at 24 fps (or set the output format to FFmpeg in the scene).

- Time goes to samples, shadows per light and resolution. Depth of field (about 6 percent) and motion blur (about 3 percent) are nearly free. Geometry barely matters: removing 48 city boxes changed the frame time from 1.44 to 1.42 s.
- One render at a time. On macOS add `nice -n 10`; Windows has no `nice`, so do not run it beside other heavy jobs.
- On 16 GB, extra processes (other Claude Code sessions, dev servers, tests) push the system into swap and single frames stall for tens of seconds.
- Ask the user not to leave the same scene in Rendered or Material Preview mode in their own window.

## Blender 5.x gotchas

- Actions have no `action.fcurves`. F-curves live in slots: use `bpy_extras.anim_utils.action_get_channelbag_for_slot`.
- With a non-English interface, node names are translated. Find nodes by type (`BSDF_PRINCIPLED`), never by name.
- Set colour in the material node (EEVEE) and in `diffuse_color` (Workbench). Set both.
- The EEVEE engine id is `BLENDER_EEVEE` in 5.x (`BLENDER_EEVEE_NEXT` in 4.2-4.5). `render_preset.py` tries both.
- Quaternion rotation mode ignores Euler angles. See the characters section.
- Leg IK without a pole target bends the knee the wrong way. Replace "leg over leg" with crossed ankles.
- At a join between pieces, reset the foot steps, or the legs "walk" to the new point.

## Using the previz in Seedance

Upload the render as the video reference (`@Video1`) and say in the prompt what it carries: camera move, positions, paths, timing, and what each can colour means ("pink can is the hero, blue is the driver"). Everything else (faces, costumes, light, place) comes from the image references. See `templates/previz-in-video-prompt.md` and `docs/stages/05-previz-camera.md`. Draft at 480p first; check `models_explore` for current options and `estimate_video_cost` for the price in credits before any paid run, and get the user's "yes" on the exact list.
