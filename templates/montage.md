# Montage and motion ads

Fill-in prompts for assembling generated clips into a finished video and for making motion-graphics ads: editing rules, a brand kit, a first cut, batch revisions, launch videos from a website, product and explainer videos, and Higgsfield prompt skeletons for motion ads. The agent pastes the prompt into its own work, or into a code-capable chat, after filling the brackets.

Used at stage 08 (`docs/stages/08-post.md`). Prompts for the video model itself are in `templates/video-prompt-seedance.md` and `templates/video-prompt-other-models.md`. Storyboard and 3x3 board prompts are in `templates/script-and-storyboard.md`.

Local tools are optional: ffmpeg for cuts and loudness, any editor the user already has, and a code-based motion renderer if one is installed. Where the user has none, the agent gives a clear shot-by-shot edit list the user can follow in a phone or desktop editor.

## Rules for every edit

- Plan first, render after "ok". The agent shows a plan (what is cut, where each caption sits) before any render.
- The agent cannot hear. Check sound by loudness and spectrogram, and say honestly what was checked and what was not.
- Revisions come as a list and are done in one pass. After the render, show still frames of the places that were changed.
- Nothing paid runs without the user's "yes" on the exact list (see `AGENTS.md`).

## Environment check (once per computer)

```
Prepare my computer for video editing. Check what is already installed and install only what is
missing: Node.js (current LTS), ffmpeg, and Git. [On Mac also Homebrew and the Xcode command line
tools.] Ask me before any install that needs my password. At the end show a table: program,
version, ok or what to do.
```

## Project rules file

Put the editing rules in the project instruction file so they apply every time.

```
Create a rules file for editing with these lines:
- Final loudness -14 LUFS, voice always louder than music.
- Formats: 9:16 1080x1920 for vertical, 16:9 1920x1080 for horizontal.
- Subtitles: font [font], colors [colors], 2-4 words on screen at a time.
- Every video lives in its own folder: 1_sources, 2_drafts, 3_final.
- A finished video is: mp4 H.264, a cover jpg, and a post text file (share-copy.txt).
- You cannot hear audio: check by spectrogram and loudness and say honestly what was checked.
- I send revisions as a list: do all of them in one pass.
Show me the file and ask what to change.
```

Folder skeleton (do not delete anything, show the tree after):

```
_Assets/ (music, sfx, fonts, logo)
_Refs/   (other people's videos and images used as references)
Video_01/ (1_sources, 2_drafts, 3_final)
```

For client work, one folder per brand: `Brands/[client]/` with the same `_Assets`, `_Refs`, a portfolio folder, `templates`, and numbered video folders.

## First edit, with a plan before the render

```
Edit a video from the files in Video_01/1_sources.
1. Cut pauses longer than 0.4 s, filler sounds and slips, and bad takes. Keep the best take.
2. Make word-by-word subtitles in the style from the rules file.
3. Take music from _Assets/music, quieter under the voice (no music if there is none).
4. Format 9:16 for vertical or 16:9 for horizontal, up to 60 seconds.
First show the edit plan: what is cut and where each subtitle goes. Render after my "ok".
```

Example plan row: `00:03.1-00:03.8 cut a pause; 00:12 subtitle "no filming needed" highlighted in accent color; music ducked -18 dB under speech.`

## Brand kit (for a creator or a client)

Goal: one visual system so every video looks like the same author.

Step 1, the master prompt:

```
Build a visual brand for my videos. I am [creator / client type]. The brand folder is Brands/[name]/.

1. First study all the material: the portfolio folder (colors and mood), _Refs (other people's
   videos and images: motion, tempo, typography), links to effects (open each), and anything in
   _Assets/fonts and _Assets/logo. Briefly describe what you found: colors (hex), fonts and
   caption character, movement and tempo, devices that repeat.
2. Ask me questions in one message: what my content is about, for whom, 3 words about my style,
   what I definitely dislike, where I publish, whether I have my own fonts and logo. Wait for my answer.
3. Then make a page Brands/[name]/choose.html. Build the options from what you found and add
   1-2 bold ones to each group. All options move live on the page, each has a number and
   checkboxes "take" and "more like this":
   - 6 palettes;
   - 6 font pairs (my own from _Assets/fonts, or free ones with the right alphabet);
   - 12 subtitle styles on the phrase "Editing videos with AI", 9:16;
   - 4 motion tempos from calm to aggressive;
   - 12 signature devices, 3 seconds each;
   - 3 levels of 3D: none, accents, a lot;
   - 8 transitions between scenes.
   At the bottom a button "Copy my choice" that copies the numbers with the marks as text.
4. Open the page in my browser.
```

