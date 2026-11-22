# 02 Film language

A reference stage: the vocabulary and rules from which the storyboard and the prompts are built (shot sizes, angles, lenses, light, camera movement, model movement, emotions, effects, ultra-realism, film look). The model will generate any frame. Deciding which frame is needed and why is the director's job, and that job is yours before any generation. The full dictionaries (28 angles, 30 lenses and 11 apertures, 46 light terms, 33 camera moves, 43 model-movement phrases, 30 emotions, 28 film stocks and cameras, 25 effects, genre playbook, one-take rules) live in `templates/film-language.md`. This file holds the principles and the order of work.

## Input and output

Input (in the project folder before the stage starts): `brief.md`, `idea.md`, `script.md`, `moodboard.md`, a draft `storyboard.md` (what happens in each scene, without the language of the frame).

Output: in `storyboard.md` each segment has a described shot (6 elements, principle 02.09), the video names one genre set and one light; a "Film language of the project" block is written in `moodboard.md` or at the top of `storyboard.md` (focal lengths, light and its temperature, film stock and grain, genre). These shots then go into the prompt file.

## Principles

### Direction and rhythm

02.01. Meaning first, then the frame. A director does not ask "which shot do I film" but "what must the viewer understand and feel now, and why now". If a shot has nothing to say, it is extra, however beautiful. Every shot says something to the viewer.

02.02. Shot size is language: each size answers its own viewer question. Wide: where are we. Medium: who is it and what do they do. Close: what do they feel. Extreme close: what to look at now. The closer the shot, the closer the viewer to the hero and the stronger the emotion.

02.03. Emotion cannot be demanded from the first frame, it is led up to: first where we are, then what happens, then what the hero feels. The viewer approaches the hero gradually, which is why the ring at the end hits hard. Start with the ring and it means nothing. Resolved (the course wins): the ladder is wide, then medium, then close, then extreme close at the peak, and the start is quieter. The hook rule still holds: the first frame is clear without sound, but it poses a riddle and does not give away the ending or show the peak. Write one emotion per shot next to the storyboard, readable and different across shots (an arc).

02.04. The whole video in one shot size is the main mistake: the eye gets used to it and attention leaves. Alternate wide, medium, close, details, and again in a circle. Eye-level camera in every shot makes a video boring. Every shot must carry information: viewers do not watch empty shots. Three face close-ups in three seconds is too many.

02.05. Three questions before each scene: what changes in the hero, where is the peak of tension, at what moment must the viewer be closest.

02.06. Give the camera a role: Observer (stands still, medium shots), Voyeur (wide shot and slow zoom), Interlocutor (close-ups at eye level), Pursuer (moves behind the hero, handheld), Judge (extreme close accents on details). The role sets the movement and the distance to the hero.

02.07. Write the shot size in English at the start of the prompt (`extreme wide establishing shot`, `medium shot`, `close-up`, `extreme close-up`), otherwise the frame forms "as it comes".

02.08. Context before the storyboard: the first block of any story prompt is the "SCENARIO" (genre, stakes, motivation of the characters, what this is NOT, the place of the video in the story). Without context the model draws each frame literally and unconnected.

02.09. Describe a shot, not an event. Each segment holds all six elements: `[lens] + [camera position and height] + [camera movement] + [composition by thirds] + [light inside the frame] + [what is out of focus]`. An unnamed element is chosen by the model and it is almost always boring (eye level, 50 mm, center, flat light). An example of turning an event into a shot is in `templates/film-language.md`.

02.10. Optics set rhythm: chaos, scale and chases with a wide angle of 14-24 mm; isolating a gag or an emotion with a telephoto of 85-135 mm; neighboring shots on different focal lengths. The contrast of focal lengths between neighbors gives a feeling of expensive editing.

02.11. Depth in three layers: an out-of-focus foreground, a sharp subject, depth in haze or light (1-1.5 stops darker than the foreground). For any shot with no foreground, check whether one can be added. An out-of-focus foreground immerses the viewer in the atmosphere.

