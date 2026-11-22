# 08 Post: edit, sound, color, motion ads, delivery

Post-production is about a quarter of the result. It adds emotion, not meaning. Meaning is set before the first generation (idea, script, storyboard), so this stage receives a script and generated clips and does not repair them. Here the user (with the agent) assembles the edit, finishes sound and color, upscales, adds subtitles, builds motion ads, and prepares the file and copies for publishing. Voice and music themselves come from stage 07.

Principle numbers are kept stable because other files cite them. Unused numbers: 08.63, 08.66, 08.85, 08.88, 08.97.

## Input and output

Input (in the project before the stage):
- `storyboard.md` and `script.md`: number of scenes, seconds, where on-screen text sits (text placement is planned already at generation).
- `video/`: raw generations per scene and take. Only the live part of each is used.
- `audio/`: voice, music, effects from stage 07. If there is no voice yet, make it first.
- `prompts.md`, `brief.md`: frame format (9:16 or 16:9), length, platform.
- For client work: a brand file and brand folder (08.67 to 08.78).

Output:
- `edit/`: an edit plan (before render), a rough cut without sound and color, versions `_v1`, `_v2`, the final `mp4` (H.264, yuv420p, faststart, audio at -14 LUFS), a cover `jpg`.
- `publish.md`: the post text (1 to 3 honest sentences), platform, format.
- When publishing copies: a copies folder with a parameters file and a contact sheet of frames (08.90 to 08.96).

## Principles

### A. What post does and in which order

08.1 Editing and sound strengthen what is already in the frames. If a frame is missing or does not join its neighbor, editing will not save it. Each stage only enlarges the errors of the previous one.

08.2 The three pillars go strictly in order: edit, sound, color. Coloring and sounding shots that later drop out of the edit is wasted work.

08.3 Start with a rough cut with no sound and no color. Go on only when the story reads. Test: if the story reads without sound and color, the cut is ready.

08.4 Editing is three decisions at every cut: which piece to take, in what order, how long to hold. The same material in a different order gives a different result.

08.5 Take only the live part of each generation. First and last frames are often bad: the model speeds up at the start and falls apart at the end. Cut to the best seconds. Of two takes, take the one with stronger emotion, even if the background drifted.

08.6 Bring all clips to one format at once: frame rate, resolution, aspect ratio. Otherwise jumps appear in the edit.

08.7 An error the previous step did not catch is the most expensive to fix in the edit. Before assembly, go through the checklist of the earlier stages.

### B. Structure: length, change of visuals, rhythm

08.8 Optimal short video length: 30 to 45 seconds holds attention best. Other lengths depend on the goal (B9 in `docs/defaults.md`: 30 to 60 seconds by default; ads about 15; portfolio pieces 15 to 20).

08.9 The main principle of short editing is dynamics: every 2 to 3 seconds the shot, angle or visual accent changes. Editing is a tool of retention. A study of leaders shows a new place every 3 to 5 seconds with shots of 1.5 to 2.5 seconds; both fit (A44).

08.10 Three kinds of hooks: visual, text, edit. Visual: motion in frame, zoom, a sharp change of angle or size, an unexpected detail; a visual shift every 2 to 3 s. Text: pain, provocation, intrigue, short, from the first seconds. Edit: a cut at the most interesting moment, contrast between shots, a cut on motion.

08.11 Give the "whole juice" in the first second. The viewer decides in half a second to a second whether to watch. A long first shot reads as a frozen phone. The hook is visible from frame 0 and the idea reads from the first frame without sound; details open by 3 seconds (A1).

08.12 Do not pour everything out in the first seconds. In a good story the hero struggles and a turn comes at the end; if everything is told at once, there is nothing to worry about. The opening frame may show an outcome as a riddle, not as the resolution (B18, B19 in `docs/defaults.md`).

08.13 Alternate shot size: wide, medium, close, extreme close. Wide answers "Where are we?", medium "Who is this, what is he doing?", close "What does he feel?", extreme close "What to look at right now?". Rule of thumb: first where we are, then what happens, then what the hero feels.

08.14 A whole video in one shot is the main directing mistake: the eye stops reacting after a few seconds. Three close-ups of a face in three seconds is also too much.

