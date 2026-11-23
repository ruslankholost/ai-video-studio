# 06 Video

This stage turns the finished frames, reference cards, storyboard and previz into video clips. The method in one paragraph: Seedance 2.5 (`seedance_2_5` on Higgsfield, omni reference) is the main model. The previz montage from stage 05 goes in as a video reference, `@Video1`, and gives only camera movement, positions, paths and timing, never looks, faces or hands. Every input image has a written role. The prompt is the Chinese JSON from `templates/video-prompt-seedance.md`, with the camera (机位) written before the picture (画面) and the acting (表演) written through the body for every shot, integer-second timecodes, at most 5000 characters, checked with `scripts/check_prompt.py`. Work in batches of 10-15 s (Seedance 2.5 takes up to 30 s), draft at 480p, check a frame grid side by side with the previz before assembly, regenerate only the bad shots, and upscale at the end. Other models (Kling, MiniMax, Omni) use the same formula with different syntax. Voice and music belong to stage 07.

A video prompt is built from one formula for any model: inputs, anchors, camera, object and order, sound and dialogue, environment and negative. Models change, the formula stays.

## Input and output

Input, before the stage starts:
- `brief.md`, `idea.md`, `script.md`, `moodboard.md`, `storyboard.md` (with angle, lens, camera move, who is in shot and what they do, location, sound).
- `refs/`: reference cards of characters, locations and recurring objects (a sheet of views).
- `frames/`: start frames (poster, first and last frame, frames for image-to-video).
- `previz/`: the Blender blockout, if the camera must be held exactly (stage 05).
- The frame format (9:16 or 16:9) decided before the first generation.

Output:
- `prompts.md` with every video prompt of the project in one file. An edit rewrites the prompt in place, no new files.
- `video/` with the clips. Name by meaning (scene, take, quality), for example `part1_take2_480p.mp4`. Rejected clips are not deleted but moved to `drafts/`.
- A frame grid (contact sheet) of every clip for checking. Clips are without voice and music if those are added in stage 07 and in the edit.

## Principles

Only what does not depend on the model. Model-specific limits and syntax are in the templates (`templates/video-prompt-seedance.md`, `templates/video-prompt-other-models.md`) and in "Tools".

### A. Formula and inputs

06.1 **A video prompt is written differently from a photo prompt.** The model takes a start state (a frame or text) and predicts how it moves through time. Writing a video prompt like a photo prompt is the first mistake.

06.2 **One formula for every video model. Do not learn a separate prompt per network.** Syntax differs, the thinking is the same. Character limits, tags and model-specific words are a thin layer on top of the formula, not a replacement.

06.3 **The formula has six blocks in order of importance: inputs, scene and anchors, camera movement, object movement and order, sound and dialogue, optionally environment and negative.** The prompt is built "not from a description of the scene, but from what the model cannot see itself". Write each block concretely, not "average".

06.4 **Every input file gets a role: what it is and how to use it.** Without roles the model mixes inputs into a mush. Example: "Image 1 is the start frame. Image 2 is the character, keep the face." Seedance wants each tag explained at the start of the prompt. Kling wants the same: given only asset IDs, the model guesses their use and results are less predictable.

06.5 **For every input, write what we take and what we do NOT take.** Any object card drags its shooting environment (a studio, a grey backdrop, a grid) into windows, openings and reflections. A character card gives the look but not the pose or expression. Pose and emotion are written in the acting of each shot.

06.6 **Do not re-describe a scene that a photo already shows: fix only the anchors, what the model may smear or remove** (a sign, a logo, a face, an important object). Example: "Keep the inscription on the label."

06.7 **The input switch: the blocks stay the same, only how much you write in "Scene" and which blocks you include changes.** Modes: text to video, one image, start and end frame, several images (multi-reference). Details are in "Workflow".

06.8 **Do not give storyboard frames to the video model.** Storyboard images are for a human to see the story. The video model gets character cards, locations, recurring objects and the start frame. Make a reference sheet only for what appears many times: a one-episode prop or place needs one image. Exception: MiniMax H3 for motion ads takes the approved 3x3 grid as a reference and may use a storyboard frame as `start_image`. Using the first frame in image-to-video (Kling and others) is a separate, allowed trick.

06.9 **A face is held most reliably by a finished frame and a reference card (face from several angles plus the look), not by text.** Seedance holds a face badly from text, but given a finished image it simply animates it. A reference card holds a face much better than one photo.

### B. Camera

06.10 **Always set the camera: "if you do not, you get a random one".** Film terms (dolly, crane, tracking) give professional camera work. A named move gives predictability and fewer tries. The camera carries emotion: a slow push-in builds tension, tracking adds dynamics, a static frame focuses on details.

06.11 **The angle comes first in every shot and is never left to the model.** "The most important thing in a prompt is the angle. It matters more than the plot, materials and light." Scheme: point of view, height, angle, focal length, what is in focus, then the action. Kling: write the camera as a path, not two points, or the model joins them with a cut. Omni: camera first, it sets the visual grammar of the whole clip. For Seedance 2.5 the JSON puts camera (机位) before picture (画面).