02.12. One genre is one coherent set of decisions (optics, angles, light, movement, rhythm). Do not mix sets inside a video without a reason. The genre playbook (thriller or noir, horror, comedy, drama, documentary, action, ad, music video) is in `templates/film-language.md`.

02.13. Light is one for the whole video and is named in every segment. The hook is in the first 1.5 seconds (resolved: the idea is clear from the first frame without sound, details open by second 3). The arc goes from wide to close, or is consciously reversed. Slow motion only on gags and beauty, not longer than 3 s in a row.

02.14. A continuous shot (oner) loses editing rhythm, so it must be replaced: at least one event of five substitutes every 8-10 seconds (change of environment, reveal, change of scale, entry or exit of characters, change of speed). A one-minute take is 6-8 events.

02.15. How to write a oner for AI: write camera movement as a path, not as two points (the model joins two positions with a cut); on a push-in the frame only narrows; between blocks use continuity marks instead of CUT; the words "CUT", "cut to" and "moving on to" are banned inside a take. These three rules come from practice, ordinary film sources do not have them.

02.16. A long take is not made for the trick. Check question: what does this scene lose if cut? If "nothing", a oner is not needed.

02.17. If the video is assembled from several generations, plan the seam in advance and put it into a smear, behind an object, into a dip to dark or a dark zone. Classic cuts (cut on action, J-cut, L-cut, match cut, smash cut) are covered in stage 08.

### Angles

02.18. The name of the angle goes into the prompt and it is the name that gives the result. Use the exact angle names from the dictionary (28 angles in `templates/film-language.md`).

02.19. First create the character, then try angles and locations on them. Angles that depend on the scene (reflection, overhead, over-the-shoulder, insert) are supplemented with a description of the scene.

02.20. "Make a photo from another angle" usually does not work: the model does not guess what is off frame. Everything not written, it invents, and the result is mediocre. Take angle and pose from a detailed description of the reference made by the agent.

02.21. A moodboard is a set of angles (wide, close, details), not feed scrolling: targeted search with notes "angle from here, light from here, clothes from here".

02.22. Each shot of a series needs its own angle. A series of shots in one angle counts as a mistake.

### Lenses and aperture

02.23. A lens in the prompt is language, not fussiness: it changes perspective, depth of field, emotion and genre code. Without it the network chooses itself and gives an average standard result. For video this is especially critical. Dictionary: 30 lenses and 11 apertures.

02.24. Aperture: the smaller the f-number (f/1.4, f/1.8), the blurrier the background; the larger (f/11, f/16), the more is in focus. Prompt formula: lens + f-stop + effect (`85mm portrait lens at f/1.4, creamy bokeh`).

02.25. Focal length guide: 14 mm dramatic distortion; 50 mm "like the eye sees"; 200 mm compressed intimate picture; wide 14-24 mm epic; telephoto 135 mm and up isolation; macro detailed objects; 70-200 reportage or sport; fisheye skate culture and action.

02.26. f/4 gives a cinematic balance of sharpness; f/1.4-2 only for portrait close-ups.

### Light

02.27. Light forms mood, creates volume, directs attention and carries emotion. Knowing the terms (hard and soft, key, fill, back, rim, low and high key, Rembrandt and others, 46 terms in the dictionary) lets you control the language of the frame.

02.28. Light is most often the biggest jump in a picture: it turns an average photo into a real frame. In the prompt formula it is a separate item and critical.

02.29. Every segment has at least one line about light: source, direction, temperature, what is in shadow. Backlight from depth gives silhouettes and halos, side light sculpts the face, underlight gives anxiety. Haze (powder, dust, smoke) makes light visible, and motivate it by the story.

02.30. "Cinematic" is 90% light pattern, the film stock is seasoning. If a frame is pretty but "not cinema" (even, multi-source high key), fix it with low key and exposure for highlights, not by adding grain.

02.31. Name the source temperature explicitly and duplicate the ban by contrast ("white, neutral, milky, no golden yellow"), otherwise the model drifts into golden hour.

