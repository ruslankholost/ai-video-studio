# Video prompts for other models

Seedance 2.5 is the default (`templates/video-prompt-seedance.md`). Use another model only for the reason given in its section. Each model reads prompts differently, so do not paste a Seedance prompt into it. For every model: check `models_explore` for current ids and limits, and `estimate_video_cost` for credits before any paid run, with the user's explicit "yes" on the exact list.

| Model | Use it when | Where |
|---|---|---|
| `kling4_0` | You need exact camera moves, strong reference fidelity, intermediate keyframes, or a cheaper long take | Higgsfield |
| `minimax_h3` | Motion design: product launch or title films with exact colours and exact on-screen text | Higgsfield |
| Gemini Omni Flash / Veo | Conversational editing of a clip, readable text in the frame, or syncing to an uploaded audio | External only, not on Higgsfield |

Seedance still wins for realistic physics, contact action (fights, collisions), long takes up to 30 s, and many references. Kling is weaker there.

## Kling 4.0 (`kling4_0`)

**Use it instead of Seedance for**: precise camera work, a single long move, characters and cars that must match their reference cards, keyframes in the middle of a clip, and lower cost. Not for fights or crashes (hits hang in the air, falls look cartoonish), and not for takes over about 15 s (a long take degrades; do two passes of 15 s or add keyframes).

**Language**: write in English. Dialogue stays in the speaker's language, in quotes. Russian is not in the official speech list, so lip sync is not guaranteed; if it matters, record the voice and lay it over.

**Principle**: describe, do not forbid. Negative instructions raise the chance of errors. There is no negative field. The only two bans are "No subtitles" and "No background music". Write everything else positively: not "no open doors" but "four doors closed from start to end". Replace judgement words ("premium", "cinematic", "epic") with visible facts (side backlight outlines the edges, 24 mm, warm tungsten key from the left).

**Structure**: capitalised blocks, in this order:

1. `SCENE CONTEXT`: exact count of characters in capitals, duration, format, genre, story in 3 to 5 sentences.
2. `ACTIVE REFERENCES`: a role for every file: what it defines, what to keep, what NOT to take (pose, expression, background).
3. `LOCATION MAP`: who stands where, facing where, direction of movement, which side the camera is on.
4. `CHARACTERS`: look, clothes, temperament; objects with their orientation.
5. `FORMAT MODE`: one continuous take or N shots with cut times; speed changes.
6. `OPTICS`, `CAMERA`: lenses; character of the camera (handheld with visible breathing, or smooth stabilised).
7. `ACTION TIMING`: beats, each with `CAMERA:` then `ACTION:` then `ACTING:` then `DIALOGUE:`.
8. `PHYSICS`, `LIGHTING`: weight and inertia; one motivated light source.
9. `AUDIO`: sound by time, dialogue, "No background music".
10. `STYLE`, `QUALITY`, `POSITIVE CONSTRAINTS`: look, what must stay identical, what must be in frame, "No subtitles, no on-screen text".

The three Seedance rules apply: camera first in every beat (point, height, angle, lens, focus, then the path of the move), acting through the body in every beat, a role for every file.

**Rules**:
- Multi-shot is on by default and cannot be turned off. For one take write "The entire sequence must be one continuous master shot with no visible cuts" in `FORMAT MODE` and "The same shot continues." in each beat's camera line. For cuts list the shots with times and what motivates each cut.
- Fractions of a second are allowed (`0.0-0.8s`), but 2 to 4 s per beat is better for drama. Beats are contiguous and cover the whole clip.
- Sound is always generated and music is added by default. Say "No background music, no score, no song".
- Name each character in each beat. A beat that does not name the driver leaves the car driving itself.
- Write the exact count ("EXACTLY 2 MAIN CHARACTERS, NO DUPLICATES"). Kling adds people and objects to explain a picture.
- Aspect ratios: 21:9, 16:9, 1:1, 9:16, auto. There is no 4:3. For 4:3 set auto, write "horizontal 4:3" in the scene context and supply a 4:3 previz.
- Higgsfield call: `generate_video` with `kling4_0`, modes text-to-video, image-to-video, reference-to-video (`video_references` for previz, see `templates/previz-in-video-prompt.md`), `start_image`, `end_image`, `image_references`, 720p or 1080p, 3 to 30 s.
- Editing an existing clip: start with "Edit @Video1." then the change, then "Keep everything else unchanged" and name what stays (background, camera, light, length, sound).
- Intermediate keyframes: "Use @Image1 as the first frame ... `4-6 sec | Keyframe 1: what happens and how the camera gets there`".