08.15 Optical rhythm gives the feel of an expensive edit: chaos with a wide lens, punchline with a long lens. Contrast of focal lengths between neighbor shots. Wide 14 to 24 mm for chaos and scale, long 85 to 135 mm to isolate emotion. Special optics only on gags and peaks, each marked in the storyboard (B17).

08.16 If a scene is one continuous shot, replace cuts with events: at least one every 8 to 10 seconds. Five substitutes for a cut: change of environment, a reveal, change of scale, characters entering or leaving, change of speed.

08.17 Tempo changes by act. Act 1: long calm shots, the viewer enters the world. Act 2: shorter cuts, rising tempo. Act 3: transformation and a freeze before the leap.

08.18 Know the music at the rhythm step: cuts are built on it. In a beat edit, cuts land on beats; the main trick lands on the drop.

08.19 Hold a close-up of emotion half a second longer than is comfortable. Cutting earlier kills the emotion.

08.20 Plan where text sits in the frame already at generation. Use a frame grid: key attention zones on the upper and lower lines. For a video without a talking face and subtitles, put the face on the upper line or between the upper and center lines so space remains for text above.

08.21 Choose shots for the story, not for beauty. If a shot has nothing to say, it is extra, however pretty.

08.22 A caption does not replace a shot. A caption is for what you could not show. If the idea does not read from the screen, shots are missing.

08.23 Same-type shots drag the video. Alternate wide, closer, close emotion. Out-of-focus foreground and detail shots with sound give the feel of being there.

08.24 Know the names of classic cuts so they can be planned at the storyboard. A match cut can be built into the next frame's prompt.

### C. Cuts and transitions

08.25 Cut on action and hidden cuts hide the seam. For AI video: a fast whip pan with blur at the end of one generation and at the start of the next, with the cut placed in the blur. Other hidden cuts: camera passing behind an object, whip pan, dip to a color, passing through a dark zone. If the generation has no blur, add one in the editor.

08.26 Sound cuts: J-cut (sound of the next scene before its picture) and L-cut (sound of the previous scene continues over the new picture). Match cut links shots by form. Smash cut jumps from silence to chaos.

08.27 Between clips you need sound as well as a cut. Do not forget sound design between cuts.

08.28 Do not cross-fade two busy scenes into each other. Either "old one gone, new one arrived", or through a dark frame, or a wipe. On a cut, one flash frame (brand color or cream at about 85 percent).

08.29 Cut a long scene into segments at natural seams (scene change, flash, blur), not in the middle of a slowdown or morph. Repeat the palette and main object in each segment. Join them in the edit. For clips over 15 seconds, build in segments.

08.30 Kuleshov effect: meaning is born at the joint of two shots. A neutral shot of a character is filled with the emotion of the neighbor.

08.31 Murch's rule of six: a perfect cut answers yes to all six points; if impossible, sacrifice from the bottom up. Weights: emotion 51 percent, story 23, rhythm 10, eye trace 7, screen plane 5, space 4. AI generations break the lower points (axis shifted, background drifted); that is fine if the upper ones work. Table under Formulas.

### D. Sound (summary; the source of sound is stage 07)

08.32 Background music is always needed, even with a voice. Instrumental versions of popular styles give a familiar feeling.

08.33 Sound design means sound hooks: whoosh on zoom or move, clicks on a change of shot or an appearing element, hits on accents, ambience, a sharp stop for tension. Save all effects for fast editing.

08.34 Sound goes in layers: separation, dialogue, foley, effects, ambience, music, boosters. Dialogue first. Sound the meaningful, not everything (07.69 to 07.72).

08.35 Synchresis: when sound and picture happen together the brain fuses them into one event. In a speed ramp the sound must follow speed; flat sound looks like lag.

08.36 Separate the voice from the generation's sound. Do not put voice into a generation together with a 3D previz. Do not bake music into generations. When replacing a voice, set the model's original voice to zero, do not just lower it.

08.37 Music and effects lie on separate tracks. Voice is always louder than music. Music ducks under hits. Final -14 LUFS (A41). Separate tracks let you swap a track in minutes.

08.38 The agent does not hear sound. It checks loudness (ebur128) and the spectrogram and writes honestly "not checked by ear". The beat phase on a dense mix is chosen by a human with A/B clicks.

08.39 Do not count a voice cleaning result as checked until the file itself is checked. A cleaning service may add a jingle or a signature, and the voice may shift. Find the shift by correlation with the original, cut, check shift 0 at several points, check the first and last phrase and no jingle in the first 20 seconds (A47).

