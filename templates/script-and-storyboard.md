# Script and storyboard

Fill-in prompts and structures that take an approved idea to a script, a storyboard and director notes, ready for the frame and video stages. The agent can run each "role" itself in one chat, or paste the role prompt into a separate chat model project.

Used at stage 01 (`docs/stages/01-preproduction.md`), with the film vocabulary from `templates/film-language.md`. Hooks are in `templates/hooks.md`. The idea itself comes from `templates/idea-toolkit.md`.

## Order of work

1. Script (what is said and the idea of each beat).
2. Storyboard (what is seen, by time).
3. Director notes (light, color, pace, performance, prompt per scene).
4. Optional: a 3x3 board image or per-second shot sheet before any paid video run.
5. The user says "ok" on each document before the next one starts.

The writer role writes only the words and the idea. The storyboard role works strictly from the approved script and invents no extra scenes.

## Script: the five blocks

Every talking or voice-over script for a short vertical video has five blocks. Default length is 30-60 seconds unless the user says otherwise.

1. Hook (0-3 s). The first strike. The viewer decides here.
2. Amplify (3-15 s). Open the problem or build curiosity. The viewer should feel the pain or want to know.
3. Key point (15-35 s). The value: an insight, a trick, a demonstration of the result.
4. Takeaway (35-45 s). A sentence that stays in the head.
5. Call to action (45-60 s). One concrete action. Not "like and subscribe".

A good hook is one of two types:

- Personal story with specifics and a gap. First person, concrete numbers (days, sums, hours, people), an open question that pulls the viewer forward.
- Provocative claim. Sharp, disputable, hits a pain or breaks a myth, needs no "I", works through the reaction "really??".

Nine hook formulas (pick one per task):

1. Experiment: "I tried [tool/trend] for [period]. Here is what happened."
2. Life hack: "This [X]-second trick gives [result] almost instantly."
3. Insider: "Nobody says that [A] + [B] = [unexpected result]."
4. Pain to fix: "For [X] months I suffered from [pain]. Three things changed everything."
5. Myth: "[Belief] is a lie. Here is what works."
6. From zero: "If I started from zero, here is what I would do differently."
7. Income or result: "I earned/saved [amount] with [unusual method]. Here is how." (real numbers only)
8. Secret: "Everyone talks about [trend], but nobody shares this."
9. Counter-position: "Most people do X. I do Y. The difference is [result]."

Turn any topic from "advice" into "a story with conflict and specifics". Example: "tips for saving time" becomes "I lost 11 hours a week to one chore. I found it in an afternoon."

Each video should trigger one reaction: "how did she do that?", "I need this", "I will send it to a friend", "I will save it", "I will follow".

Amplify tricks: show the scale ("this used to need a crew and a budget"), show the process (what I do, what I get), a mini-story with details, list what fails before the solution.
Key point tricks: demonstrate the result on screen, give step 1-2-3, show before/after in real time, use the channel's signature visual device.
Takeaway tricks: one-line result ("you no longer need [old solution] for [task]"), a strong claim, or one thought about what it means for the audience.
Call-to-action options: "Save this, more tricks next time", "Want the same? [where to go]", "Comment '[word]' and I send [what]", "Which is better, 1 or 2? Comment", "Follow if you want [result]", a teaser for the next video.

Video types: result "wow", follow-along tutorial, before/after, myth-breaker, behind the scenes, pain to solution, trend plus topic, provocation.

Before writing, confirm three things with the user: the topic or idea, the goal (reach, engagement, warm-up, sale), the selling level (pure content, soft warm-up, direct offer). If only a topic is given, offer 3 angles.

### Output format for a script

```
VIDEO: [title]
LENGTH: [approx]
GOAL: [reach / engagement / warm-up / sale]
IDEA IN ONE SENTENCE: [...]

[HOOK] 0-3 s
Voice: "..."
[AMPLIFY] 3-15 s
Voice: "..."
[KEY POINT] 15-35 s
Voice: "..."
[TAKEAWAY] 35-45 s
Voice: "..."
[CTA] 45-60 s
Voice: "..."
```

### Writer role prompt (fill in, paste into a chat model)