02.32. Describe light by sources and temperature, not by the word "beautiful". Do not write "dramatic lighting" without a source (write "golden hour side light").

02.33. Mixed light from two windows and a lamp gives even pastel. Name the needed sources, explicitly "switch off" the rest ("all other sources are off"), and mark details that can be hidden as "guessed, not visible". "Exposure for highlights" drowns the frame for the sake of a bright window instead of pulling up the shadows.

### Camera movement

02.34. Name the type of camera movement explicitly, otherwise the AI generates random or unwanted movement. An exact description cuts attempts and helps get the result on the first try. Dictionary: 33 movements.

02.35. Movement is storytelling: a slow push-in creates tension, tracking adds dynamics, a static shot focuses on details. Film terms (dolly, crane, tracking) give the look of professional camera work.

02.36. One camera movement per shot; one shot, one action, one movement. Two actions in a shot give flicker. Compound moves ("push in with tilt up", vertigo, orbital descent) are an open question, test before relying on them. Dutch angle: use 5-12 degrees until a test says otherwise.

02.37. Dolly zoom (vertigo) is dosed: once per video. Snap zoom is a comedy or reportage accent.

02.38. Write camera shake into the prompt, not in editing: generated shake looks much better. Realism comes from imperfections (handheld, tilted horizon, unposed poses, micro-movements, smoke, dirty glasses). Exception: a smooth "drone" camera where the video needs it. Resolved by genre: documentary keeps shake and writes it in the prompt; cinematic keeps the previz smooth and adds no shake.

02.39. State documentary feel again in every segment ("handheld, amateur documentary", shake, tilted horizon, focus): written once at the start, the model smooths the picture out. Seedance repeats everything from the previz, down to the shake of a hand, and the shake is not smoothed.

02.40. Camera movement can be filmed instead of described: a phone camera can drive the Blender camera through an app, and the previz then goes into Seedance as a video reference (role: camera only, positions, paths, timing). Details are in stage 05.

02.41. In Kling and Seedance the angle goes first in every beat (shooting point, height, angle, focal length, what is in focus, movement as a path), then what happens. Shake is a parameter: `handheld SETTLE: visible breathing sway...`. Prompt block order depends on the model: photo prompts open with the subject; video prompts open each beat with angle and camera (Kling: file roles first; Omni: camera opens the whole prompt; MiniMax: camera at the end after the beats). Follow the order of the chosen model.

### Model movement and acting

02.42. Set character movement like a technical brief. Without it the network invents movement: artifacts, unnatural plastic motion, change of shot. Video generation is conducting attention and dynamics inside one frame, not animating a picture. Dictionary: 43 key phrases.

02.43. Think like a director or animator: how they walk (confident, graceful, tired), where they look, what the hands do, how movement relates to the surroundings. The character of movement is a direct channel of communication with the viewer.

02.44. A living static frame needs idle movements: shifting weight, adjusting clothes, breathing.

02.45. In every shot with people, write for each character what they do, in what pose, with what emotion and manner of speech. Without this Seedance gives dummies: they stand straight, faces empty, hands hanging.

### Emotions

02.46. Describe emotion with concrete physical signs, not with its name: eyebrows, eyes (opening, gaze, moisture), mouth, muscle tension (jaw, forehead, neck), skin color, pose (head, shoulders, gaze). Dictionary: 30 emotions.

02.47. Emotion goes through body and face, not through a word. The model does not draw the word "scared", it draws what is visible (eyes bulge, eyebrows shoot up, mouth wide open, shoulders up at the ears).

02.48. Combine the emotion description with the character parameters (this keeps consistency). Change emotion with a separate prompt with an expression lock from a smile reference, not by rewriting the identity.

02.49. Editing must not kill emotion: hold a face close-up half a second longer than is comfortable; of two takes choose the one with the living face, even if the background floated.

### Effects, ultra-realism, film look

02.50. Film stock, camera model, effects and the "final style" go at the very end of the prompt: they give the network its visual character. Dictionary: 28 stocks and cameras, 25 effects, final style list.