08.40 If there is generated sound, check the finished file: duration, loudness, transcript of the start and end.

### E. Color, grain, upscale, lens effect

08.41 Grading glues shots from different models into one film. All shots must look shot by one camera.

08.42 A green-screen-style tint layer and grain go on top as separate video files in Overlay mode. Tint: darken about 20 to 25 percent (about 15 if the picture is dark). Grain: tune opacity. Clean generation looks plastic; grain brings back film feel. If grain is visible before the story, it is too much.

08.43 Color sets emotion: blue is drama, depth, calm; red is tension, energy, accent; green is freshness, nature or a light cinematic effect. Use ready filters at intensity 40 to 50, HSL for precise tuning, light grain, contrast, brightness and shadows. Do not overload.

08.44 Upscale at the very end, after the frame is accepted. It makes no sense to improve a frame you will reject. Default upscale settings change almost nothing; correct parameters transform the frame.

08.45 First upscale, then effects. Grain goes after upscale because upscalers eat film grain. Post order for Seedance clips: upscale each accepted clip, then grain and halation, then final grade. Upscale clips one by one before the edit; do not upscale the assembled video a second time (A45).

08.46 Generate at the target resolution when the scene is dynamic (chase, fight, crowd), because physics differs between 480p and 1080p. Static or simple scenes: cheap 480p draft first, then finish the same take, not a new generation (A5, C6). Part of the "cartoon" look is upsampling of soft low-resolution output. Animating a photo without upscale loses 15 to 20 percent of quality.

08.47 Detail and skin enhancers only after video generation (for final styles and posters), not before. Too clean references make plastic in the video model. For a soft picture, raise detail after the video.

08.48 "Lens effect on accents" appears in one guide line without parameters. Do not invent what it means. Related tricks with parameters: keyframed zoom in the editor (08.58) and halation and bloom on bright sources.

### F. Subtitles and text on screen

08.49 Subtitles for speech are required: many people watch without sound. Text is large, contrasting and readable without sound.

08.50 Make subtitles automatically, then fix by hand: font, line breaks, accents. Use two fonts: an accent bold and a simple main one. Highlight key words by color, size or font.

08.51 A strong hook at the start is a separate large text in the first 1 to 3 seconds, not the subtitles. If the user chose a title card, it is one short line for 0.5 to 1 second (B2). No other decorative text unless asked.

08.52 In code-based editing: subtitles word by word, 2 to 4 words on screen, fonts and colors from the studio or brand file.

08.53 Keep text inside the platform safe zone. 9:16 (1080 by 1920): the interface covers about the bottom 22 percent (below about 1480 px), a right column about 140 px (from 1000 to 1700 px in height) and the top about 200 px. Keep text roughly 64 to 940 px wide and 230 to 1480 px high; only imagery at the bottom. 16:9: text above the bottom 15 percent. For vertical MiniMax H3 ads: keep the top 12 percent and bottom 15 percent free of text.

08.54 For a generated video with captions: give the list of captions word for word and the line "nothing else is written in the frame". That stops text from drifting. Exact numbers, charts and small text are safer made in code than generated.

08.55 Switch off extra subtitles and music that a model adds on its own: `no titles, no subtitles, no text, no music`. State the language of the character always. Kling 4.0: `No subtitles, no on-screen text` in positive constraints.

08.56 The agent looks at video at about 5 frames per second and may miss text on a face. Put this into the brief and give edits. A cut left a couple of frames short shows at once, so review the cuts.

### G. Editing with an agent: environment and process

08.57 A chat only advises how to edit. A coding agent with file and terminal access edits for real. Plain chat modes without file access do not fit editing.

08.58 Zoom is two keyframes: the first at the start of the segment, the second after moving the playhead with another scale or position. Do it gently, not too sharp. Position can shift in any direction.

08.59 Write the style (fonts, colors, formats) once in the studio rules file. The agent reads it at the start of each session.

08.60 One video, one folder, one agent session. Keep order in folders from the start. A new big step (brand, video) in a new session.

08.61 Plan first, then render after "ok". Plan: what is cut out, where which subtitles are; for motion, a storyboard with time, text, assets, text and image animation type, camera or transition, sound. No code before "ok". This controls the result and does not waste limits on redoing.