06.12 **Set shake explicitly and in every span.** In documentary shooting, "if you write it once at the start, the model evens out the picture". Repeat "handheld, amateur documentary", shake, horizon tilt and focus in every span. For a smooth camera write the opposite: Kling `smooth stabilized flying camera, no handheld shake`; Omni `locked off camera` or `smooth gimbal movement, no shake`.

06.13 **When a prompt cannot hold the camera, film it first: a Blender previz.** The video model carries over everything it sees (shake, closed windows, a run that is too fast), so mistakes are caught in the previz, not in generation. Load the previz in a separate role: take only camera movement, places of people, paths and speed. Blob colour is only a label. (Stage 05.)

06.14 **One clip, one main camera move.** Seedance 2.0 guidance: do not mix several moves in one prompt. Seedance 2.5 allows a camera instruction in each time span of a master prompt. These are different levels (per clip, per shot). The 2.5 prompt writes the camera in every shot; the previz supplies the main move.

### C. Object movement, order, acting

06.15 **For the object write what it does and in which order, one after another, the key action first, optionally by seconds.** "Several actions at once confuse the model." "One shot, one action, one camera move. Put two actions in a shot and you get flicker."

06.16 **Set movement like a director's brief:** video generation is "conducting attention and dynamics inside one frame". Not "the model walks", but how she walks (confidently, gracefully, tired), where she looks, what her hands do, how the movement relates to the world. Without a brief the model invents motion.

06.17 **Write acting in every shot with people: pose, actions in order, emotion by body (brows, eyes, mouth, hands, torso), manner of speech, a gesture on a word, reaction of the background.** Without it the result is "blobs: standing straight, empty faces, hanging hands". "The model does not draw the word 'scared', it draws what is visible." Kling: `scared` is not drawn, "eyes bulge, eyebrows shoot up, mouth wide open, shoulders up at his ears" is. Kling plays emotions more reservedly, so write acting bigger. Describe emotion by physical signs of face and pose, not by name. For a shot with no people mark it ("no people in frame" in Kling, a note in the acting field in Seedance 2.5). For a crowd: "only scream, they say no words", or the model hands out lines.

06.18 **Every hero with an image appears in every span, not only at the start: "so faces do not mix".** The street lives: where a street is visible, write cars, pedestrians, cyclists, "otherwise Seedance makes an empty city". In an ad, strengthen the character lock at the start of each shot with the character (`Same woman as @image2, identity stays locked on the reference face.`).

06.19 **Name the physics: "Seedance simulates physics only if you name it. Without the words there is no physics."** Examples: `mozzarella stretching with elastic snap physics`, `cloth inertia on sleeves`, `hair physics active`.

06.20 **Magic, fire and transformations are described as physics.** "Seedance does not know what 'magic' is." Without a physical description it draws the nearest real analogue: coloured powder, paint, flat coloured fog. Write what the effect is made of physically, how it interacts with the environment and where the glow falls. A transformation runs in phases (birth, spread, surface, completion) and is never covered with a flash. In the 2.5 JSON the covering of a transform with a white flash is an explicit prohibition.

### D. Shot structure, multi-shot, length

06.21 **A shot in an ad has four elements: action, camera, physics, audio.** "The difference between a bad and good result is not the tools but how exactly you describe each frame."

06.22 **Multi-shot: each shot is a separate picture plus its own movement.** Four shots in 15 seconds are four small prompts inside one. First the roles of all inputs, then one shot, one action, one camera move, then a split by timecodes so the model knows the seconds per shot and does not rush the ending. A long multi-shot prompt of 5-8 thousand characters is fine for models that allow it. For Seedance 2.5 the hard limit is 5000 characters.

06.23 **Timecodes are mandatory for anything longer than 10 s, run back to back with no gaps and cover the whole running time.** "Seedance sees the video but interprets timing in its own way without timecodes." Seedance 2.5 uses integer seconds only (fractions are not understood), the shortest block is 1 s. Kling and MiniMax accept fractions. Write the storyboard in the units of the chosen model.

06.24 **Write slow motion and speed changes inside the shot with boundaries** (where it slows, where it returns to real speed). Without "slow motion" the model decides the object is just slow. Example: `slow motion 120fps` and `snap to real-time`. For Seedance 2.5 there is no default ban on slow motion: add it to the negative only if no slowdown is wanted. A slowdown at the peak is best made in the edit (speed ramp) rather than in generation.

06.25 **Transitions matter most in a video made of screens:** "without them you get hard cuts and jumps between frames". Describe each transition in words (what appears, what disappears).

06.26 **A video longer than the clip limit is cut into parts.** The second clip begins with "This is a direct continuation of the video from @video1". Cut at natural seams (a scene change, a flash, a blur), not in the middle of a slow-motion or a morph, and repeat palette, hero and anchor in each part.