**Short example** (6 s):

```
SCENE CONTEXT: EXACTLY 1 MAIN CHARACTER, NO DUPLICATES. 6 seconds, vertical 9:16, quiet drama. A courier waits at a door and decides not to knock.
ACTIVE REFERENCES: @Image1 is the only source for the courier's face, hair and jacket. Do not take its pose, its expression or its grey background.
FORMAT MODE: The entire sequence must be one continuous master shot with no visible cuts.
OPTICS: 35mm, shallow depth of field. CAMERA: smooth stabilized, no handheld shake.
ACTION TIMING:
0-3s
CAMERA: 1.5 m high, 2 m in front of the courier, eye level, slow push-in to 1.2 m, 35mm, focus on his eyes.
ACTION: He stands at a hallway door holding a parcel.
ACTING: He holds the parcel against his chest with both arms, weight on the left foot; brows drawn together, eyes fixed on the door handle, lips pressed.
3-6s
CAMERA: The same shot continues. The push-in ends at 1 m.
ACTION: He raises a fist to knock, stops an inch from the wood.
ACTING: His shoulders rise on an inhale, the fist trembles, then he lowers it and exhales through his mouth, head dropping.
AUDIO: Quiet hallway hum, one slow breath, footsteps fading at the end. No background music.
POSITIVE CONSTRAINTS: One person in frame. The door stays closed. No subtitles, no on-screen text.
```

## MiniMax H3 (`minimax_h3`)

**Use it instead of Seedance for**: motion-design films, product launches, logo reveals and title cards, where the palette must hit exact hex values and every on-screen string must stay straight. It holds text and interfaces when the prompt lists exactly what is written. It is not the model for live-action drama with acting.

**Limits** (check `models_explore`): 4 to 15 s, up to 2K, aspect from 21:9 to 9:16 including 16:9, 1:1, 4:3; text, first and last frame, or references; up to 4 variants per run. Default plan: 15 s, 16:9, 30 fps, silent.

**Language**: English, one continuous text, physical and concrete (materials, light direction, exact percentages, frame counts), not adjectives.

**Structure**, in this order, every block present:

1. Format line: type of film, aspect, fps, duration, style name and one-paragraph style definition.
2. Silence line, if silent: "Fully silent piece, no soundtrack, no sound design; all rhythm is carried by motion timing and cuts alone."
3. Background and world.
4. `PALETTE (locked)`: hex codes with named roles, where each colour may and may not appear.
5. Hero, mass or surface: the full product or character definition with one identity anchor, a signature feature that makes the silhouette original and keeps it identical across scenes.
6. `TYPE TREATMENT`: font character, how text enters and leaves, which word gets the accent colour.
7. `MOTION LANGUAGE`: easing, transitions, what is allowed and forbidden.
8. `BEAT SHEET`: timed beats such as `0.0-1.6s`, each with action, exact copy, accent word. A beat every 1.5 to 2 s; the last beat is a lock-up (wordmark, second line, small call-to-action chip) held about a second.
9. `COPY LIST`: every string that appears on screen, verbatim, closing with "exact strings, nothing else appears in frame". This line is what keeps text from drifting.
10. Content safety, non-IP: invented designs, greeked background text, no real logos, people or landmarks.
11. Consistency block (restate the identity anchors), camera and motion (moves allowed, moves forbidden, blur policy), render block (materials, light, what must not appear, for example no grain, no vignette, no lens flare).