08.62 Collect edits into one list by timecode and do them in one pass. One batch of edits is one render. While edits go on, look at still frames, not full renders. After a render the agent shows still frames of those places.

08.64 Check before the full render. Still frames of each scene and the middle of each transition, an ffmpeg grid, look with eyes. Look for text beyond the edge, overlapping words, empty frames, serif font on frame 0, mirrored text, text in an unsafe zone. For motion: two stills 0.25 s apart must not match in any element.

08.65 Delivery: mp4 (H.264, yuv420p, faststart, for social CRF 22; A49), cover jpg (the strongest settled frame, which is also frame 0), a post text of 1 to 3 honest sentences. Each build is a new file `_v2`, `_v3`. The report says where the files are, what was checked and how, what was not checked. Do not add a platform or tool signature to the post unless there is a partnership or it is a "how it was made" post (B16).

### H. Brand and code-based motion design

08.67 A motion pack for a brand (rules for videos, subtitle templates, lower thirds, end cards) is a separate service, worth more than a single video. One client, one brand folder; every next video is faster.

08.68 Brand is not made up. The agent builds it from material. Four kinds: own works (10 to 20 best) in a portfolio folder, motion references (3 to 5 videos by others) and typography in a refs folder, links to library effects with a note on what is liked (save effects as links, do not download).

08.69 Describing style in words is hard; choosing by eye is easier. The agent builds a selection page (palettes, font pairs, subtitle styles, tempos, tricks, 3D, transitions) with checkboxes "take" and "more like this". 2 to 3 rounds. Then a brand file, a brand page, templates, a test video.

08.70 Motion cannot be described in words; show it by reference. A gallery prompt will not repeat a video. To get a similar one, give the agent the video itself.

08.71 Animate only after the storyboard is approved (6 key frames in one picture). Redoing a picture is cheap; redoing finished animation costs time and limits.

08.72 Events and cuts land on beats, the main trick on the drop. Without rhythm, motion feels soft and cottony.

08.73 Tie motion to frame time and tie randomness to a fixed seed. Otherwise the picture jitters on render. Compute everything from time `t`; no wall-clock timers or CSS transitions.

08.74 From effect libraries, view only demos and examples; the agent reads the docs. An effect from a site library is carried over as a visual effect, not embedded into a site.

08.75 Depart from the brand file only on direct request. If there are several brands and none is named, the agent asks.

08.76 Five reasons for a wrong video: no brand, a vague prompt, no references, animation before design approval, no rhythm.

08.77 Motion laws (numbers under Formulas): nothing stands still in frame, a soft ease curve, motion blur of about 6 sub-frames, at least 3 depth layers, a 3D element in at least every third scene, each scene its own trick, 2 main colors and 1 accent.

08.78 Real assets make the video: cut out people and objects and put them inside graphics; bare graphics lose. Honest numbers in HUDs only if they are true.

### I. Motion ads (generation, not code)

08.79 Two techniques. Code: the frame is laid out from HTML and 3D, you get what you wrote. Generation: the network draws what does not exist and cannot be filmed, but each run differs slightly. Best result is both together: generate the video, then add music, logo, subtitles and end card by code.

08.80 One idea per video: a mechanic you can retell in one phrase ("the whole world is black and white, only the product is in color", "one continuous shot with no cuts"). Not "pretty shots of the product".

08.81 Prompt for an ad model has six parts: format, palette in hex, main object and its distinct detail, captions, second-by-second storyboard, list of captions word for word. The model obeys a long precise description best.

08.82 First a 3 by 3 storyboard picture (16:9, 9 frames, time and caption under each). Video only after "ok". Video costs more; any fix on a picture is cheap. The approved grid goes as a reference for MiniMax-type ad models (A7). For other video models (`seedance_2_5`, `kling4_0`) storyboard frames are not fed into the video model; use reference cards and a setting frame. Video is not generated before "ok".

08.83 Fixes in words, one list. Every generation costs credits. One regeneration with five fixes is cheaper than five single ones; resend the whole prompt, not pieces.

08.84 A reference gives structure, not someone else's brand. Take structure, tempo, tricks. Do not carry the original's logos, texts, characters or music to a client.

08.86 Talking head with graphics: make graphics and captions in code; put generated angles as cutaways on pauses or under graphics; sound always from the source. Lips of generated speaking angles may not match: better to drop them than to keep a recognizably AI face.