06.27 **Generate a long scene in batches of 10-15 s, one clip at a time ("more action that way"), then edit.** One batch is a manageable size to review and to repair.

06.28 **Do not mix too many scenes and do not give contradictory instructions: the model gets confused.** Do not write vague words ("cool, nice, beautiful").

06.29 **Cut density:** for a dense edit at least 2 s per shot, for drama 3-4 s, 15 cuts per 30 s is the top. Five shots in three seconds also work if intended. Same-type shots drag: "three close-ups of a face in three seconds is too many". Alternate wide, medium and close. Our measure of leader videos: a new place every 3-5 s, shots of 1.5-2.5 s.

### E. Sound and dialogue (inside the video prompt; voice and music are in stage 07)

06.30 **Write sound inside each shot, not in one line at the end: "Seedance ignores a sound line at the end of the prompt".** The model then ties sound to the moment. For Seedance 2.5 and videos longer than 15 s, sound by timecodes. For Kling, an `AUDIO` line in each beat.

06.31 **A line of dialogue is written verbatim, in quotes, once, in its own shot, with the language named: lip sync lands more exactly.** If one person speaks, the others stay silent (Kling: "When one person is speaking, the others remain silent. No interruptions or overlapping dialogue."). Speech speed is 2-2.5 words per second, the block length fits the line.

06.32 **Do not order music by default.** Seedance: `No music, natural ambient sounds only` (2.0) and `没有背景音乐` ("no background music") with a duplicate in the negative (2.5). Music and effects go in the edit as separate tracks, so the track can be swapped in minutes. Do not put a voice into the generation together with a 3D previz: "overload, the animation worsens and quality drops". Music inside the prompt is allowed only for a finished ad made in one generation.

06.33 **Ready voice or audio goes in as an input, not as words:** `voice and lip sync reference @Audio1 exactly`, `video rhythm references @Audio1's beats`. A voice from an audio reference is described in a separate field without the line text and with a ban on regeneration, while the line text is still written in its shot because it sets word boundaries. If the voice is laid on after generation, shape the lips to the future voice (blocks of 2-2.5 words per second). A voice made by the model can be used as a timing guide and replaced later. Whether lip sync holds with a video and an audio reference together is untested: test one short dialogue shot in a draft.

### F. Environment, negative, positive description

06.34 **Environment: wind, dust, glints, steam.** An optional block. The negative lists only what must not be in frame: shake, a static background.

06.35 **Describe what should be there instead of forbidding.** "Negative prompts do not work, only positive descriptions": `no blur, no noise` becomes `sharp focus, crisp details`; `don't move fast` becomes `moves slowly, deliberately`; `no extra fingers` becomes `anatomically correct hands`; `no flickering` becomes `stable, consistent lighting`. Kling: negative prompts can raise error likelihood, only two are truly necessary: no subtitles and no background music. Example of positive instead of a ban: "four doors closed from start to end". Replace judgement with a visual fact: "cinematic, epic, stunning" becomes "24mm, low angle, warm tungsten key from the left, teal shadows, fine grain". Per model: Seedance 2.5 wants a short concrete negative (rule 06.36); Kling and MiniMax mostly describe positively, MiniMax uses a ban list for clean styles (`no grain, no vignette, no lens flare`).

06.36 **If a negative is needed, it is specific to this scene** (snow, a car in reverse), not generic junk ("extra fingers"). In Seedance 2.5, every problem closed by text in the body of the prompt is repeated as a ban in the negative: one mention is not enough. The negative stays short, for example `Avoid jitter, bent limbs, face drift`.

06.37 **An exact count instead of a ban:** "EXACTLY TWO fighters" (Kling invents extras: a child, a jacket). For boards of 2x2, `FRAME LOCK` stops a grid or split screen.

06.38 **A screen with text in frame needs its own reference with the exact text, and you check the letters by eye.** MiniMax: list the exact strings in the prompt (COPY LIST: "exact strings, nothing else appears in frame"). MiniMax H3 keeps inscriptions and interfaces straight if the prompt lists exactly what is written.

06.39 **Light is the highest-leverage element:** write it concretely (source, angle, temperature), not "cinematic lighting". One dominant colour temperature per scene.

### G. Language, character limit, prompt check

06.40 **Language of the prompt depends on the model.** Kling, Grok and Google Omni understand Russian and many languages: write straight by the formula. For Seedance, draft in your own language and have the agent translate to Chinese (the JSON is Chinese). Seedance is a Chinese model, so no problem. Chinese is about three times shorter than Russian or English. Spoken lines stay in the language they are spoken in. Spoken Russian in Seedance 2.5 works but is not in the published language list. The language of the prompt and the language of speech in frame are different things.

06.41 **The character limit is bypassed in two ways:** translate to Chinese (3x fewer characters, no loss of quality) and "prompt as image" (print the whole prompt as text on a white background in an image model, upload it as a reference captioned "this is the execution instruction"). Lines inside a Chinese prompt remain in the original language.