02.51. A specific film stock is stronger than the word "cinematic": models know the color science of real films. One stock per prompt, do not mix.

02.52. Digital is given away by cleanliness. Film signs: halation, lifted blacks (not a single pure black point), organic grain denser in shadows, soft highlight roll-off, slight softness of the optics instead of digital sharpening.

02.53. Ultra-realism comes from words about amateur phone shooting, natural pose and visible skin texture: `amateur photo, candid pose, photo shot on iPhone, ... visible skin texture, pores, RAW iPhone look`. If that is not enough, add `JPEG Compression` (compression artifacts) and `Slight motion blur` (hand shake).

02.54. In image-to-image, SCENE LOCK first, then style: style without a scene is a new scene. Put the transformation first and strengthen it (STRONG, clearly visible), keep the "preserve" block as a short tail, otherwise the original returns.

02.55. Contradictions kill a prompt: "clean sharp focus" plus "slight softness" makes the model ignore both. Banned in the film template: `clean sharp focus`, `4k ultra sharp`, `HDR`.

02.56. A reference picture beats a text style: glossy references override a text grade. Cures: split the roles ("references only for face and location identity, do NOT take style or grade from them") or degrade the references with a film pass.

02.57. Too-clean references give plastic in video. Before feeding them to Seedance, slightly dirty them (grain, 5-10% soft blur, a film pass); generate in 1080p, not 720p; skin enhancers only after video generation. A skin block is mandatory for people in video.

02.58. Put grain after upscaling (upscalers eat film grain), and it must not fight the picture: if it is seen before the story, there is too much. The grade glues together frames from different models.

02.59. If style conflicts with realism, realism wins (PRIORITY RULE); if light conflicts with identity, identity wins.

02.60. Do not write filler words: "beautiful", "perfect", "flawless" (uncanny valley). "Ultra realistic" alone gets replaced by "photorealistic editorial". For photo models (Nano Banana, GPT Image) do not write `4k, masterpiece, ultra-detailed`: resolution is set by a parameter. For Kling and Seedance replace epithets with a visual fact ("24mm, low angle, warm tungsten key from the left, teal shadows, fine grain"). Do not carry a "cinematic lighting, 4K" tag line into finished prompts.

02.61. A photo prompt is built from blocks in order: subject, location, action, angle and camera, light, effects and styling. When debugging add one block at a time and see where the picture jumped most. Take details from the moodboard, not from your head.

02.62. Materiality decides: not "a table" but "a scratched oak table with a matte varnish".

02.63. Frames for vertical (Reels, motion control): 9:16, medium-full shot (knees to above the head) for dance and chest-up for a talking head, the camera locked-off or with a light natural drift; a fast push into the face gives wide-angle perspective distortion. Emotion in these examples goes through facial expression (eyebrows, eyes, mouth), and fingers break on fast gestures.

### Studio additions (not from the course; taste defaults, the user may change them)

02.64. A "look bible" is one page for the project: frame format, 1-2 focal lengths, direction and temperature of the key light, a three-word palette, a stock-plus-grain line, a list of negatives, names of the reference files. It is the "Film language of the project" block in the output.

02.65. Light temperature ranges: warm up to 3200 K, neutral 3500-4100 K, cold 4100-6500 K, one dominant tint per scene. Single-lens lock: one focal length for up to 30 seconds of one take, do not flip screen direction. Some details of the underlying notes were marked unverified.

02.66. Describe a camera move in five parts: `<move name>. Movement: <what the camera physically does>. Speed: <pace>. Framing: <what stays readable or constant>. End: <the final composition>.`