08.87 Editorial explainer: one wrong number and the video goes in the bin. Check numbers against sources before generation, show the table of numbers before the run, and every number on screen is word for word from the table.

08.89 Honesty rules: do not promise "ready in 2 minutes" (generation and fixes usually take 30 to 90 minutes). Numbers, reviews and clients only if true. No real brands, logos or faces without consent; do not write "in the style of studio X", describe picture properties instead.

### K. Copies and publishing

08.90 Own content only. The copies tool is for your own videos: reupload, spread across accounts, make versions. Others' videos are not made unique.

08.91 Be honest about limits: there is no guarantee a platform treats a copy as new. Platforms look for repeats with a network trained on such edits and compare sound separately. Uniqueness lowers the match; new material works best. Say this to the user before the run.

08.92 A combination works: picture and sound and file together; own sound (other music or a new voice); 30 percent or more new material (another hook in the first 2 to 3 seconds, inserts, another ending); no more than 10 similar videos per account in 30 days (A48); post from different accounts on different days. Alone they work badly: only crop, only mirror, only noise, only metadata cleaning, changing caption and hashtags.

08.93 No mirror: reels almost always have text, and the platform network is not fooled by a mirror. Do not rotate plates on black backgrounds (a 1 degree turn makes a plate a skewed card).

08.94 Grain inflates the file: strength 1 to 2, CRF 21, ceiling 7 Mbit/s. Speed change up to 4.5 percent, audio pitch up to 2.5 percent; above about 5 percent it is audible on voice. Resolution above 1080 on the short side gives nothing.

08.95 Never count "done" blind. Check: md5 differs on every copy, all have sound, none is larger than the source, the contact sheet was viewed. Sound is not heard by the agent, so the report says "not checked by ear". Render into a temp folder, move the result to the user's folder.

08.96 Check the source first: inflated bitrate (6 to 10 Mbit/s is enough for 1080 by 1920), a MOV with a `qt` tag repacked to MP4, editor traces in metadata erased.

## Workflow

Two routes lead to the same result. Manual (a free editor like CapCut) fits assembling generated clips into a film. Code route (agent with ffmpeg, an HTML-to-video or Remotion-type engine if installed) fits motion graphics, subtitles, brand templates and repeatable videos.

1. Environment (code route): agent with file access, Node.js and ffmpeg, studio rules file, folders (stage 09).
2. Brand (if the video is for a client or in a set style): a brand folder, collected material, 2 to 3 rounds of choices, a brand file.
3. Select material: the live part of each generation, the best take by emotion, one format (frame rate, resolution, aspect ratio) (08.5, 08.6).
4. Rough cut without sound or color. Check: the story reads (08.3).
5. Music and rhythm: choose music, set cuts on beats and acts, plan hidden cuts and sounds between cuts (08.17, 08.18, 08.25 to 08.27).
6. Edit plan before render. For code montage: what is cut, where subtitles are, a storyboard of 6 key frames in one picture with time and trick. Wait for the user's "ok". Only then render (08.61).
7. Sound: layers by 07.69; voice from stage 07; check loudness by file (08.37 to 08.40).
8. Color: grade, tint layer, grain after upscale (08.41, 08.42).
9. Upscale accepted clips one by one, then effects (08.44, 08.45). This is a paid step: show the list, model, number of jobs and credits from the cost estimate, wait for "yes". Name any move outside the method as a deviation.
10. Subtitles and text: auto subtitles, fixes, two fonts, the hook as separate text, safe zones (08.49 to 08.55).
11. Check: grid of frames, still frames of transitions, loudness and spectrogram; collect edits in one list; each build a new `_vN` file (08.62, 08.64).
12. Delivery: mp4, cover, post text (08.65).
13. Copies for publishing, if needed: copies, check, spread by accounts and days (08.90 to 08.96).

Motion ad for a client: choose a niche and a company before the request; make a folder; read the client's site (colors, fonts, benefits, screenshots); write a 15-second script; make a 3 by 3 storyboard; "ok"; the six-part prompt; generate; finish with a code pass (music on beats, logo at the end for 2 seconds, cover from the strongest frame); price by cost.

## Formulas