06.42 **Count the limit with code, not by eye.** After a prompt, print `characters: XXXX / 5000` for Seedance 2.5 (4000 for 2.0). A prompt is output whole and an edit means the whole prompt again: "patches lead to assembly errors".

06.43 **Check the prompt with a script before generating.** For Seedance 2.5, `scripts/check_prompt.py` checks: valid JSON, length, integer timecodes with no gaps, the camera before the picture, the acting written through the body, text outside Chinese appears only in dialogue lines, instruction words, warnings about music and slow motion. It does not catch a typo in a Chinese character, so read it yourself. Kling 4.0 has its own `check_prompt.py` (see `templates/video-prompt-other-models.md`).

06.44 **Only what is seen and heard.** "Write only what is seen and heard, short, no repeats." The prompt describes the video, it is not a note to the model about how to work: no rules for the model, no process ("they will dub later", "this is a previz"), no "why", no repeats.

06.45 **No author signature and no brand or studio names in the body of the prompt.** Seedance tends to render any text in the prompt right into the frame, and a studio name is "a label with no technical information" and a filter trigger. Write properties of the picture instead of a brand.

06.46 **Do not mention real celebrities or copyrighted characters: moderation cuts them.** Do not try to get around the rules for real people. If a harmless prompt is blocked: add 2-3 film terms, retry 2-3 times (the filter is probabilistic) and replace trigger words with neutral physical ones (`attack` to `impact`, `soldiers` to `armored figures`, `kill` to `final moment`, `blood` to `red mist`). Real faces sometimes trip moderation: a full-length photo helps, and anime, illustration and AI-generated faces work best.

### H. Process: draft, regeneration, checking

06.47 **Cheap first: a 480p draft, then finishing.** "Only a draft can be taken to 1080p, and it will be the same clip, not a new take": order the draft as a draft, not just at low resolution. If you do not like it, fix the prompt and make a new draft. If you do, finish the draft. Resolution of the draft question: static and simple scenes get a cheap draft or a 4-5 s test first, then the same clip is finished. Dynamic scenes (chase, fight, crowd) may behave differently at 480p and at full resolution: test one dynamic scene at both before relying on drafts for such scenes. Budget for both cases.

06.47a **Seedance reference drafts** (2026-11-23): length Auto with the length written in the prompt (not a fixed 5, 10 or 25 s), sound on, 2 to 3 drafts before any finish. The order of numbered references in the prompt must match the order of the attached files exactly.

06.48 **A paid generation runs only after the user's "ok".** Show the model, mode, frame format, length, resolution, with or without sound, files and roles, price (from `estimate_video_cost`) and the prompt. An "ok" for one run does not carry to the next. Cheap picture first, expensive video second: a 3x3 storyboard in one call, and no generation before the "ok".

06.49 **Regenerate only the bad shot, not the whole video:** "A bad shot: regenerate only it." Generation slips (people walking backwards) are regenerated. If the network made a mistake (through a wall, through a door), "that shot is garbage, fix the prompt".

06.50 **Collect edits into one message:** one regeneration with five edits is cheaper than five single ones. A finished video is edited in words only in models that can (Kling `Edit @Video1... Keep everything else unchanged`; Omni "Change X. Keep everything else identical."). Others rewrite the prompt (06.52).

06.51 **Versions are not overwritten:** every new previz or video is a new file, the old one goes to `drafts/` as `draft_<what>_vN.<ext>`. All project prompts live in one `prompts.md`.

06.52 **Check a clip with a frame grid (contact sheet):** the style of every frame, the direction of movement across several frames, faces, hands, text. Check sound without listening by loudness and spectrogram and say honestly "not checked by ear". Edit one variable at a time and add "Preserve all previous changes" (Omni: do not rewrite from scratch). Seedance 2.5 and Motion MCP rewrite the whole prompt.

06.53 **Upscale always, and before effects.** "We do it in every lesson, and you always do it." Turning a photo into a video loses 15-20 percent of quality, and a short Kling clip "gladly compresses quality", so it goes through an upscale pass. Resolution of where to upscale: for Seedance, references are not upscaled and are slightly dirtied, and skin enhancers and sharpeners run only after the video. For Kling Motion Control, upscale the source photo before animation. Upscale accepted clips one by one before the edit (before grain and grade), and do not upscale the assembled video a second time. Whether per-clip upscale beats upscaling the finished video is untested: try one clip both ways.

### I. Task recipes

06.54 **An ad from a poster:** a static poster (an image model) with a consistent character and brand references becomes the start frame and Seedance animates it; the character comes as a separate reference frame. The background changes everything: switching an orange background to black moved the style from "ordinary pizza ad" to "Asian comic energy drink". "Name the graphics concretely": "motion graphics" gives a weak result, while `speed lines`, `comic burst stickers`, `polaroid photo collages`, `flame graphics`, `kinetic typography` are applied literally. A low angle from below gives heroism and appetite for food.