```
You write scripts for short vertical videos (Reels, Shorts, TikTok) for [channel name].

Channel: [name and topic]
Product: [what is sold, to whom, the main promised change]
Host: [name, character, how they speak, tone: friend / expert / mentor / provocateur]
Audience: [who, their pains, their wishes, their level]
Promise of the product: [main result the buyer gets]
Proof: [real numbers, real reviews only, or "none yet"]
Entry points: [comment word / link / direct message]

Voice examples (4 real lines in the host's style):
- "[line]"
- "[line]"
- "[line]"
- "[line]"
Rhythm: [short chopped lines / long explanations / storytelling / humor / provocation]

Rules: the first 1-2 seconds decide everything. Write only what the host says and the idea
of the video; a separate storyboard role handles visuals. Use the five blocks: hook,
amplify, key point, takeaway, call to action. Default length 30-60 seconds.
If details are missing, ask: topic, goal, selling level. If only a topic is given,
propose 3 angles. Never invent numbers, reviews or names.
Output in the format above.
```

If the user has good past videos, transcribe them first and load them as style samples. Transcription prompt for a video model:

```
Transcribe this video. Write down word for word everything the host says.
Keep the structure: hook, amplify, main part, takeaway, call to action.
```

Instruction for the writer project once samples are loaded: "The files contain sample scripts in the right style. Study voice, rhythm, structure and sentence length. Write all new scripts exactly in this style."

## Storyboard role

A storyboard is detailed enough that the video can be shot or generated from it with no further explanation.

For every scene give:

- Timing: an exact interval (for example 0-3 s).
- Composition: subject (host, product, screen, detail), position in frame (center, left edge, close-up of the face, waist up, full body), background (neutral, interior, street, generated), important details.
- Camera movement: static, slow push-in, pull-back, pan left/right, handheld, drone if it fits.
- Movement in frame: what the host does (gesture, look at camera, turn, step), text animation, graphics, transitions.
- Visual effect if needed: AI transformation of background or objects, overlay, morph, appearing elements, transition type (cut, soft, visual trick).
- Atmosphere in one word or phrase (energetic, intimate, surprising, businesslike, playful).

### Storyboard role prompt

```
You write storyboards for short vertical videos (9:16) for [channel name].

Host look and energy: [description]
Signature visual style: [colors, mood, devices]
Platform: [Instagram Reels / TikTok / Shorts]
Production: [shot live or generated by AI]

Take the approved script and produce a frame-by-frame storyboard. Think about a vertical
phone screen, because horizontal compositions do not work. The first 3 seconds must catch
the eye with no sound. Keep the signature style in every frame. Do not add scenes that
are not in the script. If a scene is generated, add a ready prompt for [video model].

Output one table per scene:
| Timing | Composition | Camera | Action | Effect | Atmosphere |
then a short director comment: what to watch for when shooting or generating this scene.
If no script is provided, ask for it. Ask whether it is live or generated, whether visual
references exist, and whether a prompt is needed for each scene.
```

## Director role

Gives exact notes that can go to a camera operator or straight into a generation prompt. Every note is concrete: not "beautiful", but "warm side light, golden hour, soft shadows".

For each scene:

```
SCENE [no.] | [timing]
Light: source (natural / studio / mixed), direction (front / side / back), character (soft / hard), temperature (warm / cool / neutral), special effects.
Color: palette, saturation (rich / muted / desaturated), mood through color.
Atmosphere: energy (fast / meditative / tense / playful), cut rhythm (fast cuts / smooth transitions / one long shot), music mood (no track names).
Host: body and gestures, eye direction (camera / aside / object), speech tempo, emotion, one specific gesture if it matters.
AI prompt (if generated): the ready prompt, camera settings, reference.
```

After all scenes add overall notes: what must stay the same through the whole video. If something in the storyboard does not work as direction, say so and propose a replacement. Always check how the first 3 seconds look on a phone with no sound.

## Analyst role (stage 10)

After publishing, an analyst chat reads the statistics export and a list of videos with topics and dates. It reports only from numbers and states hypotheses; one viral video is not a trend.

```
You analyze short-video statistics for [channel]. Platform: [...]. Goal: [reach / sales / growth].
Metrics: views, reach, share of non-followers, shares and sends, average watch percentage,
where viewers leave, replays, likes / comments / saves per view, profile visits, new followers
and view-to-follow conversion.
Look for patterns in topics, formats (tutorial / story / provocation / before-after),
hooks, length, publishing time and the last month's trend.
Output: top videos of the period (title, views, watch %, followers, why it worked),
what works with numbers, what does not with numbers, 3-5 hypotheses in the form
"If we do [X], we expect [Y], because [Z]", and the top 3 actions for next week
(a specific format, topic and hook type, not "make interesting content").
If data is missing, say what to collect. Priority metrics: for reach, views and shares;
for sales, profile visits and follow conversion.
```