Murch's rule of six, by weight:
1. Emotion, 51 percent. Do not kill it with a cut: hold the close-up half a second longer than comfortable.
2. Story, 23 percent. Every cut gives new information. A shot that adds nothing is extra.
3. Rhythm, 10 percent. The cut lands on the beat and the tempo of the scene.
4. Eye trace, 7 percent. If the hero looks up, the next shot shows the sky.
5. Screen plane, 5 percent. If a hero looks right at a creature, the creature in its own shot looks left.
6. Space, 4 percent. Where everyone physically is.

Three pillars:

| Pillar | Contains | Check |
|---|---|---|
| 1. Edit | Selection, rough cut, music and rhythm, cuts and transitions | The story reads; tempo changes with the acts |
| 2. Sound | Voice, foley, effects, ambience, boosters | Everything meaningful on screen sounds |
| 3. Color | Grade, tint layer, grain | All shots look shot by one camera |

Booster prompts for generated effects (English, one per effect; the longer set is in `templates/voice-and-music.md`):
```
cinematic riser, building tension, 6 seconds, dark thriller
deep cinematic impact hit with long reverb tail
fast whoosh transition, camera swipe
trailer braam, low brass, epic and ominous
dark ambient drone, slow tension build, horror
sub bass drop, deep boom
reverse suck in effect before impact
horror stinger, sudden sharp scare
footsteps on asphalt, city street, daytime
city street ambience, traffic, distant horns
```
Labels in order: riser, impact, whoosh, braam, drone, sub drop, reverse, stinger, foley, ambience.

Color and grain:
- Tint layer: Overlay blend, darken 20 to 25 percent (about 15 if dark).
- Grain: a separate video layer, Overlay, opacity tuned. Apply after upscale.
- Post order for Seedance clips: upscale (a batch size of at least 5 against flicker, if the tool has it), then grain and halation, then final grade.

Manual editor settings: music volume low under voice; effects louder than music but under voice; color filter intensity 40 to 50; HSL for single colors; two subtitle fonts; hook text 1 to 3 s; zoom by two keyframes; shot or accent change every 2 to 3 s; length 30 to 45 s.

Motion laws (1920 by 1080, for code motion):
- Every visible element makes a new step on every beat: shift 80 to 250 px, or scale plus or minus 10 to 40 percent, or rotation 3 to 25 degrees. Between steps drift at least 5 percent per second.
- Curve `cubic-bezier(.87, 0, .13, 1)` for moves, scales, rotations, masks, camera; step 0.30 to 0.50 s, fastest point on the beat. `ease-out (.16,1,.3,1)` for instant reactions; `linear` only for endless motion. No ease-in on entrances.
- Entrance 0.35 to 0.5 s, exit 0.12 to 0.16 s, cascade of neighbors 30 to 80 ms. Nothing appears from nothing: start at no less than `scale(.9)` with opacity and a blur of 12 to 14 px.
- Motion blur: average 6 sub-frames at a 180 degree shutter; do not fake with `blur()`.
- At least 3 depth layers; parallax background x0.35, middle x0.8, foreground x1.25; push-in +8 to 18 percent per scene, a nudge of 3 percent on a beat.
- One flash frame on a cut; a long flash of 0.2 s only on the main hit; shake only on hits, 0.3 s.
- A scene of 1.5 s (3 beats) is the norm for a 19-second video; a final call to action 1.8 to 2 s.
- 2 main colors and 1 accent; common grain 6 to 9 percent; vignette 26 percent.
- Text stays at least 0.3 s per word after it is fully in. Sans serif, no italics, bold.
- A 19 s render at 30 fps with 6 sub-frames at 1920 by 1080 takes 20 to 30 minutes. Always look at test frames before the full render.

Mix with ducking (local ffmpeg, optional):
```
ffmpeg -ss <start> -t <dur> -i track.mp3 -i sfx.wav -filter_complex \
 "[0:a]aresample=48000,afade=t=out:st=<dur-1.3>:d=1.3,volume=0.9[m];\
  [1:a]asplit=2[s1][s2];[m][s1]sidechaincompress=threshold=0.06:ratio=4:attack=5:release=200[md];\
  [md][s2]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.2:LRA=9" -ar 48000 mix.wav
```
Loudness check: `ffmpeg -i mix.wav -af ebur128=peak=true -f null -`. Spectrogram: `ffmpeg -i mix.wav -lavfi "showspectrumpic=s=1700x300:legend=0:scale=log:fscale=log" spec.png`.