02.67. Look and tone defaults: by default the camera is clean, and special moves (slow motion up to 3 s, wide 14-24 mm, snap zoom, one dolly zoom per video) are for gags and peaks and each is marked in the storyboard. The look is chosen by genre before the first generation and stays one inside a video (noir and heist on film stock, everyday comedy in phone-camera style). Comedy tone comes from acting and the gag, big readable funny expressions, real light and real colors, not from asking an image model for "comedy" and not from bloodshot eyes. Absurd without effects: nothing comes alive, flies or glows, strange characters live in ordinary life. Frames are not "cute" or glossy: compare each frame with the approved character card and write the rough look as its own prompt paragraph. Pace guide from measuring leader videos: a new place or event every 3-5 s, inside a place wide, detail, reaction for 0.3-0.9 s each, one or two holds of 2.5-5.7 s. (default; the user may change it)

## Workflow

The order of application:

1. Read `script.md`, write the "SCENARIO" block (genre, stakes, motivation, what this is not, place in the story).
2. Choose the genre set (`templates/film-language.md`) and the camera role (02.06).
3. For each scene answer the three questions (02.05) and build the rhythm wide, medium, close, extreme close (example: a lake and a boat, the fisherman pulls a net, he freezes, a ring in the net).
4. For each segment write the six-element shot, taking names from the angle, lens, light and camera movement dictionaries.
5. Check the optical rhythm (no two neighbors on one focal length), three-layer depth, one light for the video.
6. For people: a movement brief (model-movement dictionary) and emotion in physical signs (emotion dictionary), separately for each character in frame.
7. If a scene is one take: a seam substitute every 8-10 s, a camera path, continuity marks.
8. Add at the end of the prompt the stock, effects, skin block and the "final style". Decide which realism is needed (amateur phone look or film stock; the look is chosen by genre, 02.67).
9. Run the checklists below. Show the user and wait for "ok".

## Formulas

Shot:

```
[lens] + [camera position and height] + [camera movement] + [composition by thirds] + [light inside the frame] + [what is out of focus]
```

Photo prompt, 6 blocks:

```
Subject -> Location -> Action -> Angle and camera -> Light -> Effects and styling
```

Lens plus aperture:

```
85mm portrait lens at f/1.4, creamy bokeh
24mm wide-angle at f/8, landscape depth
50mm prime at f/2.8, balanced depth of field
200mm telephoto at f/2.8, compressed perspective with soft background
```

Camera movement in structured form:

```
CAMERA: FOCUS PULL REVEAL. The video starts completely out of focus (bokeh). The lens slowly pulls focus until the subject is razor-sharp. SUBJECT: ... ENV: ...
```

Emotion description structure: eyebrow position; state of the eyes (opening, gaze direction, moisture); mouth shape; muscle tension (jaw, forehead, neck); skin color; overall pose (head, shoulders, gaze).

Ultra-realism words:

```
amateur photo, candid pose, photo shot on iPhone, casual framing, slightly tilted, visible skin texture, pores, RAW iPhone look, clear background
```

Add if not enough: `JPEG Compression`, `Slight motion blur`.

Universal film additions:

```
gentle halation and bloom on highlights, lifted milky blacks,
organic film grain denser in shadows, soft highlight roll-off,
slight chromatic aberration at frame edges, subtle vignette,
slight optical softness, no digital sharpening, not AI-clean
```

Skin block for people in video:

```
realistic skin with visible pores and subtle oil, natural micro-imperfections, film grain, ARRI Alexa 35mm aesthetic, soft subsurface scattering. No 3D, no cartoon, no VFX.
```

Camera move in five parts: see 02.66.

Prompt length has no single number. It depends on the model and its version: read the current limits for the chosen model before writing a long prompt, and keep length to what the scene needs. The storyboard does not set prompt length.

## Check before "ok"

Scene check without words:
- [ ] Where does the viewer enter the scene? (wide)
- [ ] When do they approach the hero? (medium)
- [ ] Where must they feel, not only see? (close)
- [ ] Is there one detail that earns an extreme close-up?