**Rules**:
- One core mechanic per film that a viewer could retell in one sentence ("the world is black and white, only the product is coloured", "one continuous morph with no cuts"). Invent it first, then write beats that prove it.
- Style by constraints, not adjectives: chaos styles get rules ("jitter only on beat landings"), clean styles get prohibition lists, hybrid 2D and 3D styles get a layer rule (2D never gets lighting, 3D never goes flat).
- Vertical 9:16: add safe zones (top 12 percent and bottom 15 percent free of type), stack headlines in 2 to 3 short lines, recompose horizontal moves into vertical ones.
- If a clip is shorter than the plan, split the beat sheet into segments at natural seams and restate palette, hero and anchor in each. Never split mid slow motion or mid morph.
- Drift is the main failure: repeat the identity anchor in the beat that matters most and keep hex codes exact. Keep a Plan B (fog instead of a particle cloud, three segments instead of one take).
- Cheap order: storyboard grid as one image first, approved by the user, then the video from it as `start_image` or reference. Collect edits in one batch.

**Short example** (4 s title card):

```
4-second motion-design title card, 16:9, 30 fps, silent. Style: flat paper cut-out, layers move on soft springs.
Fully silent piece, no soundtrack, no sound design; all rhythm is carried by motion timing and cuts alone.
Background: matte off-white paper #F4F1EA.
PALETTE (locked): paper #F4F1EA background; ink #1B1B1B for text; accent #E4572E only for the accent word and the chip.
HERO: a paper boat with one identity anchor, a single folded red tip on the bow, visible in every beat.
TYPE TREATMENT: heavy rounded sans-serif, words drop in with a small bounce and settle fully; accent word in #E4572E.
MOTION LANGUAGE: springs settle completely, no easing overshoot beyond 5 percent, no camera shake.
BEAT SHEET:
0.0-1.6s: boat slides in from the left, copy "Slow mail".
1.6-3.2s: boat stops at centre, copy "arrives on time".
3.2-4.0s: lock-up, wordmark "Paperboat" and chip "Join the list", hold.
COPY LIST: "Slow mail", "arrives on time", "Paperboat", "Join the list". Exact strings, nothing else appears in frame.
CAMERA: locked off. RENDER: no grain, no vignette, no lens flare.
```

## Gemini Omni Flash and Veo (external only)

These are Google models and are not on Higgsfield. Use them outside the studio's Higgsfield flow, only when the user already has access and the task needs one of: conversational editing of a clip over several turns (change one thing, keep the rest), readable text rendered inside the video, syncing a clip to an uploaded audio track, or text, images, audio and video as inputs together. Check the current limits and availability yourself, they change. Clips are about 10 s, every clip carries a hidden watermark, and the quota per session is small.

**Language**: English.

**Structure**: cover six dimensions, camera first, because the camera instruction sets the visual grammar of the whole clip:

```
[Camera]: shot type and move.
[Subject/Action]: who does what, in detail.
[Location]: where, with detail of the surroundings.
[Lighting]: specific light.
[Style]: look, colour range, mood.
[Audio]: sound or music.
[Text]: only if text must appear: content, position, style, time on screen.
```

**Rules**:
- Use camera terms as commands: locked off, oner, push in, pull back, orbit, tracking shot, crane up, handheld, Dutch angle, POV, overhead.
- Multi-turn is the strength. Do not rewrite the prompt. Change one variable per turn and add "Keep everything else identical" (or "Preserve all previous changes"). Three to five turns beat one long prompt.
- Multi-input prompts say what comes from where: "Using the uploaded image as the reference for the character's appearance ...", "Apply the camera movement of the uploaded video ...", "Match the rhythm of the uploaded audio". Upload audio rather than describing it.
- Use real-world facts for physics and light ("golden hour light at 47 degrees north in late October", "accurate surface tension on the splash").
- Face drift fix: "Keep the character's face, outfit and physical features identical across every frame. No identity drift."
- Its clip length is short, so plan a long video as several clips and join them in post (`templates/montage.md`).

**Short example**:

```
Camera: locked off, medium close-up at eye level.
Subject/Action: a baker in a flour-dusted apron lifts a loaf out of the oven, steam rises past her face, she smiles at the crust.
Location: a small bakery at dawn, wooden shelves, a cooling rack behind her.
Lighting: low warm sunlight through the shop window at 15 degrees, long soft shadows, amber highlights.
Style: natural colour, shallow depth of field, photographic.
Audio: oven door clank, soft crackle of the crust, quiet street outside. No music.
Text: none.
```

Second turn, to change only the camera: `Change the camera to a slow push in. Keep everything else identical: same character appearance, same lighting, same background, same pacing, same audio.`
