# 05 Previz and camera

The hardest thing to control in AI video is the camera: a prompt alone hardly holds it for long. When that matters, the video is first built as a simple 3D blockout with a camera (previz) in Blender, corrected with words for free, and the video model then receives a finished movement. The previz decides where the camera goes, where people and objects stand, which paths they walk and how fast. The images decide how everything looks. The prompt decides the acting and the details. This stage produces the previz video that stage 06 feeds to Seedance as `@Video1`.

**When this stage is needed.** Most AI videos are made without a previz: a strong start frame, the character cards and the template prompt with timecodes (stage 06) hold short shots with simple camera moves (static, slow push-in, pan, short tracking). Build a previz only in two cases:
1. A long continuous take with no cuts, where one camera move carries the whole clip (for example a 25-30 s one-take through a building or around a car).
2. A camera move the prompt failed to hold on the same shot twice in a row. Then build the previz for that shot only.

The Blender link works with Seedance only. If neither case applies, skip this stage and write in `progress.md`: "05 skipped: no long take, no failed camera".

## Input and output

Input:
- `script.md` and `storyboard.md`: the idea and a director's storyboard in whole seconds (what is in shot, camera path, speed, text). Call the detailed version `shot-spec.md`.
- `refs/` and `frames/`: the images for everything the model must draw exactly (hall, facade, car, interior, face, driver; stage 04). For a previz of a real room you need photos and three anchor dimensions (ceiling, door, room length).
- A voice recording (even a rough one) or a table of lines by second: the timing is built from it.
- A video reference (someone else's clip with a scene like ours), if there is one.
- For filming the camera with a phone: an iPhone or iPad with the free Omniscient app and Blender 4.2 or newer.

Output (`previz/`):
- `previz/*.blend`: the scene, each assembly a new file (`scene_v1.blend`, `scene_v2.blend`).
- `previz/ref_*.mp4`: the previz video, each edit a new version (`ref_car_v1.mp4`, `_v2`, `_v3`), old ones stay.
- A blocking table, a top-down plan, a frame grid, a report: what was done, where it departs from the spec and why, and a ready correction for the spec.
- For a phone take: a screen recording with voice and the camera keys in the `.blend`.
- The role of the previz written into `prompts.md` (the prompt itself and the generation belong to stage 06).

## Principles

### A. Why previz, and who does what

05.1 **Blender is responsible for movement, images for how everything looks, the prompt for acting and details.** The previz gives Seedance the camera, the paths and the speed, which it does not invent well by itself.

05.2 **The camera in the previz is corrected for free, so mistakes are caught in the previz, not in generation.** You see the clip before generating and fix it in words until you like it. Seedance gets finished motion, and money goes into one or two generations instead of twenty. Seedance carries over everything it sees (closed car windows stay closed). One practitioner estimated the saving from prior 3D blocking at roughly 35 percent of the generation budget. That is an estimate from a conversation, not a measurement.

05.3 **You do not need to know Blender: the agent builds the scene and you describe it in words, "as to a camera operator".** Use the strongest available model with high reasoning effort for 3D work, because in a 3D scene one wrong digit means a car backwards or a camera through a wall.

05.4 **Write the director's storyboard in whole seconds first, then everything else.** Seedance does not understand fractions of a second. Corrections go into the chat in words ("in the second beat the camera is lower, the explosion one second later").

05.5 **Build the timing from a voice recording: the voice lies in the previz from the first pass.** Without a voice, the running time shifted twice in one project (58, then 67, then 60 seconds). If there is no recording, say the timing is temporary and place a marker at the start of each line. In a phone take the agent transcribes the voice and matches it to the camera keys, making a table "second, what the camera does, who says what" before animating.

05.6 **Block before animating: a table "time, where, who, facing what, what is visible", a top-down plan with paths, 5-6 key frames (up to 8-9 for a long take). Show it and wait for "ok".** On the plan the car's path is red, the camera's yellow, runners grey, with seconds at camera points. (user's ok)

05.7 **Check the spec against physics before animating.** The speed of each move is distance divided by time. List conflicts as "spec line, what is in the scene, what I propose". Do not speed things up silently. Ask about words with two readings ("screws in", "frame", "sign") or show both.

### B. Movement and speed carry over literally

05.8 **The video model repeats the movement of the blockout exactly, so speeds and acceleration of people and objects must look real.** A slow smooth car in the previz becomes the same "game-like" car in the video. The camera transfers best. Reference speeds: walk 1.2-1.5 m/s, fast walk up to 1.8, run 3-5. An operator walking backwards goes no faster than about 1.2 m/s, a handheld camera up to about 4 m/s.

05.9 **People in the previz are simple blobs without hands or extras. Hands only where a gesture matters to the story.** Seedance copies motion fully, and a 3D person with hands moves like a video-game character. Blob colour equals the character, and each colour gets a role in the prompt. The blob's head (a nose cone) gives only the gaze direction: expression and lips are not taken from it. Suggested build: `CHR_<Name>`, body a cylinder r 0.16-0.18 m, head a sphere r 0.12, nose a dark cone, contrasting colours for the set. Take only movement and head direction from the blob: faces and hands are drawn by Seedance. (Resolved as the studio default; the user may change it.)

05.10 **No camera shake in the previz unless shake is wanted, and if it is wanted it is set in the previz.** Seedance repeats any shake from the previz. A smooth drone-like camera suits a cinematic piece. In a documentary piece, hand shake is kept on purpose: it makes the clip look documentary. Decide by genre before the previz (default; the user may change it).

05.11 **The camera is driven like a live operator: shake by noise modifiers, steps as a sine on Z, jerks, jumps to events, focus drifts.** A jerk is 10-20 cm and 8-15 degrees over 3-4 frames, easing out over about 8 frames. A lens change is a smooth zoom of at least 24 frames. Hold a downward tilt to about 75-80 degrees. Every move off the hero goes to an object (a person, a thing, an event), not to a point. No "blank wall" frames.

05.12 **No intersections or teleports: bodies do not pass through each other, furniture, doors or the operator, and the hero reacts to every touch.** Touches of 3-7 cm in grabs are allowed. "Hidden jumps in one take": lens by zoom of at least 24 frames, nothing appears off-screen.

05.13 **Doors and details on the interior and location images are made closed beforehand: the video model carries them into the clip.** The doors on a car-interior card are closed on purpose.

05.14 **Do not put a voice into the generation together with a 3D previz: the result gets overloaded, the animation worsens, quality drops.** Generate without voice and place the voice in the edit. In a long documentary take the model may generate "with sound" but without music (music cannot be separated from noises), and the voices are replaced later. Whether lip sync holds with a video and an audio reference together is untested, so check it with one cheap short clip.

### C. Camera from a phone

05.15 **For realism the camera movement is not described but filmed: the phone is the Blender camera.** The Omniscient app turns an iPhone into a virtual Blender camera and records the movement as a key on every frame. "We did not describe the camera in words, we filmed it."

05.16 **The actors adapt to the camera, not the reverse.** Only the camera is filmed with the phone, the heroes are not moved. The agent watches the screen recording with voice and the camera keys, finds the seconds and animates the heroes to fit the take. Corrections of the previz are written in your own words, each a new version.

05.17 **The camera carrier stands still and the world moves: "the car stands, the city drives".** The phone moves the camera in scene coordinates. If the car moved, the camera would stay hanging on the road. When the car is thrown left and right, move and rotate the city around it.

05.18 **Do not smooth hand shake. Remove only the freezes where frames repeat.** The phone sends its position less often than 24 times per second, frames repeat and the camera twitches. Fill repeated frames from neighbours. The free Omniscient tier gives live camera control and a limited number of recordings per day, the paid tier removes the limit and smooths hand shake (not needed here).

05.19 **Rehearse without recording, record the whole take, save the file immediately.** Turn on AR (a step forward is a push-in, crouching is a low angle, turning is a pan), rewind, press Play, film like an operator and speak the lines. Record with the red button, then save the file. Until it is saved, the recording lives only in the open scene and can be lost. A scene scale slider sets how many metres of scene equal one step.

05.20 **Match the Blender lens to the phone: a 13 mm camera matches the 0.5x lens on an iPhone, and the camera sits where the operator holds it** (for example in the driver's right hand in front of the face). When matching a camera to a photo, an iPhone ultrawide is about 13 mm, at a height of 2-2.3 m.

05.21 **Higgsfield's cloud 3D scene tools (`scene_builder_3d_*`) work when Blender is not installed, but they cannot use a phone camera and cannot import your own 3D models (only the Higgsfield catalogue).** If Blender is missing: build the scene from the spec there, show key frames, render the previz after "ok". (user's ok)

### D. Script checks of the previz

05.22 **Check the previz with scripts before rendering, not only by eye:** speeds of people and camera, camera jumps, who covers whom, intersections. The agent checks that nobody runs faster than a person, the camera does not jump, the heroine is in frame when she speaks and nothing covers her. The checks are `check_motion.py`, `check_view.py` and an intersection check in `.claude/skills/blender-previz/` (`scripts/`); a whole take is checked in seconds in background Blender. Look yourself first, then show, then wait for "ok". (user's ok)

05.23 **Before handing over, the scene is checked from different points that the agent views itself:** a side cut view (seat-back tilt), the camera view, a view from the back seat. Before rendering, a grid of frames (every 24th and the key ones).

05.24 **The best check of a set is a top-down plan (orthographic, no ceilings).** On a perspective render an upside-down object is easy to miss. Doors the camera or a character passes through are made open, and you check that the door leaf does not block the way.

05.25 **Tolerances come from the script.** Defaults of `check_motion.py`: walk 1.8 m/s, run 6.0 m/s, teleport 0.5 m per frame, operator 4.0 m/s, walking backwards 1.2 m/s, rotation 12 degrees per frame, lens 1.0 mm per frame, focus 0.35 of the distance per frame. A violation counts as a problem after 6 frames in a row. Frames of deliberate jerks go into `--allow`.

05.26a **Each script check is a rule: the previz is unfit if even one fires.**
- `check_motion.py`, people (on the floor, XY): faster than the walk limit of 1.8 m/s for more than 6 frames in a row; faster than the run limit of 6.0 m/s for those the spec names as runners (`--runners`, where the limit fires after 2 frames in a row); a position jump over 0.5 m per frame counts as a teleport. People are root objects with the `CHR_` prefix.
- `check_motion.py`, camera: a position jump over 0.5 m per frame; a rotation over 12 degrees per frame (shortest angle, q and -q are the same rotation); a lens jump over 1.0 mm per frame (a smooth 24 to 35 mm zoom over 24 frames gives about 0.7); a focus step over 0.35 of the distance per frame with nearly still neighbours (a focus pull needs an ease-in); an operator faster than 4.0 m/s or walking backwards faster than 1.2 m/s (both only if it lasts 6 frames in a row). Frames of intended jerks (blur, shove) go to `--allow` and jumps in position, rotation, focus and speed are not counted there; a lens jump is not forgiven by `--allow`. Problem spans print as "a-b: up to value"; if nothing is printed, it says everything is in range and the motion is continuous.
- `check_view.py`: the hero's head (`<hero>_Head`) must fall inside the frame with a 0.02 margin and be in front of the camera. A ray from the camera to the head must not hit another object visible in the render (parts of the character itself are skipped). It prints three lists: hero outside the frame (compare with intended moves in the spec), hero in frame but covered (with the names of the covering objects), empty frame (no visible head). It checks every 2nd frame (`--step`) and spans shorter than 3 checks are not printed (`--min`).
- Intersection check (the example script is adapted to the scene, names and tolerances change): a person is a capsule (axis from the body bottom to the head centre, radius 0.17-0.20 m), furniture and walls are boxes of the object sizes (for tables only the top, 0.06 m thick: below is empty), the operator is a vertical cylinder r 0.18 behind the lens (centre 0.15 m behind the camera, height 0.3-1.6 m). Penetration tolerance 0.03 m (operator 0.05 m). Intended contacts (sits on a chair, on a motorbike, a grab) go into `SEATED_ON` and `ALLOW` lists with frame ranges, decor, lamps, cables and handheld props go into `SKIP_OBJ`. It also checks that the lens does not go inside geometry (distance under 0.02 m).
- `render_preset.py`: default `previz` (EEVEE, short side 480 px, even sizes, 8 samples, shadows off on all lamps); `check` is Workbench 480 px without shadows; `hq` is 1080 px, 16 samples, shadows on the 6 strongest lamps and the sun. The script does not save the `.blend`. Argument order: script, output, render, then `-- preset`.

05.26b **Movement of the model in shot is set as a brief for movement: the previz gives position and path, the prompt carries the acting.** Without a clear brief the model invents motion, which produces artifacts, unnatural plasticity or changed shots. The way a character moves (a sharp head turn, a smooth walk, nervous gestures) speaks directly to the viewer. Questions a director asks: how does she walk, where does she look, what do her hands do, how does the movement relate to the surroundings. Blobs have no hands or face, so key phrases such as "idle movement, small unconscious gestures, realistic micro-motions" (very important for realism), "stumbling forward, losing balance, natural recovery motion", "reaching toward camera", "looking over shoulder" go into the acting of each shot in the prompt, not into the previz. The table of such phrases is in `docs/stages/02-film-language.md` and `templates/film-language.md`.

### E. Rendering the previz and the load on your machine

05.26 **Render the previz small and without shadows: Seedance takes only movement from it.** Default: 480 px on the short side (vertical 480x854), no shadows, EEVEE, 8 samples. More resolution, shadows or samples only if you ask. Checks and frame grids use Workbench. Course practice: 24 frames per second, 640x480 for 4:3 horizontal, a 25 s clip renders in about two minutes. Resolved default: fast grey render, no shadows. Turn shadows on only if a test shows the model mixes up depth.

05.27 **Do heavy work in background Blender, one process at a time, rendering from a copy of the `.blend`.** Through the MCP bridge the same script ran more than 10 minutes and hung the add-on, in the background it took 5 seconds. The user's open Blender window may overwrite a save. Use the MCP bridge only for viewing and small edits.

05.28 **Never overwrite old versions: every new previz or video is a new file. Prompts are edited in place in one file.** `ref_v2.mp4`, `ref_v3.mp4`.

### F. The previz role in the video prompt, and clip lengths

05.29 **In the prompt, write the role of the previz directly: it sets only the camera movement, the places of people and the car, paths and speed. Blob colour is only a label. Shape and light are not taken.** The prompt runs by seconds, with the camera angle written for each span as in the previz. Each blob is named for what it becomes (pink = Anna, blue = the driver, black box = the car). The acting of each person is written in the prompt of each shot. See `templates/previz-in-video-prompt.md`.

05.30 **A generator may cut a long take into pieces, and the join is hidden in blur.** Seedance 2.5 takes pieces of up to 30 s. The join frame is fully covered by a body very close to the lens plus blur, a wipe is a run without a tilt, and the last frame of piece 1 equals the first frame of piece 2. Takes of 25 s and 30 s were made in a single pass without cuts.

05.31 **The length and size of the reference clip depend on the model and the host.** Kling 4.0: up to 5 videos of 3-30 s, total up to 30 s, side at least 700 and at most 4553 px, up to 300 MB, 24-60 fps, ratio 2:5 to 5:2. A 640x480 previz does not pass the 700 px limit, so it was enlarged with ffmpeg to 960x720 (`scale=960:720:flags=lanczos`) and the host accepted it. Seedance 2.5 on one host: up to 10 video references of 2-30 s, total at most 30 s, 480p/720p, frame area from 409,600 to 927,408 pixels, 24-60 fps. Our own research: some Seedance hosts allow 3 videos of 2-15 s in total, up to 50 MB; render each shot of the cut as a separate continuous clip of about 3-8 s, at most 720p, H.264; do not use jump cuts inside a reference. Ratios and limits differ by host, so before rendering test your host's validator on one clip (see "Check before ok").

05.32 **A 480p draft can be taken to 1080p as the same take, not as a new one.** Only a draft started as a draft can be finished. After the user's yes, the agent names the price from `estimate_video_cost`. The generation itself belongs to stage 06.

05.33 **The link between Blender and a video model.** One lesson says it works only with Seedance. Another model note says Kling 4.0 takes a white-model blockout and a depth video as a standard input. In one test Kling kept both cars as in the images. The studio default is Seedance 2.5 and the Kling route is a test (see "Common mistakes").

### G. Library of camera moves

05.34 **Name the camera move explicitly: it is one of the key factors of a good generation. Without it the model makes random or unwanted moves.** Movement is storytelling: a slow push-in builds tension, a tracking shot adds dynamics, a static frame focuses on details. A table of 33 moves (static, pan, tilt, dolly, arc, pedestal, crane, handheld, tracking, zoom, dutch, overhead, whip pan, vertigo, orbital descent, focus pull reveal and others) with an English prompt phrase each is in `templates/film-language.md`. Use the templates as a base and adapt them.

05.35 **In the previz the same move is built once and reused.** An accepted camera move from a Blender reference, supplied with another start frame, gives the same choreography. Keep a library of named moves (push-ins, orbits, whip-arounds). Record each move in five parts: name, movement, speed, framing, end.

05.36 **Movement of the model in shot is a brief:** not "the model walks", but "how does she walk, where does she look, what do her hands do". Without a clear brief the network invents movement, which often leads to artifacts, unnatural plasticity or a changed shot. The long table of 43 phrases is in `templates/film-language.md`.

### H. A room from photos, and the previz start frame

05.37 **A room is built from photos like this:** all photos in one grid, the layout in words, axes and sizes in one line at the top of the script, the scene as one script (one function per object), rebuilt from scratch with no hand tweaks, then render the same angles, a "photo / render" grid, correct, usually 3-4 rounds. Ask a person who knows the room for three anchor sizes (ceiling, door, room length) and the positions of mirrors and glass: they are not visible in photos, and a person names them in a minute. Furniture as ready-made functions, not plain boxes.

05.38 **One coordinate system for the whole take: origin, axes, where we look from. Say "facing the table", not "left/right" with no reference point.** Leave room for the operator: the body is about 0.15 m behind the lens and there is room to step back. The corridor for the camera may be wider than the real one.

05.39 **A start frame from a viewport screenshot is matched with 7 points of known coordinates:** the error is about 8 px, and a 50 mm viewport equals a 25 mm camera.

### I. More from the Blender lessons (also relevant to stage 06)

05.40 **In the video prompt, documentary feel and the heroes repeat in every shot, not once at the start.** If you write it once, the model flattens the picture. Name the hero with the image in each span ("the freak, @Image7") so faces do not get mixed up. Write that the street lives (cars, pedestrians), otherwise Seedance makes an empty city.

05.41 **References: up to 25 in a Seedance 2.5 prompt through an aggregator, each mentioned 3-4 times. Streets A, B, C do not need to be tied to seconds: "the model understands the city itself".**

05.42 **Upscale the clip (to 2160p, x2) and re-voice it after generation.** See stage 06 (06.53) and stage 07.

## Workflow

Variant A: previz from a spec (the default).

1. Set up the environment: Blender (blender.org or via the agent: Homebrew on Mac, winget on Windows), the project folder with the video reference, and `.claude/skills/blender-previz/SKILL.md`.
2. Director's storyboard: ask the agent with the idea, format, length and a link to the video reference; write `shot-spec.md`. Check three things: time in whole seconds; it is visible where slow motion is and where normal speed is; text stands in the seconds where it is spoken. (user's ok)
3. Reference images for everything that must be drawn exactly (stage 04): hall, facade, car, interior (doors closed), heroine, driver.
4. Voice: record it or get a table of lines by second.
5. Set from images or photos. Ask for the three anchor dimensions. One coordinate system.
6. Blocking: table, top-down plan, 5-9 key frames. Show it, wait for "ok". (user's ok)
7. Check the spec against physics, list the conflicts. Show them.
8. Animate by dependency: the hero's path, background, camera, gaze and props, the rest. Use scripts in background Blender.
9. Run the script checks and the frame grid; look yourself; then show.
10. Render with the `previz` preset (480 px, no shadows). Say how long it will take. Save as a new version.
11. Report: what was done, departures from the spec, a correction for the spec, facts about the place.
12. The user watches the previz and writes corrections in their own words, each a new version. The stage closes with "ok". (user's ok)

Variant B: camera from a phone.

1. Install Omniscient on the phone and the add-on in Blender (Blender 4.2+).
2. Build the scene "the carrier stands, the world moves" (request below). The agent renders check frames and looks at them itself.
3. Connect the phone: Blender, key N, the Omniscient tab, Virtual Camera, QR code; on iPhone the Virtual Cam tab, New Virtual Camera Session, point at the QR. Same Wi-Fi (not a guest network, VPN off). If the network is blocked, turn on Omniscient in Settings, Privacy, Local Network.
4. AR: "AR moves the active camera, not the viewport". Show Camera. If you walked off: turn AR off, return the camera, turn it on again.
5. Rehearse without recording (time at the start, Play, film like an operator, say the lines).
6. Record the take: screen recording with the microphone (for example QuickTime on Mac), red button on the phone, play the whole take, stop, save the file.
7. The agent transcribes the voice, makes a table "second, camera, line", shows it before animating; animates the heroes to fit; removes camera freezes but keeps shake; checks intersections and shows the frame grid; renders the previz without shadows.
8. Corrections by voice by seconds, each version new. (user's ok)
9. Next: stage 04 images, stage 06 prompt and generation, upscale and post.

Test of the host limit before rendering (open question): upload the same previz in 640x480, 480x854 and 960x720 to the chosen host and see which it accepts. If the host rejects it at upload, the test costs nothing. Do not start a paid generation on a clip the validator rejected.

## Formulas

Scripts (run from the skill folder; paths are examples):
```
blender -b scene.blend --python .claude/skills/blender-previz/scripts/check_motion.py -- --runners Hero,Friend --allow 369-378,714-726
blender -b scene.blend --python .claude/skills/blender-previz/scripts/check_view.py -- --hero CHR_Hero --step 2
blender -b scene.blend --python .claude/skills/blender-previz/scripts/render_preset.py -o //render/ref_#### -a -- previz
blender -b scene.blend --python render_preset.py -o //sheet/f_#### -f 0 -f 48 -- check
nice -n 10 Blender -b ...
```

Render presets (measured on a laptop with 16 GB memory, a scene of 13 thousand polygons, 22 lamps, depth of field and motion blur, 1441 frames = 60 s):

| Preset | Settings | s/frame | 60 s of video |
|---|---|---|---|
| `check` | Workbench, 480 px short side | 0.03 | about 1 min |
| `previz` (default) | EEVEE, 480x854, no shadows, 8 samples | 0.17 | about 4 min |
| `previz --samples 16` | the same with 16 samples if blur shows grain | 0.33 | about 8 min |
| `hq` (only on request) | EEVEE 1080x1920, 16 samples, shadows on 6 lamps | 0.74 | about 18 min |

Ten mistakes of previz work, each with a rule: voice before previz; anchor sizes from a person; one coordinate system; for each beat say what must be visible (`check_view.py`); speeds in numbers (`check_motion.py`); lens by zoom of at least 24 frames, no teleports; action through the body and a dictionary of terms in the spec; default "banks" and state shown by colour; leave the hero for an event; a plan and a grid instead of expensive render rounds.

Blocking request (the shape; use the agent's own words):
```
Make a 3D storyboard of the clip in Blender with the blender-previz skill.
Take shot-spec.md and the images in frames/: hall, facade, car, heroine.
Blocking first: a table "time, where is the camera, car, driver, heroine, guests, what is visible", a top-down plan with the paths of the car, camera and guests, and 8-9 key frames. Show it and wait for my ok.
Format 4:3, one take, 25 s. People are simple figures: cylinder, head and a nose showing where the face looks. The car is a sedan like the image: hood, roof, pillars, windows; side windows open, dashboard, seats inside. The driver at the wheel, the heroine behind the driver on the far seat. Many guests, the nearest tables at the window.
```

Scene for a phone take (shape):
```
Build a Blender scene for a phone-camera take from inside a moving car, using the blender-previz skill.
1. 30 seconds, 24 fps, horizontal 4:3.
2. The car is a black executive sedan of about 5.4 x 1.92 x 1.5 m, with a full interior and four doors on hinges, side windows down.
3. The car stands still and the city drives past at 50 km/h: road with markings, lamps, trees, houses, parked and oncoming cars, wheels spinning to match.
4. People are blobs: cylinder, head and a nose. Seated, legs visible. Driver yellow, one hand on the wheel. Front passenger light blue. Rear behind the driver pink.
5. Camera CAM_PHONE with a 13 mm lens (like 0.5x on iPhone), in the driver's right hand in front of the face, looking at the road. Make it active.
6. Save the scene in the 3d folder and open it in Blender.
7. Before handing it over, render check frames: a side cut view (check the seat-back tilt), the view through CAM_PHONE, and a view from the back seat. Look at them yourself and fix what is wrong.
```

Animation to the take (items 1 and 4-6):
```
1. Transcribe the voice and match it to the camera keys: a table "second, what the camera does, who says what". Show it to me before animating.
4. Do not move the camera, only remove the freezes: fill repeated frames from neighbours. Keep the hand shake.
5. Check that nobody passes through seats, doors or the camera. Show the frame grid.
6. Render the previz 640x480, no shadows, save as ref_scene_v1.mp4 in the video folder.
```

Role of the previz in a Seedance prompt (shape; the Chinese JSON form is in `templates/video-prompt-seedance.md`):
```
@Video1 is the latest previz: only the camera movement, the places, the paths and the speed of the car and the people.
Give each blob colour a role: pink is Anna, blue is the driver, the other colours are guests.
In each shot write the angle and the acting of each person: pose, face, hands, a gesture on a specific word. Write only what is seen and heard, short, no repeats. The car doors stay closed all the time.
```
The Seedance 2.5 JSON form of this rule: `@Video1 只提供镜头运动、人物位置、路线和时间，不提供人物外貌、表情和手部动作` (it provides only camera movement, positions, paths and timing, not looks, expressions or hand acting). The acting goes into the acting field (`表演`) of each shot.

Role of the previz for Kling 4.0 (`templates/video-prompt-other-models.md`):
```
@Video1 is a coloured white-model blocking animation of this exact shot, with no sound.
It is a moving blueprint and controls only the motion: the camera's path, height, framing and lens changes, the timing and speed changes, and the positions and paths of the car and the people. Follow it frame by frame. Its pink figure becomes Anna from @Image4, its light-blue figure becomes the driver from @Image5, its black box car becomes the car from @Image3, its room becomes the hall from @Image1, its other cylinders become guests. Do not take its flat untextured shapes, primitive geometry, colours or lighting.
```

## Check before "ok"

Storyboard:
- [ ] Time everywhere is whole seconds.
- [ ] It is visible where slow motion is, where normal speed is, and when the transition is.
- [ ] The user's text stands in the seconds in which it is spoken.

Blocking:
- [ ] The table, the top-down plan with paths and 5-9 key frames were shown, and the user said "ok".
- [ ] Conflicts of spec and physics are listed, nothing was sped up silently.

Previz before rendering:
- [ ] Nobody runs faster than a person (`check_motion.py`: walk up to 1.8 m/s, run up to 6.0, no teleports over 0.5 m per frame).
- [ ] The camera does not jump: no position jumps, no rotation over 12 degrees per frame, no lens over 1.0 mm per frame, no focus step (except frames listed in `--allow`).
- [ ] The hero is in frame when speaking and nothing covers them (`check_view.py`). No empty frames.
- [ ] No intersections (tolerance 3-7 cm in grabs) and nobody passes through seats, doors or the operator.
- [ ] People: no spans over 1.8 m/s (runners per spec up to 6.0 m/s) for more than 6 frames in a row and no position jumps over 0.5 m per frame.
- [ ] Camera: no position jumps over 0.5 m per frame, rotation over 12 degrees per frame, lens over 1.0 mm per frame, focus step over 0.35 of the distance; the operator is not faster than 4.0 m/s and does not walk backwards faster than 1.2 m/s for more than 6 frames. Intended jerks are in `--allow` and match the spec.
- [ ] The hero's head is in the frame with a 0.02 margin and is not covered by another object. Moves off the hero match the table of moves in the spec. No frame shows no person at all.
- [ ] Intersections: person capsules, furniture boxes, the operator cylinder r 0.18 behind the lens; penetration at most 0.03 m (operator 0.05 m); the lens does not go into geometry closer than 0.02 m; every intended contact is in the exception lists with frames.
- [ ] What must be closed is closed (windows, doors), because "Seedance carries over everything it sees".
- [ ] Camera shake is what the video needs.
- [ ] Render is 480 px, no shadows; for Kling the side is at least 700 px; the version is saved as a new file.
- [ ] The host's validator accepted the clip at that size before any paid generation.
- [ ] For a phone take: the `.blend` was saved after recording; freezes removed, shake kept; the heroes animated to the take; the frame grid reviewed.
- [ ] The report contains departures from the spec and a ready correction for the spec.

Money: a previz costs nothing, but the next stage does. Before it, the price message lists the model, the number of jobs and the credits from `estimate_video_cost`, with this checklist. The stage closes only after the user's "ok".

## Common mistakes

From the lessons:
- Describing a complex camera only in the prompt: the model does its own thing, many tries are needed, each costs money.
- Fractions of a second in the storyboard.
- A person with hands in the 3D previz moves like a game character; a voice in the generation together with 3D; closed car windows and an open door on the interior image carry into the video.
- Camera shake in the previz that is not needed; expression and lips taken from the blob.
- A weak model or low reasoning effort for the 3D work.
- Generating straight in 1080p with no draft: only a draft can be finished to 1080p.
- Installing skills by hand; making new prompt files instead of editing one.
- Moving the car in the scene: "it drives off and the camera hangs on the road".
- Smoothing hand shake; writing "handheld" once at the start of the prompt; not naming the hero with the image in every shot; not writing a living street; music in the generation.
- Not saving the Blender file after a phone recording.
- Connecting the phone: VPN on (turn it off); a guest Wi-Fi; Blender not restarted for a new QR code.
- Room echo on the voice recording.
- Cloud 3D scene tools cannot do a phone camera or your own 3D models.

From the skill (ten mistakes): timing from text, voice later; sizes by eye; "left/right" with no reference point; undecided what covers the hero; movement "like a game"; hidden jumps in a "single take"; words with two meanings; no agreement on what the previz shows; a robot camera; expensive render rounds.

Blender 5.x gotchas: no `action.fcurves`, curves live in slots (`bpy_extras.anim_utils.action_get_channelbag_for_slot`); find non-English node names by type (`BSDF_PRINCIPLED`); set colour in the node (EEVEE) and in `diffuse_color` (Workbench); compound objects built from cylinders use quaternion mode and a rotation by angle is silently ignored; an IK leg with no pole bends the knee the wrong way; reset foot steps at a join. On 16 GB of memory extra processes cause swapping. Do not touch a file the user has open. Do not render several processes in parallel; do not push heavy work through the MCP bridge; do not raise resolution, shadows or samples without being asked.

Open questions to test, not to assume: whether Kling works as well as Seedance with a Blender previz (one cheap run each, same previz, compare that objects survive); whether lip sync holds when both a video and an audio reference are used; which preview size and ratio the host accepts (see above). Until tested, the default is Seedance 2.5 and nothing here is a promise.

## Tools

Check `models_explore` for current models and `estimate_video_cost` for the price before any paid run. Never rely on a remembered price.

| Tool | Role |
|---|---|
| A capable coding agent with the strongest model and high reasoning effort | Builds the scene by script, animates, renders the previz, writes prompts, runs generation. |
| Blender (free, blender.org) | 3D blockout, camera, previz, render; background Python scripts or live via MCP. Blender 4.2+ for Omniscient. |
| MCP for Blender | Viewing the scene and small edits; port 9876; do not push heavy work through the bridge. |
| Omniscient (iPhone, iPad, plus a Blender add-on) | Phone as a Blender camera, movement recorded as keys. |
| Higgsfield `scene_builder_3d_*` tools | Cloud Blender when Blender is not installed. No phone camera, no own models. |
| `seedance_2_5` (omni reference, `video_references`) | Generation from the previz and the images (stage 06). Drafts at 480p. |
| `kling4_0` | Accepts a white blockout and depth video as a motion reference. Reference video at least 700 px on the shorter side, 3-30 s, total at most 30 s; there is no 4:3 option. |
| `bytedance_video_upscale`, `topaz_video` (paid) or a local upscaler | Final upscale after generation. |
| ffmpeg | Resize a previz to a host-accepted size, extract frame grids. |
| Screen recording with voice (QuickTime on Mac or any recorder) | Phone take recording. |
| Image tools of stage 04 | Reference images of hall, streets, driver. |