Six parts of an ad-model prompt (MiniMax-type, 15 s):
1. Format first: length, ratio, style.
2. Palette in hex and the role of each color.
3. Main object and one distinct detail: the model keeps the product the same across scenes by it.
4. Captions: font, how they enter and leave, which word is highlighted by color.
5. Second-by-second storyboard (0.0 to 1.6 s, 1.6 to 3.2 s, and so on).
6. List of all captions word for word and the line "nothing else is written in the frame".
Defaults for such ads: 15 seconds, 16:9, 30 fps, palette with hex, a beat every 1.5 to 2 seconds, last beat a lock-up (name, second line, button) with a pause of 0.8 to 1.0 s and a fade. The model's own audio is uncertain (open question C5); put sound and music in post either way. The long template is in `templates/video-prompt-other-models.md`; the 3 by 3 storyboard prompt is in `templates/montage.md`.

Copies table (one set of parameters per copy):

| Layer | Edit | Range |
|---|---|---|
| Frame | zoom and shift | +1.5 to 3.5 percent over what rotation needs, shift within the reserve |
| Frame | rotation | 0.5 to 1.3 degrees either way (off on videos with plates; zoom +2 percent there) |
| Color | brightness, contrast, saturation, gamma, hue | plus or minus 0.025; 1.00 to 1.05; 0.94 to 1.08; 0.96 to 1.04; plus or minus 4 degrees |
| Texture | grain | strength 1 to 2, changing frame to frame |
| Time | speed | +2 to 4.5 percent |
| Time | trim of edges | 1 to 4 frames at the start, 1 to 6 at the end |
| Sound | pitch | -1.2 to -2.5 percent or +1.2 to +2.5 percent, tempo matched to video |
| Sound | equalizer | one band plus or minus 2.5 dB at 180 to 6000 Hz |
| File | metadata | all erased, new creation date, standard track names |
| File | container and codec | H.264 High, AAC 192k, MP4 `isom`, faststart, 30 fps |

Zoom needed to hide the corners after rotating by angle t on a frame W by H: `s >= cos t + (H/W) * sin t` (and the same with W/H; take the larger). For 9:16 and 1 degree it is about 1.031.

Contact sheet of frames for review: `d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "video.mp4")` then `ffmpeg -v error -y -i "video.mp4" -vf "fps=12/$d,scale=180:-1,tile=6x2" -frames:v 1 sheet.jpg`. Probe the source first: `ffprobe -v error -show_entries format=duration,size,bit_rate:stream=codec_name,width,height,r_frame_rate,bit_rate -of compact "video.mp4"`.

Cost of a short launch ad: a 3 by 3 storyboard picture, then one 15-second video, plan for 2 to 3 attempts. Get the numbers from `estimate_image_cost` and `estimate_video_cost` before running; do not quote fixed prices.

## Check before "ok"

Show the user only what passed this list. The stage is closed by the user's "ok".

- [ ] A live piece is taken from every generation, chosen by emotion.
- [ ] All clips are in one format.
- [ ] The story reads without sound and color.
- [ ] Music is chosen; tempo changes with the acts.
- [ ] Cuts are hidden in motion or blur where possible.
- [ ] The first second is clear and interesting without sound (hook, large readable text).
- [ ] Shot, angle or accent changes at least every 2 to 3 seconds; no three close-ups in a row.
- [ ] The voice is separated from the generation's sound.
- [ ] Everything meaningful on screen sounds; boosters sit on key moments.
- [ ] Voice is louder than music, final mix -14 LUFS; loudness and spectrogram were checked; the report says "not checked by ear" where true.
- [ ] If a cleaning service was used on voice: jingle cut, shift 0 at several points, first and last phrase in place.
- [ ] All shots look shot by one camera; grain does not fight the picture.
- [ ] Upscale was done on accepted clips and grain was laid after it.
- [ ] Subtitles stay out of unsafe zones; no text beyond the edge, no mirrored text.
- [ ] Code montage: the plan was shown and got "ok" before render; still frames of each scene and mid-transition were reviewed; two stills 0.25 s apart differ.
- [ ] Ad: the 3 by 3 storyboard got "ok" before video generation; on-screen numbers are word for word from the table; a reference's logos, texts and music were not carried over.
- [ ] Export matches the platform: mp4 H.264 yuv420p, faststart; cover; post text.
- [ ] Copies: md5 differs, all have sound, none larger than the source, the contact sheet was viewed, and the user was told there is no guarantee.
- [ ] Every paid step (generation, upscale) ran only after a "yes" on that step with its cost.