## Scene expander: one line into a full scene (6 layers)

Use at stage 01 or 04 when a storyboard row is too thin. Every scene needs all six layers. A missing layer gives flat, generic results.

1. Subject and action. Who or what is in frame and what they do. Be specific ("sitting with legs crossed, looking out the window", not "sitting"). Add small gestures ("one hand around a coffee cup"). With no character, describe an anchor object.
2. Environment. Type (interior, exterior, urban, nature, studio), a specific place ("corner table of a small cafe, marble counter, vintage espresso machine behind"), time of day (morning, golden hour, midday, blue hour, night), weather for exteriors.
3. Light. The most important layer. Source (window, overhead, practical lamp, neon, sun, candle, studio), direction (left, behind, overhead, below), quality (soft and diffused, hard and directional, warm, cool, flickering), and what it does to the subject.
4. Atmosphere and texture. The air (hazy, crisp, steamy, dusty, foggy), implied background activity, visible textures (worn wood, cold concrete, soft linen, wet pavement), color temperature.
5. Camera. Shot size, lens (24 wide, 35 natural, 50 standard, 85 flattering and compressed), angle, movement, depth of field.
6. Mood summary. Two or three words that unify the layers ("quiet and intimate", "tense and raw", "cold and editorial").

Rules:

- More specific is better. "A cafe in Paris" becomes "corner table, small brasserie, black-and-white tiled floor, frosted windows letting in grey morning light".
- Light logic must be consistent. If it is golden hour outside, an interior near the window gets warm side light, not overhead fluorescent.
- Atmosphere implies sound. Think about what you would hear.
- Do not add everything. Ten competing elements confuse the model. One strong atmosphere beats five weak details.
- Always offer two alternatives after the main scene: A with a different time of day or light, B with a different camera angle or shot.

Example, input "a woman in a cafe in the morning":

```
[CHARACTER] sitting at a small corner table in a brasserie, one hand around a ceramic cup,
looking out the window with a slight smile, relaxed posture. Black-and-white tiled floor,
round marble table, vintage espresso machine behind the counter, patrons softly blurred.
Soft grey morning light from large frosted windows on the left, diffused, no harsh shadows,
a slight warm glow from a pendant lamp. Steam rising from the cup.
Medium shot, 50mm lens, eye level, static with a slight handheld drift, shallow depth of field.
Shot on 35mm film, natural grain, photorealistic. Preserve face identity.
Mood: quiet, intimate, nostalgic.
```

Variant A: same scene in the evening, warm candle light, dark window. Variant B: same scene from overhead, cup and hands in close-up.

## Context first: the three-act script block

A video model should understand the story before it executes shots. Put a SCRIPT block first in any story prompt: genre, stakes, the characters' motivation, what this is not, and where the video sits in the story. The storyboard only guides after that. Without it, the model draws every frame literally and disconnected.

Write the script in three acts with place, time and lines:

```
SCRIPT
Act 1. Setup
[Place, time of day.] [What the hero does in a relaxed state.] [The event that breaks it.]
HERO: "[first line]"
Act 2. Development
[The disruption grows. A new threat appears.]
HERO: "[reaction line]"
Act 3. Resolution
[The hero's decisive action. The final held pose before the clash.]
```

Short example of our own:

```
SCRIPT
Act 1. Setup
A rainy night in a laundromat. Mia folds towels, headphones on, calm.
A dryer starts to glow orange. She takes one earbud out.
MIA: "That is not a normal cycle."
Act 2. Development
The dryer door bursts open. A cloud of warm steam fills the room and a pair of mismatched socks rises in it like a swarm.
MIA: "No. Not again."
Act 3. Resolution
Mia pulls a laundry basket over her arm like a shield and a coat hanger from her pocket like a sword.
The socks hover. She plants her feet. Both sides hold still before the first move.
```

## 3x3 board before a paid video run

A single 16:9 image with nine frames (a 3x3 grid), each labeled with time and caption, lets the user approve the look before video credits are spent. Generate it with an image model (`nano_banana_pro`), pass real screenshots, logo or character references as image references, and check the cost with `estimate_image_cost` first.

For a model that takes a long structured prompt (for example `minimax_h3`), build the video prompt in six parts:

1. Format first line: duration, aspect ratio, style.
2. Palette in hex and the role of each color.
3. The main object and one distinguishing detail. The model keeps the product identical across scenes by this detail.
4. Text: font, how it appears and leaves, which word is color-highlighted.
5. A storyboard by time slices (for example 0.0-1.6 s, 1.6-3.2 s). Fractions are fine for this model only. For Seedance use whole seconds.
6. A verbatim list of every on-screen text and the line "nothing else is written in frame". That line stops text from drifting.

Launch video from a website, fill-in prompt for the agent:

```
Make a launch video for [product], site: [link]. Logo: [file]. Project folder: [folder].
1. Read the site: what the product does, the 3 main benefits, who it is for.
2. Capture the brand: colors (hex), fonts, illustration and interface style. Save screenshots
   of the home page and 2-3 key screens as references. Show me benefits, palette and fonts briefly.
3. Write a 15-second script: hook, 3 benefits, final with logo and call to action.
   Short captions in [language].
4. Make a storyboard: one 16:9 image, 3x3 grid, 9 frames, time and caption under each.
   Strictly in the site's style: its colors, fonts, real product screens. Pass the screenshots
   and logo as references. Invent nothing beyond the site. Estimate the credits and wait for my ok.
5. After my ok: write the video prompt and generate: 15 seconds, 16:9. Pass the storyboard,
   screenshots and logo as references. State the credits used.
6. Save the video in the project folder and show it to me.
```

Repeat a reference video:

```
The file [reference.mp4] is a video to repeat.
1. Break it down into a scene table: time, what is in frame, on-screen text, how it appears
   and leaves, transitions, tempo, palette in hex.
2. Write the video prompt with the same structure, tempo and devices, but our product,
   texts and colors: [client or user data].
3. Generate with the reference passed as a video reference. Same length and format as the original.
4. Put the original and the result side by side and compare honestly: what matched, what did not.
```

## 9-frame board of a location and of a model in a location

Used at stage 04 to get a coverage set from one look.

Step 1, the location prompt (give a short, concrete description first):

```
Private black-tie cocktail reception in a wood-paneled European salon, warm candlelight sconces,
crystal chandelier, wall tapestry, antique furniture, night city lights through an arched window,
champagne glasses, elegant crowd
```

Step 2, ask for the board:

```
Make a director's storyboard of 9 frames of this party. It is a society evening reception
in an old European mansion with a large terrace, quiet old-money aesthetic: warm light, wood,
crystal, no rush. Photorealism like the reference photo.
```

Step 3, if a frame is weak: "Make this image detailed and high quality."

Step 4, the model in the location. Attach 6 location frames and 4 photos of the model. Run 4 generations of 9 frames each:

```
Attached are 6 photos of the location (a society party in a mansion with a large terrace,
old-money aesthetic: warm light, wood, crystal) and 4 photos of the model in a red dress.
Make a 9-frame board where the woman in red takes a selfie with guests, films herself in
a mirror and hangs out at the party.
```

Step 5, if the face drifts on a board frame (give the frame screenshot and all model photos):

```
Make the first image high quality, visible skin texture, high detail. Replace the face of the
woman in red with the face from the reference photos.
```

Step 6, a missing frame (model photo plus location photo): `Medium shot of the woman in red walking along the terrace and holding the railing.`

Each generation costs credits. List the number of runs and wait for the user's "yes" (see `AGENTS.md`).

## Per-second storyboard for a one-take video

Use when the video is one continuous shot with several events and a spoken line. Ask the agent for a second-by-second brief. Fill this prompt with a reference video if one exists.

```
In this folder there is a reference video: [what happens in it]. Watch it.
Make a director's storyboard of my video using the film-language template.

Idea. [Starting position of the camera and set. What happens at normal speed. The moment of impact
and the switch to slow motion. Where the camera travels, as a path. Who speaks which line and
where. The return to normal speed. The final action and the final shot.]

Format: [aspect ratio], one continuous shot, [N] seconds, smooth camera, no shake.
Split into beats by whole seconds: what is in frame, the camera path, the speed
(slow motion or normal), and the spoken line. Add a SCRIPT block, the light and the film look.
Save as a file "brief.md" in the project folder.
```

Check before "ok":

1. Time is in whole seconds everywhere. Seedance does not understand fractions.
2. It is clear where slow motion and normal speed are and when the switch happens.
3. The spoken line stands in the exact seconds where it is spoken.

Add the one-take rules from `templates/film-language.md` (substitutes for cuts every 8-10 seconds, camera path not two points, frame only narrows).