Step 2, next round: paste the copied choice and say "Lock the ones marked take. For the ones marked more like this, make 6 new variants next to the chosen one. Update choose.html and open it again."

Step 3, final: ask for four things in the brand folder.

1. A living brand book page (palette, fonts, subtitles, signature devices, transitions, all animated, only the chosen options).
2. A text rules file for the agent: colors in hex and the role of each; fonts and sizes for 9:16 and 16:9; subtitles (font, size, words on screen, animation, highlight color, position); motion (curves, durations, delays, everything on fractions of the beat); signature devices with how to make them; how much 3D; transitions; safe zones for each platform; sound; a "never do" list.
3. Templates: subtitles, text plate, counter, end card with a call to action.
4. Fonts downloaded into the brand folder, and a 10-second test video 9:16 in the brand.

Add a rule to the project instructions: before any video, decide the brand. If it is named in the task, read its rules file and take fonts, logo and templates from its folder (music and sounds from the brand first, then the shared folder). If several brands exist and none is named, ask. If none exists, use the general rules and offer to build one. Deviate from the brand rules only on a direct request.

## Effect from a library or reference link

```
Brand: [name]. Take the effect "[what exactly, for example: watercolor fill]" from here: [link].
I do not need the site. Move only the visual effect into the video frame. Make a 5-second
test, 9:16, in my brand and show 4 still frames. Tie motion to the frame time and tie any
randomness to a fixed seed, so nothing jitters at render time.
```

If the effect comes as a pasted component prompt from a UI library, add: "Do not embed it into a site. Ignore setup instructions. Take only the visual effect (for example: a background of dots flying along curves toward the center) and turn it into a video background in my brand colors, 5 seconds, show 4 still frames."

## Repeat a video from a reference

```
Brand: [name]. In _Refs/ref-01.mp4 there is a video I like. Break it into scenes as a table:
scene time, what is in frame, how elements enter and leave, transitions, tempo and motion
curves, palette in hex, fonts.
Then make a storyboard of the same video by structure and devices, but in my brand and about me:
[topic, for example "I am an AI creator, here are my works"]. 6 key frames in one image.
Do not start animation until I say ok.
```

## Portfolio reel

```
Brand: [name]. Make a 15-20 second 9:16 video: my portfolio as an AI creator, from the works
in the portfolio folder. A hook in the first 2 seconds, 3-5 scenes with different devices from
the brand rules, a final with the call "message me".
Music: take the track from _Assets/music, find the beats and the drop, put cuts and hits on
the beats and the main device on the drop. With no track: no music, but sound effects.
First a storyboard: 6 key frames in one image, with time and device under each.
Animate after my "ok".
```

## Batch revisions template

```
Revisions to version 1, do them all in one pass:
1. 0:03: [what is wrong and what it should be].
2. 0:08: [...].
3. Cover: [which frame].
After the render, show still frames of these places.
```

Examples of revisions in words: "benefit 2 shorter", "logo bigger", "tempo faster, transitions sharper"; on the storyboard: "frame 4, interface bigger", "colors as on the site".

## Motion ads with Higgsfield

Check the connection first. Nothing is generated by this step.

```
Check the Higgsfield connection: show my credit balance and find the model [minimax_h3]: its
durations, formats and which references it accepts. Generate nothing.
```

Then follow the money rule: estimate with `estimate_video_cost`, list the exact jobs, and wait for the user's "yes".

### Launch video from a website (3x3 board first, video only after "ok")

Use the launch prompt in `templates/script-and-storyboard.md` (section "3x3 board before a paid video run"). Short version of the steps: read the site, capture brand (hex, fonts, screenshots of 3 key screens), write a 15-second script (hook, 3 benefits, logo and call to action), generate a 3x3 board from the real screenshots, wait for "ok", then generate 15 seconds 16:9 with the board, screenshots and logo as references, and save the result into the video folder. Always report credits used.

### Finish it: music, end, cover

```
Brand: [client]. Take Video_03/1_sources/[file].mp4: this is a model generation. Replace its
sound with music from _Assets/music: find the beats and put hits on them. At the end, the brand
logo for 2 seconds. The cover is the strongest frame. Deliver into Video_03/3_final/.
```