06.55 **Game style:** quality comes from consistency, not tools: "each step is built on the previous one as a foundation". Chain: blob, game 3D style, screens, video. Each screen uses the previous result as a reference. The prompt begins "Same detailed 3D game character". The mouse cursor is a constant across the clip. Transformations like a transformer: mechanical sound, sparks. End with "AAA, Unreal Engine 5, cinematic".

06.56 **Morphing is a transformation of one object, not a transition between scenes.** Give a first frame, a second frame and a prompt on the mechanics of the change: "the action block describes not the style but the mechanics of the transformation" (how, physics, volume and shape). For morphing, set the maximum clip length: the change is more detailed, and speeding up in the edit looks better. Ten action templates are in `templates/video-prompt-other-models.md`.

06.57 **A construction timelapse:** everything is built on one final image. First stage prompts and stage frames come from it in an image model, then Kling animates the transitions between neighbouring frames. The camera is the same and stable in the stages ("no drones, no aerial, no top-down, no sudden angle change, no teleportation"), a fly-in only in the last frame (optional). More stages, more interesting video.

06.58 **Start plus end:** give the first and last frames and describe exactly how the first becomes the second. In Seedance this is First Frame plus Last Frame (`start_image` and an end image where the model supports it).

06.59 **A neuro-model and dance (Kling Motion Control):** "the video sets HOW (movement, expression, tempo), the prompt sets WHAT (who is in frame and on the background, and camera control)". The reference video has a static camera, no zoom, no shake. The character in the photo stands in the same angle and at the same distance as in the video. Prompt: "Static camera". Generate several variants, failures are normal. Kling 2.6 without sound often makes the character talk by default: state the expression ("a slight smile, mouth closed"); keep clips to 5 seconds or "everything swims". Use the `motion_control` tool.

06.60 **Clip formula from a frame:** "what is in frame + what the main action is + how the camera moves", and a block at the end that keeps light and colour ("Keep the original lighting and color from the reference, no relighting, no flicker, no warping..."). The same principle holds for Kling, Veo 3.1 and Wan. Use a preset instead of a long prompt when the scenario is already in it.

06.61 **A cartoon** needs close-ups, cutaways and different angles for live, dynamic video. Animate a frame from an image with an action description. **UGC** and AI-influencer work use the same workflow: fashion video and product integration from a creator reference card and a product card, and eight videos with different characters from one product photo. (The source gives no prompts for this, so take the formula.)

06.62 **A video from a reference clip:** the reference gives the structure, not a foreign brand. Break the original down by scenes (time, what is in frame, text, transitions, tempo), write the prompt, pass the original as a video reference, compare honestly. "We do not carry the original's logos, text, characters or music into client work."

06.63 **Model by task:** a face in frame means a finished frame as reference, not text, and a model chosen by task and by the newer version. Default for realistic scenes: `seedance_2_5`. Kling for a face in shot when Seedance rejects the reference, and for Motion Control. Russian speech and price: Grok. Talking head with lip sync and sound in video: Veo 3.1. Quick draft: Omni Flash. Wan 2.5 is not used for characters (weaker consistency and audio).

06.64 **A whole pipeline in one place saves hops:** the result of one model feeds the next. Work through the agent and the Higgsfield MCP, and save generations right away.

### J. From observed example clips

These come from reviewing finished clips, not from lessons.

06.65 **"One continuous take" in a prompt does not guarantee no cuts: count cuts in the finished clip.** In several clips the prompt began with "cinematic continuous single-take shot" and the result was an edited montage with hard cuts at about 6, 10, 14, 18, 20 and 22 s. Others, truly cut-free, existed in the same set. Check on the frame grid (06.52).

06.66 **Listen to the sound of a finished clip separately from the picture: a ban on music in the prompt does not guarantee silence.** One clip with "No background music. Only: metal clashing, energy bursts…" came out with a choir chant, a synth bed and an unwanted line of speech. Listen to every clip's track before acceptance and remove or replace the extra in stages 07 and 08. See 06.32.

06.67 **Hold light, time of day and scale of key objects in the prompt of every shot of a multi-shot: a jump between shots is a typical defect.** Seen: shot 1 in a black stormy night, shot 2 suddenly day; a bear that "abruptly scales up" between shots; an exoskeleton that turns into a separate bigger mech; a structure that changes geometry. Relates to 06.18 and 06.39.

06.68 **Hide a transformation or a scale change behind a strong event in frame:** a flash, lightning, fire, smoke, an energy burst. Lightning acted as a high-exposure flash covering a morph between a man and a giant; explosions of flame and smoke covered transitions between ground and air. Relates to 06.56.

06.69 **Add text, plates, HUD, prices and brand names in ads in post:** letters the model draws turn to garbage. Seen: HUD with pseudo-characters, a pizza box printed "DREE ZA", a logo on a sole that is garbled, unreadable captions. The main title composited cleanly in post looked fine. Relates to 06.38, 06.54 and stage 08.

