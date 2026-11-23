# 01 Preproduction

Logline, script by seconds, moodboard as text, director's storyboard. All of it is written before any generation.

Every video follows one route: preproduction, production, postproduction. The first stage weighs about half of the result. The next two do not fix its mistakes, they amplify them. The goal of this stage is a document you can sit down with and generate from, without inventing anything on the fly. Approximate weights: 50% / 25% / 25%.

## Input and output

Input (in the project folder before the stage starts):
- `brief.md` and `idea.md` from stage 00: logline, idea, platform, frame format, duration, credit budget.
- `refs/`: a reference video and links (somebody else's video with a scene like yours; the agent reads angle, light and pace from it).

Output (up to the user's "ok"):
- `script.md`: logline, a "SCENARIO" block (genre, stakes, motivation, what this is not, the place of this video in the story), then text by seconds: what is seen and heard, lines, captions.
- `moodboard.md`: moodboard as text: 3-5 phrases to copy into every prompt (palette, light, optics, texture, location, time of day), a style block, links to the reference sources. The images themselves live in `refs/`.
- `storyboard.md`: the director's storyboard. Per shot: shot size, angle, lens, camera movement, light, who is in frame and what they do, location, sound, duration in whole seconds. Plus an editing note (order, pace, transition type) and a separate list of characters, locations and recurring objects that need reference cards.
- `frames/` (optional): the storyboard as pictures, a 9-frame or 3x3 grid, only so the person can see the story.
- `previz/` (optional, when exact camera is needed): a 3D stand-in in Blender (stage 05).
- For a test, show the story to 5-10 people from the audience as a storyboard or animatic.

The style block from the moodboard is also copied into the prompt file at the end of this stage. That file itself is created in production.

## Principles

### A. Place of the stage and roles

01.01. The four steps go strictly in order: idea, script, moodboard, storyboard. Each step narrows the freedom of the next, so you come to the prompts with a ready decision, not a blank page.

01.02. The model does not think things up, it executes what is written. In production you invent nothing, you execute. If you start composing on the fly in production, preproduction is not finished: go back.

01.03. The script answers "what happens", the storyboard answers "how it is shot". Until there is a second answer, it is too early to generate.

01.04. Preparation is cheaper than generation. In one large story project about 14 days went into the look (locations, characters, clothes, props) against about 4 days of generation. Every detail found saved dozens of generations, because the world was assembled before generating started.

01.05. Roles: the user is the director, the agent is the creator. The user decides, the agent does, checks and shows. At the end of each stage the agent gives a short summary and asks "go on?". Paid generation only after "ok". Stage 01 has no paid generations, except the storyboard as pictures, which also needs a priced "yes".

01.06. Preproduction decides the most: do not rush to generation. A creator who thought she was almost done discovered a mountain of post work. This is a reason to plan the whole route in advance.

01.07. The agent does not see your screen and does not know your workflow. The more context, the more precise the result: references, the idea and script, a piece of the storyboard, how assembly is arranged. The stage documents are this context.

### B. Logline and script

01.08. Logline in one sentence: who, what they want, what stops them. Plus the limits at once (duration, format, number of shots) and a generatability check.

01.09. The frame format is chosen before the first generation. A format change means all generations again. A horizontal 4:3, 25 s, one take is a possible previz format. Vertical 9:16 is for Reels.

01.10. The script contains only what is seen and heard in frame. "Hook in the first 3 seconds, then development and finale. A breakdown by seconds, one scene, one thought." Output: text laid out by the length of the future shots.

01.11. Before generating, know how the video starts and how it ends. Otherwise the plot drifts and the story breaks. If the video is pure atmosphere with no story, the script can be skipped, the moodboard cannot.

01.12. Script structure depends on format, but structure is mandatory. Choose by format, not by taste. Options: three acts (setup, development, resolution); five blocks for Reels (hook 0-3, build-up 3-15, key idea 15-35, conclusion 35-45, call to action 45-60 s); hook (2-3 s), reveal, 3-5 device scenes, finale with a call; for a story cartoon eight beats (hit, bottom, mentor, path, caption, meeting, mirror and "How?", call); for an ad built from a website: hook, 3 benefits, finale with logo and call. Example of a three-act script: `templates/script-and-storyboard.md`.

01.13. The agent writes the script from a master prompt, the idea belongs to the human. Master prompts for the roles Scriptwriter, Storyboarder, Director are in `templates/script-and-storyboard.md`. The agent learns the style from real examples of content, not from a description of the style.

01.14. Do not invent extra scenes: work strictly by the script. One idea per video, one scene one thought.

01.15. The "SCENARIO" block goes first in any story prompt. It holds genre, stakes, motivation of the characters, what this is not, the place of the video in the story. The video model must first understand the story, then execute frames. Without context the model draws each frame literally and unconnected.

01.16. Meaning first, then the frame. A beginner asks "which shot do I film now?". A director asks "what must the viewer understand and feel at this moment and why now?". If a shot has nothing to say, it is extra, however beautiful.

01.17. Before each scene answer three questions: what changes in the hero, where is the peak of tension, at what moment must the viewer be closest.

01.18. Expand a one-line scene into six layers: subject and action; environment; light (the most important layer, where it comes from); atmosphere and texture; camera; the mood in 2-3 words. Missing layers give flat, generic results. Template: `templates/script-and-storyboard.md`.

01.19. Expand with specifics but do not overload. More specific is better. Light logic is consistent. Atmosphere implies sound. One strong atmosphere beats five weak details, and ten competing elements confuse the model.

01.20. Emotion is built, it cannot be demanded from the first frame. The viewer approaches the hero gradually, which is why a ring at the end hits hard. Start with the ring and it means nothing. Golden rule: first show where we are, then what happens, only then what the hero feels. Shot ladder: wide, then medium, then close-up, then extreme close-up at the peak, with a quieter start. Write one emotion per shot next to the storyboard, readable and different across shots (an arc).

01.21. The choice of device must follow psychological reality. In one project, shooting the whole second part in first person broke the logic: a hero who wakes up in someone else's body first goes to the mirror. That part was redone three times.

01.22. Plan ahead for what models do badly: reflections and mirrors (a transition through a car reflection "did not work"), pure POV, optically complex scenes. Better to leave such scenes out or simplify them at script stage.

01.23. Contrast between heroes in a 60-90 s vertical must be exaggerated. The first frames show who is who at once.

01.24. Short entry: instead of a wide shot of a school, go straight into the corridor. A wide establishing shot is too long for social media. Wide architectural shots also fit vertical 9:16 badly.

01.25. Do not tell everything in the first seconds; show the emotions of people, not landscapes; do not replace a shot with a caption. (Detailed idea rules are in stage 00.) Hook conflict is resolved as in 00.36: do not reveal the turn early. The first frame may pose a riddle, never the resolution.

01.26. For a direct test of the script, show an animatic or storyboard to 5-10 people from the audience: "retell what happened" and "where did you laugh".

### C. Moodboard

01.27. A moodboard is mandatory even without a script. It is the most important step unless you are a professional with 10 years of experience. Every moodboard trains your eye. It is not scrolling a feed, it is targeted search.

01.28. A moodboard has two parts: (1) a reference video (effects, editing dynamics, sound); (2) a set of pictures so your video differs from the reference: frames, location, angles, model, light, clothes.

01.29. The core of a moodboard is a set of interesting angles. Eye-level camera in all shots makes a video boring.

01.30. How to collect: the script shows which frames are needed (wide, close, details). Search Pinterest, keep themed boards (angles, characters, ads), assemble in a free board tool with notes like "angle from here, light from here, clothes from here", make a preliminary storyboard by episodes, on average 3 frames per episode. Film frames can be found in a film-frame library or on Pinterest.

01.31. Two layers (resolved). The pictures stay in `refs/` for the human. The text goes into prompts: take references from one source, not twenty different ones, and turn them into text, 3-5 phrases copied into every prompt (palette, light, optics, texture, location, time of day) in `moodboard.md`. The text does not cancel the collection.

01.32. Details come from the moodboard, not from your head. You do not invent, you transfer from real samples. This is prompt engineering.

01.33. References in 4K. Video takes its quality from references, so all references must be 4K. Set high resolution explicitly wherever the tool defaults to low.

01.34. Realism rests on the style setting of the references, not on the prompt. A moodboard of amateur flash photos and a personal style profile does the work. The look is chosen by genre before the first generation and written into the style passport (`moodboard.md`): noir and heist on film stock, everyday comedy in phone-camera style. Inside one video the look is one. (default; the user may change it)

01.35. Perfectly symmetrical faces give away the network. For a realistic character use a reference card (a sheet from different sides) and a slight asymmetry of the face in the prompt.

01.36. If you plan to feed moodboard images into generation as a reference, remember the model may take them directly, down to somebody else's face. Describing the picture in words (through the agent) and generating from the description is safer.

01.37. A reference is structure, not someone else's brand. Take structure, pace, devices. Do not carry the original's logos, texts, characters and music into work. If the reference is lively but scenes came out static, regenerate only those.

01.38. If the client names a style reference, study it deeply. In one project the named reference was a mystery TV series and a vibe of two heroines (look and clothes). The creator watched three seasons and pulled out the era, the dark mood, the school year, the red thread.

01.39. Choose style through a specific film stock and a light pattern, not the word "cinematic". "Cinematic is 90% light pattern, film stock is seasoning." A specific stock beats the word "cinematic". One stock per prompt. If it does not look filmic with the right grain, fix it with light, not by adding grain. Templates: `templates/film-language.md`.

01.40. Color must not jump between shots (in one product video a dress changed color). Write one palette into the moodboard in advance: car, clothes and model in the same tones. Light is one for the whole video and is named in every segment.

01.41. The moodboard leads to the style block. The style block is written into the prompt file at the end of this stage.

### D. Director's storyboard

01.42. For each shot give size, angle, camera movement and duration. A director's storyboard per second: what is in frame, where the camera is, where slow motion is, when who speaks. Per shot: angle, lens, camera movement, who is in frame and what they do, location, sound.

01.43. Describe a shot, not an event. "They fight in a shop" is an event. A shot is: [lens] + [camera position and height] + [camera movement] + [composition by thirds] + [light inside the frame] + [what is out of focus]. If even one is not named, the model chooses itself and it is almost always boring (eye level, 50 mm, center, flat light). An example of the translation is in `templates/film-language.md`.

01.44. Shot size is language. Wide answers "where are we, what world is this". Medium answers "who and what are they doing". Close-up answers "what do they feel". Extreme close-up answers "what to look at right now". The closer the shot, the closer the viewer is to the hero and the stronger the emotion.

01.45. Scene rhythm: wide, medium, close, extreme close. The main mistake is the whole video in one shot size: the eye gets used to it and attention leaves. A good video is built like music: louder here, quieter there, a pause and an accent. Course example: a fisherman on a lake, the ring in the net as an extreme close-up.

01.46. Alternate shots in a circle: wide, medium, close, details, and again. Every shot must carry information. Viewers do not watch empty shots. Three face close-ups in three seconds is too much. An out-of-focus foreground immerses, details and sound give the feeling of presence.

01.47. Arc from general to particular: first a wide shot and the location, then details. Or a consciously reversed arc.

01.48. Optics alternate. Wide angle 14-24 mm for chaos, scale, chase; long focus 85-135 mm to isolate a gag or emotion. Chaos with a wide lens, the punchline with a telephoto. Contrast of focal lengths between neighbors gives a feeling of expensive editing. No two neighboring shots on the same focal length.

01.49. Depth in three layers: an out-of-focus foreground, a sharp subject, background depth in haze 1-1.5 stops darker than the foreground. Recheck any shot with no foreground.

01.50. The camera is a character: observer, voyeur, interlocutor, pursuer, judge. The choice of role sets the movement and the distance to the hero.

01.51. Shot size is written in the prompt in English and at the start: `extreme wide establishing shot`, `medium shot`, `close-up`, `extreme close-up`. Then the frame forms at the needed size, not "as it comes". Reference lists of angles, lenses, light and camera movement are in stage 02.

01.52. The hook in the storyboard. The most catching angle of the video goes into the first second and a half, and the first 3 seconds must catch visually without sound. Resolved timing: the idea is clear from the first frame, details unfold by second 3. Prepare 2-3 variants of the first seconds for testing.

01.53. Bold angles instead of same-type straight shots. In sport they use bold angles. Same-type straight shots, especially with a look into the camera, cheapen the video. Add movement, sweat, different people in the same clothes.

01.54. Eye-to-eye scene: if you show the hero's eye in close-up, show the animal's eye as close. Then it is clear they saw each other, and drama begins.

01.55. Where the character looks is written in the storyboard and the prompt. Looking at the camera only when the character speaks to the viewer, or as a single look in the finale. For expensive products, a look from above with a challenge. Continuity: where the hero looks, where they move from and to.

01.56. Emotions are not only in the face: nervous fingers in close-up. Describe emotion with concrete physical facial signs, not with its name.

01.57. Imperfections for realism: handheld, tilted horizon, unposed poses, micro-movements, smoke, dirty glasses. Write camera shake into the prompt: generated shake looks much better than shake added in editing. Resolved by genre: documentary keeps the shake and writes it in the prompt; cinematic previz is smooth, no shake added. Seedance repeats any shake of the previz. Exception: a smooth camera "like a drone" where the video needs it. Default camera is clean. Special moves (slow motion up to 3 s, wide 14-24 mm, snap zoom, one dolly zoom per video) only on gags and peaks, and each one is marked in the storyboard. (default; the user may change it)

01.58. Speed is set deliberately: slow motion only on gags and beauty, not longer than 3 seconds in a row. Speed ramp: normal, slow at the peak, sharp return, with sound that stretches and mutes. Sound follows speed, otherwise the effect looks like a lag. Slowdown at the peak is made in editing as a speed ramp, not in generation.

01.59. Sound is written in the storyboard. Minimum: where lines are (by seconds), music, tempo type. Know the music already at the rhythm stage, because cuts are built to it. Your text stands in the seconds where you say it.

01.60. Pace changes by act: act 1 long calm shots, the viewer enters the world; act 2 shorter cuts, pace rises; act 3 transformation and a freeze before the leap.

01.61. Plan cuts and transitions already in the storyboard. Know classic cuts at least by name: cut on action, J-cut, L-cut, match cut, smash cut. The shape for a match cut can be planted in the prompt of the next shot. Hidden cuts: pass behind an object, whip pan, dip to color, pass through a dark zone. When assembling a long video from several generations, plan the seam in advance and put it into a motion smear. Never default to hard cuts.

01.62. A continuous shot (oner) is not for the trick. Check question: "what does this scene lose if cut?" If "nothing", a oner is not needed. Rules for AI: a path, not points; the frame only narrows on a push-in; continuity marks instead of "CUT"; a seam substitute (change of environment, reveal, change of scale, entry and exit of characters, change of speed) at least every 8-10 seconds; a one-minute take is 6-8 events; character choreography is written before the camera movement. Full text: `templates/film-language.md`.

01.63. Genre sets the decisions. One genre is one coherent set of decisions. Do not mix sets inside a video without reason (thriller, horror, comedy, drama, documentary, action, ad, music video). For product ads: product as a character, hero shot, macro detail, a finale of 1.5-2 seconds.

01.64. Light is named in each segment: source, direction, temperature, what is in shadow. For low key, name the temperature of the source explicitly, otherwise the model drifts into golden hour.

01.65. List characters, locations and recurring objects separately. Anyone who appears more than once needs a reference card. An object or place for one episode needs one picture. Each hero gets their own picture in each segment of the video prompt, so faces do not get mixed.

01.66. A storyboard as pictures does not replace the text. It exists so the user sees the story. Its frames are not fed to the video model (Seedance, Kling). One exception: with MiniMax H3, an approved 3x3 grid may go in as a reference and `start_image` may be a storyboard frame. Using a first frame in image-to-video is a separate allowed device.

01.67. Picture first because video costs more. A 3x3 storyboard before generation: any change to a picture is cheap. No video is generated until the user's "ok" on the storyboard. Collect corrections into one list. Structure of the six-part prompt and the grid request are in `templates/script-and-storyboard.md`. Check the grid price with `estimate_image_cost` before running it.

01.68. Time in the storyboard. For Seedance 2.5, whole seconds only, shortest block 1 second: it does not understand fractions. Kling and MiniMax accept fractions. Write the storyboard in the units of the chosen model. Check the storyboard on three points: (1) whole seconds; (2) it is visible where slow motion is, where normal speed is and when the transition happens; (3) your text stands in the seconds where you say it.

01.69. Three ways to storyboard as pictures: (1) a quick 9-frame grid in one prompt from a reference (when there is no complex plot and you need angles of one episode); (2) manual: clothes layout, reference card, setup frame, frames, the slowest but most controlled; (3) a quick "video in 10 minutes" workflow. Main rule: with 30-40 frames feed only the setup frame and the reference card into each storyboard frame, not other people's references. Otherwise the network drags extra from them: color, effects, face features, the face drifts, color jumps. With few frames, add location and model photos where the location is really in frame. The setup frame is a frame with the whole atmosphere, not the first frame of the video.

01.70. A 9-frame grid from references: upload a location frame and a model photo, ask for a "director's storyboard of 9 frames"; 4 generations of 9; shoot a missing frame with a separate prompt. If the grid came out cartoonish, ask to keep the style. Prompts: `templates/script-and-storyboard.md`.

01.71. A location from another angle cannot be requested with the words "make it from another angle". Everything not written the network invents, and the result is mediocre. Describe the location yourself (sofa, wardrobe, two doors, TV), in prompts of 1000-1500 characters. A fallback is a 3D world from one photo (lower quality).

01.72. Previz in Blender builds the video by seconds before generation and is corrected in words for free. Seedance takes camera, paths and speed from the previz, pictures set the look, the prompt sets acting and details. You see the video before generation; money goes to one or two generations instead of twenty. One creator estimated that blocking in Blender would have saved about 35% of the generation budget on a large project (her estimate). Details in stage 05.

01.73. References are needed for everything the network must draw exactly: a hall, a facade, a car, an interior, a face, a driver. The list of such things is made in the storyboard.

01.74. Previz people without extra detail. Seedance repeats previz motion fully. Add a hand only where a gesture matters for the story. Decided in the storyboard. Previz default: simple blocks with no hands (default; the user may change it).

01.75. Do not forget editing. At the end of the storyboard put a short editing note (order, pace, transition type), for example "Cut scene 1, 2, 3 on beat, total about 12 s reel". Default for Reels is 3-5 scenes.

01.76. Editing to the beat: shift cuts slightly to the music and the video looks livelier. Plan beat cuts if the music is known.

01.77. Better from several variants than from one generation. A 15-second video generated whole from one prompt and one picture gives doubling and floating graphics. Assemble 10, 15 or 20 seconds from the best frames of several generations. In the storyboard this means the video is cut in advance into pieces at natural seams (scene change, flash, blur), and each piece repeats the palette and the main object.

01.78. A beginner with no ideas: repeat a ready ad. Find a video, build a moodboard, break the idea into a storyboard (which frames from which angles), then generate with the agent.

01.79. The economics of generations goes into the storyboard. Up to 95% of generations are waste, and one setup frame costs dozens of generations. In one story project about 22 s of generation went into each 1 s of finished video. Dynamic scenes with fast cuts and shot changes can behave differently at draft and final resolution. Resolved: static and simple scenes, a cheap 4-5 s test or draft first, then the same shot is finished; dynamic scenes (chase, fight, crowd) go at target resolution at once. Budget for both cases.

01.80. For a client: with a very small client budget, warn honestly that it buys a couple of generations. The number of revisions is in the contract. Agree the storyboard with the client before generation, so changing it is cheap.

01.81. The model reads video at roughly 5 frames per second and may miss text on a face. Put captions and inscriptions not on the face.

01.82. Eyes and taste stay with the human; the agent does not replace taste. The director's storyboard is never handed over without being shown to the user.

## Workflow

1. Read `brief.md` and `idea.md`. If the frame format is not set, ask before any generation.
2. Write the logline, the limits and the generatability check.
3. Write the script by seconds: the "SCENARIO" block (genre, stakes, motivation, what this is not, place in the story) plus what is seen and heard, the hook in the first 3 seconds, development, finale. If it starts from one line, expand it into six layers. Choose structure by format (01.12).
4. Build the moodboard: reference video plus pictures; Pinterest, boards, a free board tool; about 3 frames per episode; 4K references. Then turn it into 3-5 phrases and a style block. Pick the look by genre (01.34).
5. Write the director's storyboard: per segment the six shot elements, rhythm of shot sizes, optics, light, sound, duration in the units of the chosen model; one emotion per shot; for a oner, a seam substitute every 8-10 s; mark every special move.
6. List characters, locations and recurring objects that need reference cards.
7. If the user needs to see the story, make the picture storyboard (9-frame grid or 3x3). This is a paid step: run `estimate_image_cost`, send the price message with the checklist, wait for "yes". Optionally a Blender previz (stage 05).
8. Run the "Check before ok" list, show the user. Corrections go as one list. The user's "ok" closes the stage.

After "ok", the next stages are reference cards, setup frame, video prompt, generation and upscale.

## Formulas

Shot: `[lens] + [camera position and height] + [camera movement] + [composition by thirds] + [light inside the frame] + [what is out of focus]`.

Shot size to viewer question:

| Shot size | Question it answers |
|---|---|
| Wide / establishing | Where are we? What world is this? What space? |
| Medium | Who is this? What are they doing? |
| Close-up | What do they feel? |
| Extreme close-up | What to look at right now? |

Camera as a character: Observer (stands still, medium shots); Voyeur (wide shot and slow zoom); Interlocutor (close-ups at eye level); Pursuer (moves behind the hero, handheld); Judge (extreme close accents on details).

Simple grid prompt:

```
make a storyboard of 9 frames of this story, using angles from above, from below, from the side
```

Request to the agent, what to include: 1. all references; 2. the idea and script; 3. a piece of the storyboard (what is in frame, lens, light, camera movement); 4. how my workflow is arranged.

Storyboarder structure per shot: timing, composition (subject, position in frame, background, details), camera movement, motion in frame, visual effect (if needed), atmosphere. Output as a table `| Timing | Composition | Camera | Action | Effect | Atmosphere |` with a director's comment.

Long forms (three-act script example, six-layer scene expander, storyboard-by-seconds request and its 3-point check, six-part 3x3 prompt, 9-frame grid prompts, master prompts for Scriptwriter, Storyboarder, Director) are in `templates/script-and-storyboard.md`. Style block templates and film stocks are in `templates/film-language.md`.

## Check before "ok"

Script and logline:
- [ ] The logline is one sentence: who, what they want, what stops them.
- [ ] The script is clear: it is known how the video starts and how it ends.
- [ ] There is a "SCENARIO" block: genre, stakes, motivation, what this is not, place in the story.
- [ ] The script has only what is seen and heard; the hook is in the first 3 seconds.
- [ ] The 4 director's questions are answered: where does the viewer enter the scene (wide), when do they approach the hero (medium), where must they feel (close), is there a detail for the extreme close-up.

Moodboard:
- [ ] A moodboard is built: a reference video and pictures with angles, light, clothes.
- [ ] References are from one source, in 4K, turned into 3-5 phrases.
- [ ] Palette, light, optics, texture, location, time of day are named; color does not jump.

Storyboard:
- [ ] Wide, medium, close shots and details alternate; no three identical shots in a row.
- [ ] Each segment has all six shot elements.
- [ ] The most catching angle is in the first second and a half.
- [ ] Optics alternate; no two neighboring shots on the same focal length.
- [ ] The arc goes from general to close, or a consciously reversed arc.
- [ ] Light is one for the whole video and is named in every segment.
- [ ] Speeds (normal and slow motion) alternate meaningfully; slow motion only on gags and beauty.
- [ ] Sound is written; in slow motion the sound stretches and mutes.
- [ ] If a scene is one take: a seam substitute every 8-10 seconds, movements as a path, the frame does not widen (the 8-point oner check is in `templates/film-language.md`).
- [ ] Time is in the units of the chosen model (whole seconds for Seedance); slow motion and transitions are visible; lines stand in their seconds.
- [ ] Imperfections are provided in the prompts (handheld, tilted horizon, micro-movements), in line with the genre.
- [ ] It is stated where the character looks; no look into the camera everywhere.
- [ ] One emotion per shot is written, and emotions differ across shots.
- [ ] Characters, locations and recurring objects for reference cards are listed.
- [ ] If a picture storyboard was made: only the setup frame and the reference card (or, for few frames, location and model photos) were fed in; pictures are reduced before video generation.
- [ ] For a 3x3 ad storyboard: the grid is approved before video generation.

General:
- [ ] The user was shown the storyboard, corrections were collected in one list, "ok" received.
- [ ] Time and credits are set aside for search and redo.
- [ ] What is dangerous for the model (mirrors, pure POV, complex reflections) is identified and the scenes are simplified.

The stage closes only on the user's "ok".
- [ ] Storyboard has a shot-size column and neighbouring shots cut by size (02.68); wide and extreme wide shots exist (02.69).
- [ ] Every shot has its light with the shooting side (`backlight`, shadow side) and a lens with aperture up to 135 mm (02.70, 02.71).
- [ ] Palette of 1-3 main colours with one accent that leads to the product; three planes, no clutter, a telling object (02.72, 02.73).
- [ ] Three anchor points in seconds: question around second 5, turn in the middle, climax with the product 5 s before the end (02.76).
- [ ] Camera and subject move in every shot; scenes of 1-3 s (02.75).

## Common mistakes

- Inventing on the fly during generation; hoping production and post will fix preproduction (they only amplify it); a video as a "set of beautiful generations" instead of an excerpt from a film.
- Generating with no script and no idea of start and end; eye-level camera in all shots; empty shots; feeding moodboard references into every storyboard frame; changing a model's clothes from somebody else's photo without cropping the head; "make a photo from another angle" with no description.
- The whole video in one shot size; a beautiful shot with nothing to say; a close-up with no emotion; starting from the key detail; demanding emotion from the first frame; a prompt with no shot size.
- Same-type shots; frames out of style; low-resolution references; perfectly symmetrical faces; badly cropped frames in cuts; a caption instead of a shot.
- One look into the camera in all shots; a video from a single generation; a product not tied to the story; cartoonish look; color jumping between shots.
- Describing an event instead of a shot; leaving shot elements unnamed; the words "CUT" and "moving on to" inside a take; describing the start and end of a camera without a route; widening the frame after a push-in; a long take for the trick; mixing genre sets without reason.
- In requests to the agent for scenes: numbering characters in the request; loading references in a different order than in the prompt; forgetting "no music" (it affects editing).
- Fractional seconds in a storyboard for a model that does not accept them; a human with hands in previz; voice-over in generation together with 3D.
- Failures seen in a real project: the opening scene was generated endlessly because the heroine's look did not carry emotion; reflections and pure POV; a wide shot of a school; robot voice instead of live voices; search was not put into the quote.
- Jumping into the storyboard before the script and the moodboard; not showing the storyboard to the client before generation. Generating video before "ok" on the storyboard is a mistake.

## Tools

| Tool | Role in this stage |
|---|---|
| The agent (Claude Code or similar) | script, storyboard, scene expansion, style block |
| Pinterest | collect the moodboard on themed boards (free) |
| A free board tool | lay out references, mark "angle, light, clothes from here" |
| A film-frame library | film frames as references |
| Higgsfield `nano_banana_pro` (up to 14 reference images, up to 5 human faces) | the 9-frame grid and storyboard frames |
| Higgsfield `gpt_image_2_6` | the 3x3 storyboard grid at 2K |
| Blender with the `blender-previz` skill (`.claude/skills/blender-previz/SKILL.md`) | optional previz by seconds, corrected in words for free |
| A site reader of your choice | optional: read the client's site (colors, fonts, screenshots) for a launch video |
| A voice dictation app | optional: dictate scripts, prompts, notes |

Only the picture storyboard is generated in this stage. Check `models_explore` for current models and run `estimate_image_cost` before the run. Run nothing without the user's explicit "yes" on the exact list (model, number of jobs, credits from the estimate). The price message includes the stage checklist with yes/no per item and names any move that is not the method as a deviation.

Tools change, the roles stay: find a reference, build a moodboard, lay a scene out by seconds, show the story in pictures.