## Common mistakes

Edit and structure:
- Expecting the edit to rescue a missing or mismatched frame.
- Coloring and sounding shots that later drop out.
- Using the first and last frames of a generation (they are bad).
- Mixed formats (frame rate, resolution, ratio) causing jumps.
- Cutting a close-up of emotion early; picking a take for a clean background over strong emotion.
- Moving on before the story reads without sound and color.
- A weak start; everything told in the first two seconds; no struggle and no turn; a long first shot.
- No subtitles while many viewers watch muted.
- Same-type shots; a whole video in one shot; only landscapes without human emotion; a caption that explains the idea instead of a shot.

Sound and color:
- Flat sound under a speed ramp; mickey-mousing every movement; too much grain.
- Not checking the output of a voice cleaning service.
- Room echo on a recorded voice: record closer to the microphone.
- Music inside the generation; voice in one generation with a 3D previz.

Upscale and picture:
- Upscaling a frame before it is accepted, or using default settings.
- Detail or skin enhancers before video generation.
- Too heavy files (a huge photo or 8K where a lighter one fits).
- A video-upscale service may refuse content; plan a second way.
- Some models compress quality in clips over about 5 seconds; keep clips short and upscale.

Code editing:
- Asking a plain chat to edit video; a pile of everything in one folder; one very long session (cost grows with every step because the whole conversation is re-read).
- Editing one fix at a time instead of in one batch; asking "so what now" every minute; starting without a plan.
- A full render for each fix instead of still frames.
- Deleting things while tidying; always keep the originals.

Brand and motion:
- The five reasons for a wrong video (08.76).
- Effects that render differently each time because of live time and random numbers: tie motion to frame time and randomness to a fixed seed.
- A gallery prompt with "full creative freedom": each run gives a different video.
- Video generation before "ok" on the storyboard; fixes one at a time.
- Showing a key in the chat; doubling the connection (use one).
- Older models broke text (letters drifted); now captions hold if listed word for word.
- Giving charts and exact numbers to the generator.
- Carrying a reference's logos, texts, characters and music to a client.
- Static scenes when the original moves: regenerate only those scenes in one message.

Copies:
- Grain of strength 2 to 4 at CRF 19 inflated copies above the source.
- Rotation on plates; mirror; strong speed or pitch change; resolution above 1080; rendering straight into the user's folder; others' videos; only metadata cleaning, only crop or only noise.

Code-motion pitfalls: text wider than the frame; serif font on frame 0 (warm up fonts); empty frames from undecoded images; mirrored text when a word flips in 3D; words overlapping when letter spacing grows; text lost on dark clothing in a cut-out; 480 by 854 video full-frame looks soft; paths with spaces; a "video in letters" mask.

## Tools

Check `models_explore` for current models and `estimate_*_cost` for credits before any paid run. Nothing paid runs without the user's explicit yes on the exact list.

Higgsfield:
- Upscale: `upscale_video` with `bytedance_video_upscale`, or `topaz_video` (paid). `upscale_image` for stills. `reframe` for aspect-ratio changes. `remove_background` for cut-outs.
- Ad storyboard picture: `generate_image` with `nano_banana_pro` or `gpt_image_2_6`, one 3 by 3 grid.
- Motion ad video: `generate_video`, MiniMax-type `minimax_h3` where available, otherwise `seedance_2_5` or `kling4_0` with the six-part prompt.
- Audio for effects and music: `generate_audio` and `elevenlabs_music_v2_5` (see stage 07).
- `media_upload`: bring clips and audio back into a project.

Local, all optional:
- ffmpeg: cuts, format unification, grid of frames, loudness, spectrogram, export, copies.
- A free editor (for example CapCut) for the manual route: subtitles, filters, keyframed zoom, transitions.
- An agent with file access plus an HTML-to-video or Remotion-type engine for code motion and subtitle templates.
- A local upscaler such as SeedVR2 for clips, applied one by one before the edit.
- Python for a copies script and file checks.
- Websites of effect libraries and typography sources: look at demos only; save effects as links.

Open questions that touch this stage: C5 (sound of MiniMax H3), C6 (does a 480p draft predict the final), C7 (upscale order), C8 (copies). See `docs/defaults.md`.