06.70 **Check first the places where artifacts repeat in almost every example:** (a) fingers and objects in hands; (b) feet "slide" on the ground with no friction; (c) force contact and fast impacts (a paw hits flowers while a glass vase stays still, face and paw smear); (d) liquids and cloth that look like gel; (e) unreadable text (06.69).

06.71 **Structure of an ad from the examples:** the hero product in the first and last frame; a character with a parameter card near the start; a macro insert of the product; the slogan spoken at least twice; a logo or site address at the end. This is an observation from examples.

06.72 **A multi-shot scene follows the film language "establishing, close-up, detail insert, reaction, wide result" and shows causal successive states.** One scene kept an asset and environment consistent across five distinct cuts: a cat on a table (wide), profile close-up, a macro insert of a petal with an ant, the cat's reaction, a wide finish. A barber scene showed overgrown client, haircut, shave, hot towel, clean client, and the pile of hair on the floor matched the end. Relates to 06.22 and 06.29.

06.73 **Join worlds or states by a match of movement or sound (match cut).** A boot touches the floor and match-cuts into a hydraulic mech leg; a bear's paw falling acts as an edit trigger for a whip transition into a room, a voice off-screen and a sudden muted room sound finish the transition, and the heroine's face stays the same in both worlds. Relates to 06.25.

### K. The lesson that fixed the method

06.74 **Do not generate every shot as a separate short clip from its start frame only, with no previz and free-text prompts.** This was tried, and it failed. Gags do not work: cars do not brake, people do not turn, hits do not land. The cut looks like a slideshow of unrelated pictures. The fix is the method of this stage: the previz as `@Video1` for camera, positions, paths and timing, written roles for every image, the JSON prompt with camera and acting in every shot, batches of 10-15 s. Do not swap the model or skip the previz to save credits. A cheaper model without the previz costs more in the end, because every failed gag is paid for and still unusable.

## Workflow

The Seedance 2.5 path. Other models follow the same steps, with their own template.

1. **Check the input.** Roles of the files, frame format, a storyboard with angle, lens, movement, who does what, sound. A start frame per scene (stage 04) and a previz montage (stage 05). If there is no previz and the camera matters, go back and make one (06.13). Do not start from start frames alone (06.74).
2. **Choose the input mode (the switch):**
   - text only (text to video): no image, describe the scene completely like a photo prompt, include all blocks;
   - one image (image to video): the scene is in the frame, "Scene" holds only anchors, the focus is camera and movement;
   - two frames, start and end: describe how the first becomes the second;
   - several images (multi-reference): the "Inputs" block is the main one and each image gets a role.
   For the main method the mode is omni reference: `start_image`, `image_references`, `video_references` (the previz), and optionally `audio_references`. If the host rejects a start frame together with a video reference, pass the start frame as an image reference and name it in the prompt (`@Image1 is the first frame, keep its look, people and faces`).