Storyboard checklist:
1. Is there a SCENARIO block with genre, stakes and motivation?
2. Does each segment have all 6 shot elements?
3. Is the most catching angle in the first 1.5 seconds?
4. Does the optics alternate (no two neighboring shots on the same focal length)?
5. Is the arc wide to close (or consciously reversed)?
6. Is light one for the whole video and named in every segment?
7. Do the speeds (normal and slow motion) alternate meaningfully, with slow motion only on gags and beauty?
8. Is sound written, and in slow motion does the sound stretch and mute?
9. If a scene is one take: is there a seam substitute every 8-10 seconds, are movements described as a path, does the frame never widen back?

One-take checklist: 8 points, in full in `templates/film-language.md`.

Film look additions:
- [ ] The prompt is checked for mutually exclusive commands.
- [ ] The light temperature is named.
- [ ] Halation and lifted blacks are present, otherwise it looks digital.
- [ ] Image-to-image has SCENE LOCK and PRIORITY RULE.
- [ ] People in video have a skin block.
- [ ] One emotion per shot is written and emotions differ across shots.
- [ ] Any special move (slow motion, wide angle, snap zoom, dolly zoom) is on a gag or peak and is marked in the storyboard.
- [ ] A symptom, cause, cure table for film look is in `templates/film-language.md` if a frame fails.

The stage closes only on the user's "ok".

## Common mistakes

- Asking "which shot do I film" instead of "what must the viewer feel"; a beautiful shot with nothing to say. Result: an extra shot.
- The whole video in one shot size; eye-level camera everywhere; empty shots. Result: the eye gets used to it, attention leaves.
- Starting with the key detail at once; demanding emotion from the first frame; a close-up with no emotion in the scene.
- A prompt with no shot size: the frame comes out "as it comes".
- No lens named: an average standard result.
- No camera movement named: random or unwanted movement.
- No movement brief for the model: a static picture or chaos, artifacts, change of shot.
- Describing an event instead of a shot; leaving shot elements unnamed.
- Describing the start and end of a camera with no route; widening the frame after a push-in; a long take for the trick; mixing genre sets without reason.
- The words "CUT" or "moving on to" inside a take.
- Shake only in editing instead of the prompt; documentary feel written once at the start.
- Asking for a "photo from another angle" with no description.
- Image-to-image where "preserve" is heavier than "change"; style without SCENE LOCK; "clean sharp focus" next to "slight softness"; glossy references; light temperature not named (it drifts to golden hour).
- Too-clean references and 720p in video: plastic.
- The words "beautiful", "perfect", "flawless"; "ultra realistic" alone; "dramatic lighting" with no source.
- Putting in video slow motion, fisheye, heavy vignette, dust or film burn "just because", and zoom transitions. Resolved by model: for Seedance 2.5 there is no default ban, add slow motion to the negative only when slowing is unwanted. For photoreal prompts on other models (Kling, Veo) keep these out unless the video asks for them. A slowdown at the peak is made in editing as a speed ramp, not in generation.

## Tools

| Tool | Role in this stage |
|---|---|
| Higgsfield `nano_banana_pro` | all angle examples (character first, then angles and locations); a 9-frame grid by angles; up to 14 reference images, optimum up to 6 |
| Higgsfield `gpt_image_2_6` | a shot by 6 blocks: angle and camera, light, effects; a constraints block |
| Higgsfield `seedance_2_5` | executes the language of the frame in video: camera first, acting of each character, stock and skin block; 1080p not 720p for final, 480p for drafts |
| Higgsfield `kling4_0` | the same: angle first in each beat, ACTING; reported to lose camera moves after the third (not verified) |
| The agent with film-language skills (`templates/film-language.md`) | write the storyboard by 6 elements and the film blocks |
| Pinterest and a free board tool | moodboard: angles, light, clothes |
| Blender plus a phone-as-camera app | film the camera movement by hand instead of words (stage 05) |
| An editor with overlay mode | grain and a light-leak overlay as separate files (stage 08) |

Check `models_explore` for current models and `estimate_image_cost` or `estimate_video_cost` for the price in credits before any paid run. This stage is mostly writing. Nothing paid runs without the user's explicit "yes" on the exact list (model, number of jobs, credits from the estimate), with the stage checklist and yes/no per item, and any move that is not the method named as a deviation.