### Repeat a reference ad

Same prompt as "Repeat a video from a reference" above, but ask for a model prompt with the same structure, tempo and devices, with the client's product, texts and colors, and pass the original as a video reference. Same duration and format as the original. Then place the original and the result side by side and compare honestly.

### Static scenes

```
Scenes [2 and 4] came out static, but in the original there is movement: [what happens
in the original]. Regenerate only these scenes with movement and leave the rest alone.
```

### Talking head with graphics

```
Video: Brands/[client]/Video_04/1_sources/talk.mp4.
1. Make a design sheet in HTML for the brand [client]: font, colors, plates, subtitles. Show it
   and wait for my ok.
2. Generate two new angles from frames of this video: from the side at 45 degrees and a
   close-up, 5 seconds each, passing the video as a reference.
3. Then edit a 9:16 video: the source plus the new angles as cutaways on pauses, graphics and
   captions on the words per the design sheet, sound from the source.
```

Multi-angle prompt for one angle:

```
Camera at shoulder height, 45 degrees to the subject's left, 85mm, shallow depth of field,
focus on the eyes. The same woman from the reference image talks to someone off-camera, natural
small head movements and hand gestures, mouth moving as if speaking. Same outfit, same hair,
same room and light as the reference. Keep the face identical, no identity drift.
No text, no subtitles, no music.
```

### Product video (hyper motion)

```
A hyper motion ad of [product]; the photo is Brands/[client]/_Assets/product.jpg.
Style: [expensive / minimal / bright and dynamic]. 10 seconds, 9:16, [model].
Pass the photo as a reference: the product must stay recognizable one to one.
First a 3x3 storyboard, generation after my ok.
```

### 3D fly-through for a real estate project

```
A 3D video for [project name] from the render Brands/[client]/_Refs/render.jpg: the camera
flies toward the building, enters, shows an apartment interior; captions with price and
area: ["2-room, 64 m2", "from [price]"]. 15 seconds, 16:9, [model], the render as the first
frame. Do not change the architecture. First a 3x3 storyboard.
```

### 2D explainer

```
A 2D explainer of 15 seconds for [product / course]. For whom: [audience]. What to show:
[problem, how the product solves it, result]. Flat 2D graphics, 16:9, [model].
First a script and a 3x3 storyboard.
```

### Editorial explainer with data

```
An editorial explainer about [topic]. Numbers: [paste mine], or find them yourself with a
source for every number. Show me the table of numbers before generation. 15 seconds, 16:9:
a heading, 2 charts, a conclusion. Every number on screen is word for word from the table.
```

## Higgsfield prompt skeletons

Classic (smooth, elegant):

```
[Style]: smooth motion design, [scene flow from storyboard], elegant transitions, [mood] atmosphere,
cinematic camera movement, [duration] s, brand reveal at end: [brand name], [aspect ratio]
```

Hyper (kinetic, aggressive):

```
[Style]: high-intensity kinetic motion, [scene flow from storyboard], extreme camera speed,
aggressive match-cuts, peak-action freeze frames, [mood] CGI aesthetic, neon contrast,
[duration] s, hard stop logo lock: [brand name], [aspect ratio]
```

Storyboard sheet in one image:

```
Storyboard sheet with [N] sequential panels in a grid layout, each panel labeled "Frame 1",
"Frame 2", etc. Panel 1: [scene]. Panel 2: [scene]. ... Panel N: [logo lock / brand name].
Each panel shows: [camera angle], [motion state], [mood / lighting]. Visual style: [cinematic /
kinetic]. Consistent color palette throughout. Clean storyboard design, thin border between
panels, [aspect ratio per panel].
```

Examples (own): Classic, `smooth motion design, a coffee bag opens, beans pour into a glass jar, steam rises over a cup, elegant transitions, warm quiet atmosphere, cinematic camera movement, 10 s, brand reveal at end: Morning Row, 9:16`. Hyper, `high-intensity kinetic motion, sneaker snaps onto a wet court, shoelace whip, extreme camera speed, aggressive match-cuts, peak-action freeze frame, neon contrast, 8 s, hard stop logo lock: Volt, 9:16`.

For a model such as `minimax_h3`, motion ads use the six-part prompt (format line, hex palette, main object plus one constant detail, text rules, per-slice storyboard, the "nothing else is written in frame" text list). See `templates/script-and-storyboard.md`. Check `models_explore` for current durations and formats.