3. **Choose the model.** Default `seedance_2_5`. Use 06.63 for other cases. Run `models_explore` to confirm the current ids and limits, and open the matching template.
4. **Upload the files.** Use `media_upload` for the previz video, frames and cards. Keep a table "tag, file, role, what we take, what we do NOT take". The previz role line is: `@Video1` gives only camera movement, positions, paths and timing, never looks, faces or hands (`templates/previz-in-video-prompt.md`). Every image has a written role (06.4, 06.5).
5. **Write the prompt.** Ask the agent for the Chinese JSON from `templates/video-prompt-seedance.md`. For every shot: camera (机位) first, then picture (画面), then acting (表演) written through the body (06.11, 06.17), integer-second timecodes with no gaps (06.23), sound inside the shot (06.30), lines verbatim in quotes (06.31), a short concrete negative (06.36). Keep it to 5000 characters at most. Split into batches of 10-15 s (06.27) and cut a longer video at natural seams with `@video1` continuation (06.26).
6. **Check the prompt.** Run `python scripts/check_prompt.py <prompt.json>`. Fix every error it reports and read the Chinese text yourself, because a typo in a character is not caught (06.43).
7. **Show the user the price message.** Model, mode, frame format, length, resolution (480p draft), with or without sound, the files and roles, the number of jobs and the credits from `estimate_video_cost`, the prompt, and the "Check before ok" list with yes/no per item. Name any move that is not the method (for example "no previz" or "another model") as a deviation. Wait for the user's "yes" for this exact run. (user's ok)
8. **Generate the draft.** 480p batches via `generate_video` (`generate_video_batch` for several), then `jobs_wait`. Drafts only, no 720p or 1080p yet (06.47).
9. **Check against the previz.** Make a frame grid of the draft and put it side by side with a frame grid of the previz. Compare the start, middle and end of every shot: camera direction, object placement, order of foreground things passing, face drift, room drift, scale drift. Check hands, feet, text and cuts (06.52, 06.65, 06.70). Listen to the track (06.66).
10. **Regenerate only the bad shots (06.49).** Fix the prompt in place in `prompts.md` and regenerate the batch with the fix, collecting all edits in one message (06.50). If the same shot fails twice, fix the previz, not the prompt. Save the accepted version together with its references.
11. **Finish at the end.** Finish accepted drafts or run the upscale pass (`bytedance_video_upscale`, `topaz_video` or a local upscaler), one clip at a time, before grain and grade (06.53). Price check and "yes" again before paid upscale. (user's ok)
12. **Save and log.** Clips in `video/`, rejects in `drafts/`, prompts in `prompts.md`. The user watches and gives the stage "ok". (user's ok)

Homework to practise: take a photo, start with one frame in image to video, go through the formula block by block, and when it works add a second and third shot with timecodes.

## Formulas

The formula, in order: 1 Inputs; 2 Scene and anchors; 3 Camera movement; 4 Object movement and order; 5 Sound and dialogue; 6 optionally environment and negative.

Block examples:
- Inputs: "Image 1 is the start frame. Image 2 is the character, keep the face."
- Anchors: "Keep the inscription on the label."
- Camera: "Slow push-in, handheld with no stabilization."
- Object and order: "First the cat turns its head to the rose, then half-closes its eyes. By seconds: 1-3 s the cat jumps onto the table gracefully; 3-5 s the cat sniffs the rose and closes its eyes."
- Sound and dialogue: "Sound: a quiet room, the rustle of petals. A woman says in an irritated voice: 'You jumped on the table again?!'"

Seedance 2.5 JSON skeleton (the full field list is in `templates/video-prompt-seedance.md`; copy the field names from there, do not invent them): global fields (inputs and roles, style, sound), then one block per shot with timecode, camera (机位), picture (画面), acting (表演) and sound, then the negative. The previz line, in Chinese: `@Video1 只提供镜头运动、人物位置、路线和时间，不提供人物外貌、表情和手部动作`.

Our own multi-shot example in English, for the shape of a shot (not a Seedance JSON):
```
@Image1 is the character reference: keep the exact coat and face in every shot, no face drift.
[0s-2s] WIDE SHOT. The cat walks to the rose and touches a petal with its nose. Camera static, eye level, wide lens. Backlight rims the fur.
[2s-4s] CLOSE-UP on the face. One slow deep inhale, eyes closing, whiskers forward. Camera static, 85mm look, shallow depth of field.
[4s-6s] WIDE SHOT. The cat hisses at the rose, swats it, petals scatter into the sunbeam.
AUDIO per shot: room tone, petal rustle, a short hiss at the end. No music.
Avoid jitter, bent limbs, face drift.
```
Checklist of the lesson before launch: roles of all inputs written; the scene is not re-described, only movement and anchors; one shot, one action, one camera move; dialogue verbatim, in quotes, with the language.

Shot structure for ads (four elements): action, camera, physics, audio. Ad style parameters that change: background, typography, graphics, energy. A European ad uses a warm orange background, bold commercial text and a motion-graphics overlay. A K-pop or manga style uses a pure black background, explosive comic typography with speed lines, and comic burst stickers.

Task patterns, copy as templates:
- motion transfer: `use the motion from the video in @video_1 for the character in @<id>. Use the image @image_2 as a location reference.` and `@video_1, mirror motion timing exactly`;
- adding to a video: `Add to this video @video_1 plants and flowers slowly creep out...`;
- one continuous shot: `FORMAT: 15s / single continuous camera move / no dialogue`, `One unbroken continuous tracking shot. No cuts. All real time.`;
- match cut: `FORMAT: 15s / free rhythm / 1 MATCH CUT / continuous move until match cut, immediate action from first frame.`;
- 15 s sequences with reference cards of the hero, armour, location and details.

Morphing: first frame, second frame and one of ten action prompts (liquid, particles, energy wave, surface peel, freeze and shatter, time reversal, light construct, material evolution, flow through itself, micro-detail morph). Each prompt must say how the change happens, set the physics, and keep the object's volume, form and logic. The ten prompts are in `templates/video-prompt-other-models.md`.

## Check before "ok"

- [ ] The method is followed: previz as `@Video1` (camera, positions, paths and timing only), a role for every image, the Chinese JSON, drafts at 480p. If any item differs, it is named to the user as a deviation, not hidden.
- [ ] The roles of all inputs are written (what we take, what we do not take).
- [ ] The camera is set in every shot, the angle comes first, and shake or stabilisation is named.
- [ ] One shot, one action, one camera move; timecodes in whole seconds run back to back with no gaps and cover the whole running time.
- [ ] Acting by body and face for every character in every shot; a hero with an image appears in every span.
- [ ] Physics is named; any effect is described materially (not "magic").
- [ ] Dialogue verbatim, in quotes, with the language, in its own shot; sound inside the shot, not in one line at the end; music not ordered unless asked.
- [ ] Positive descriptions instead of bans; the negative only specific (or by the model's rule).
- [ ] The character limit counted by code (at most 5000 for Seedance 2.5); the prompt is whole; no signature, brands or instruction words for the model; `scripts/check_prompt.py` was run and passed.
- [ ] The price message listed model, mode, format, length, resolution, price, prompt, and the user's "ok" is for this run.
- [ ] The 480p draft was viewed on a frame grid side by side with the previz (style, direction of movement, faces, hands, text), and only the bad shots were regenerated.
- [ ] Upscale is done at the end and before effects; clips and `prompts.md` are in the project; rejects are in `drafts/`.
- [ ] Sound was not checked by ear unless it was listened to, and that is stated honestly.

The stage closes only with the user's "ok".

## Common mistakes

What the lessons call mistakes:
- Writing a video prompt like a photo prompt; learning a separate prompt for every network ("endless, and you still fall behind").
- Skipping the camera: you get a random one. Several actions in a shot: flicker.
- Not writing input roles: a mush. Not splitting a multi-shot by timecodes: the model rushes the ending.
- Re-describing a scene that a photo shows (only anchors are needed).
- Seedance 2.0 with prompts in a language it does not read well (English or Chinese needed).
- Audio in one line at the end: ignored. Physics not named: it does not appear. "Motion graphics" in place of concrete terms: a weak result.
- Negative wording instead of positive (`no blur` instead of `sharp focus`).
- Magic without a physical description: coloured powder or fog. Two heroes shooting the same element: needs an ELEMENT LOCK. A transformation as a teleport: needs phases. Ice as cartoon cubes (use `solid crystalline ice, jagged translucent`).
- A signature or studio name in the body of the prompt: the model draws the text in frame.
- Giving storyboard frames to the video model.
- Generating straight in 1080p with no draft: only a draft can be finished to 1080p.
- Not regenerating slips ("people walked backwards") and letting rejects into the cut.
- A reference video with zoom and shake (Motion Control); a character in the photo at another angle and distance than in the video.
- A video longer than the clip limit in one piece; transitions with no description: "hard cuts and jumps".
- Not upscaling: photo to video loses 15-20 percent.
- A voice in the generation together with the 3D previz: overload.
- Feeding moodboard images straight as a reference: the image model may take even someone else's face.
- Observed in examples: one continuous shot requested but hard cuts received; a light jump between shots (night, then day); flickering hands and fingers on fast moves; unreadable text on the ground; weak lip sync on a short line; scale shift between shots; a lightning flash covering a morph cut; small non-physics (hair and a towel hanging in the air).
- **Generating each shot as a separate short clip from its start frame, with no previz and free-text prompts (06.74).**
- Swapping the model or skipping the previz to save credits.

## Tools

Always check `models_explore` for current models and `estimate_video_cost` for the price in credits before any paid run. Never rely on a remembered price. Check `balance` before a long batch.

| Tool | Role in this stage |
|---|---|
| `seedance_2_5` (omni reference) | Main model. Inputs: `start_image`, `image_references`, `video_references` (the previz), `audio_references`. 5000 characters in the Chinese JSON, up to 30 s per pass, many references (practice about 25), drafts at 480p. Realistic scenes, multi-shot, dialogue. May reject reference images of real human faces: test one cheap generation with the user's own face before relying on it, and if it fails, use a stylised face or Kling for those shots. |
| `seedance_2_5_flash` | Faster, cheaper tests of a prompt or a previz. |
| `kling4_0` | Faces in shot, Omni Reference, previz as a white-model video, edits via `Edit @Video1`. 3-30 s, up to 10 images, 5 videos, 7 elements, 3 voices, at most 15 files. Does not support Russian speech in frame, so put a recorded voice on top. Its own `check_prompt.py`. Motion Control via the `motion_control` tool. |
| `minimax_h3` | Launch videos and motion design with text on screen, reference-based videos. 4-15 s, up to 2K. Sound is untested: do not rely on it, add sound in the edit. |
| `wan2_6` | An alternative, mostly for tests. |
| `cinematic_studio_3_0` | Cinematic generation, check its inputs in `models_explore`. |
| `generate_video`, `generate_video_batch`, `jobs_wait` | Run and wait for generations. |
| `media_upload` | Upload the previz, frames and cards. |
| `upscale_video`, `bytedance_video_upscale`, `topaz_video` (paid) or a local upscaler | The final upscale. |
| `motion_control` | Kling Motion Control (the video sets how, the prompt sets what). |
| Claude (the agent) | Writes the prompt from the formula, translates to Chinese, counts characters, runs `scripts/check_prompt.py`. |
| ffmpeg | Frame grids (contact sheets) for the check, resizing a previz. |
| Blender | The previz (stage 05, `.claude/skills/blender-previz/SKILL.md`). |
| `docs/higgsfield.md` | Higgsfield notes. |
