# 04 Frames (image generation)

This stage makes every still image of the project: reference cards, the start frame of each scene, storyboard frames, product and fashion shots, infographics. It is the "production" half of the work. Nothing is invented here: everything was decided earlier, and this stage executes it. The one tool that steers an image model is the prompt, so most of this file is about writing prompts that leave nothing to the model's average taste. Principles do not depend on a model. Model-specific limits are in "Tools" and in `templates/image-prompts.md`.

## Input and output

Input (must already be in the project folder):
- `brief.md`, `idea.md`, `script.md`: what the video is and why.
- `moodboard.md`: the best frames in the topic, with the light, composition and mood to borrow. Details come from the moodboard, not from memory.
- `storyboard.md`: the piece of the storyboard for the frame in question (what is in shot, lens, light, camera move). It is one of the four inputs the agent needs (principle 04.12).
- `refs/`: 3-5 photos of each face from different angles, clothes and accessories without the model's head, the product, the location, style references.
- The user's "yes" for every paid generation (see the money rule in `AGENTS.md`).

Output:
- `frames/`: reference cards (character, objects, location), one start frame per scene, storyboard frames, accepted frames after upscale. An accepted frame is saved right after generation.
- `prompts.md`: one file with every image prompt. Edits are written in place and versions are kept (principle 04.17).
- A note in `prompts.md` for each accepted frame: which model and which prompt made it.

## Principles

### A. Formula and length

04.1 **Every photo prompt follows one six-part formula in a fixed order: subject, location, action, angle and camera, light, effects and styling.** A short prompt gives grey results because the model averages everything it knows about the topic. Fill each part with specific meaning, never with "average".

04.2 **The model does not pull the best picture from a library, it averages, so fill the space: describe every element.** "Beautiful cat" returns the mean of all cats. Treat the prompt as a brief for a photographer: whatever you do not name, the model decides for you.

04.3 **Camera angle and light decide a frame more than anything else.** A good angle and a named light turn an average photo into a real shot. "Cinematic" is about 90 percent light and 10 percent film grain. Terms for angle and light come from stage 02 (`docs/stages/02-film-language.md`, `templates/film-language.md`).

04.4 **Name the lens, the aperture and the light in the prompt.** Without a lens the model picks the average one. Light shapes mood, volume and where the eye goes. The reference tables live in stage 02.

04.5 **End the prompt with a priority block: if style conflicts with realism, realism wins; if lighting conflicts with identity, identity wins.** Styling must not kill believability.

04.6 **Take details from real samples (the moodboard), do not invent them.** Look at the best frames in your topic, find what works in them (light, composition, mood), then describe that. For handheld feel and imperfections, analyse real videos from the moodboard.

04.7 **Prompt length equals the number of decisions you hand to the model.** Photo prompts for a complex frame run roughly 2000-3000 characters. Product shot or portrait: 1200-2000. A single-detail edit: 200-600. A simple mechanical change: 1-3 sentences. If a decision is already made (a reference exists, one detail changes), extra text only gets in the way. Length is per model and per task, there is no single number. Nano Banana and GPT Image take long prompts. Very long prompts (above about 4500 characters for GPT Image) start to lose details from the middle.

04.8 **Use dense visual facts instead of adjectives.** "Stunning cinematic masterpiece" gives the model nothing. Banned filler: stunning, epic, masterpiece, incredible, ultra-detailed, gorgeous, 8K, award-winning. Replace each with a visible fact. Suggested block sizes for a long GPT Image prompt, in characters: subject 250-450, location 350-550, action 200-350, angle and camera 200-350, light 250-400, effects 250-400, constraints 150-250. Nano Banana: no quality boosters (4k, trending on artstation), they are noise.

04.9 **Practice drill: build a prompt one part at a time, change one thing per step, then put six frames side by side.** Order: subject only, then +location, +action, +angle, +light, +effects. If you change several parts at once you cannot see which part moved the picture.

04.10 **The shape of a prompt depends on the model.** Nano Banana and GPT Image accept long prompts. Nano Banana wants natural full sentences, no tag soup, no negative prompts. GPT Image takes long structured text and an explicit constraints block. Some external models (for example Midjourney, which has no Higgsfield integration) want 20-60 words, English, subject first. Check the model note before writing.

### B. The agent writes the prompts

04.11 **Prompts of two or three thousand characters are not written by hand: the agent writes them, using a model note for the target model.** Without a note the agent produces something generic and averaged, and it may not know the newest models. A model note is a short document: the formula, the recommended length, the hard limit, known quirks. Add to it whenever you find a new trick. Higgsfield models change often, so the agent checks `models_explore` first.

04.12 **Give the agent four things per frame: all references, the idea and script, the storyboard piece for this frame, and how the assembly works** ("I am generating the start frame of scene 3; these two cards go in as references; the output must be a clean still with no text"). The last item is skipped most often and matters most. The agent cannot see your screen, so without it the prompt is written in a vacuum.

04.13 **When a prompt does not work, there are three kinds of follow-up:** name what is wrong, point by point (angle, shot size, object in the background, blur); give a new reference and have the prompt rewritten whole; or edit over the frame while forbidding changes to everything else. The first try almost never works. If edits do not help, the model simply does not see the needed object: make a reference card and rewrite the prompt instead of patching the old one.

### C. Iterations and edits

04.14 **Improve a frame by iterating the source prompt, not by repeatedly re-editing the finished image.** Repeated re-editing in Nano Banana eats quality and it is hard to get it back. If you forgot something or want a change, change the original prompt and generate again. Resolution of the "edit the frame or edit the prompt" question: wide changes early on mean editing the source prompt and regenerating; one detail on a nearly finished frame means an edit on top of it; after 4-5 edits start again from a reference. A reference card is only ever rebuilt by a fresh generation from the original sources.

04.15 **Golden rule: spend the time on a detailed prompt up front instead of repairing the result.** Commands like "change the face" give bad results. Order of work: base prompt, 4 images, review what you like and what you do not, find gaps (forgotten accessories, makeup), go back to the source prompt and add them, regenerate, and only then fix age, height and weight.

04.16 **In a series of frames, change one variable at a time: the SHOT line. Everything else stays fixed.** Fixed: face and outfit references, outfit description, makeup, lighting. Process: copy the base prompt, change SHOT, generate 4-8 variants, keep the best, move to the next angle. IDENTITY LOCK and OUTFIT LOCK blocks pin the face and the clothes.

04.17 **Keep all prompt versions in one document.** `prompts.md` holds every prompt of the project. Edits rewrite a prompt in place, new files are not created.

04.18 **Write every point edit in two parts: what to change (one thing) and what to keep (everything else). Repeat the keep list in every edit of a series.** A bare edit without a keep list is the main cause of drift. The model changes whatever you did not forbid. Edit template:
```
CHANGE: exactly one change.
KEEP: face and identity, pose, lighting, framing, background, object geometry, text, composition, shadows, reflections.
INTEGRATION: how the new element must match light, perspective, scale and shadows of the scene.
CONSTRAINTS: no new objects, no redesign, no logo drift, no watermarks.
```

04.19 **When replacing a character inside a frame, assign the roles explicitly: the "canvas" (background, pose, light) and the "donor" (look, clothes).** Formula: action command, new character, link to the surroundings, keep the style. If the insert looks pasted in, add a Seamless integration block at the end (light, colour temperature, contact and cast shadows, lens, depth of field, grain). A structured prompt stops the model from repainting the whole image.

04.20 **When a style comes from a reference, break it into seven parts (light, palette, camera and lens, texture and grain, composition, mood, styling) and put the style block after the character and scene description.** Identity block comes first: never let style override character identity. Change one detail at a time when iterating.

### D. References and consistency

04.21 **Give every reference a role: what to take and what NOT to take.** A picture is stronger than text. Glossy references override any colour grade written in text. An object card brings its own shooting environment (studio, grey backdrop) and leaks it into windows, reflections and backgrounds. "Use as reference" with no role is the main reason a model takes the wrong thing. A reference image beats a style described in words.

04.22 **Reference numbers in the prompt match the order in which the files were uploaded.** If you mix up the order, the model puts the heroine's face where the car should be.

04.23 **Anything that appears more than once and must look identical gets a reference card; several angles on one card beat a single perfect angle.** Without a card every shot gets a different car. In video the object turns, so the model must understand it from all sides. A typical project has cards for the character, objects, location and any creature.

04.24 **Build face and body of a card separately: each face angle is its own generation (front, three-quarter, profile), the full-length figure has no head, then combine into one card.** Generating a whole person in several angles makes the face drift: "three different people". Clothes and accessories are shown without the model's head. Photo requirements for a face reference in Nano Banana: at least 1024x1024, face 30-50 percent of the frame, 3-6 angles, even soft light, one shooting session, no more than about 6 references per generation. Realistic cards: face fills the whole image in 4K, figure without head, three panels in one wide sheet. Cartoon characters use a turnaround sheet (front, side, back, close-up). Use a flat single-colour background for cards, `#cccccc` by default.

04.25 **One face reference is not enough: in video the face will drift.** The more good references from different angles, the more stable the final video. A solid set is 5 photos (front, three-quarter twice, waist-up, full length). A card with the face in three angles plus the look holds a face much better than a single photo. By default use 3 face angles, add up to 5 if the face still drifts.

04.26 **The face is held only by a reference, never by a text description.** Text holds clothes, light and surroundings, but not a face or a specific product. If a source model is weak at faces, use real photos for the face part of the card and other tools only for the look, figure and environment.

04.27 **When the face drifts, treat the symptom with a precise phrase, not blind regeneration.** Each feature (eyes, jaw, skin tone, proportions, age) has its own wording, for example "the same almond-shaped grey-blue eyes, the same set". Add an Identity Lock block to any prompt that has a character reference.

04.28 **In an outfit prompt, pin age, height and weight.** It helps to get the right proportions and skin texture. Example: age 23, height 170 cm, weight 50 kg, natural micro-texture of skin visible.

04.29 **Build frames by the laws of direction: wide, medium and close shots, and alternate the rhythm.** Do not run eight frames of one shot size. A 9-frame storyboard grid works well: "make a storyboard of these 9 frames from above, from below, from the side".

### E. The start frame

04.30 **The start frame is the anchor of a scene: one per scene, built from the reference cards and the scene description. Every video shot of the scene takes its light and palette from it.** Process: upload the cards to the agent, give it the scene description from the storyboard, get the prompt, generate. Check before moving on: one frame per scene, light and palette from the moodboard.

04.31 **Plan for a lot of retries: up to 95 percent of generations fail, and that is normal.** One start frame is tens of generations, not one or three. Run the same prompt through several models (`nano_banana_pro`, `gpt_image_2_6`, `seedream_v5_pro`): what one fails, another delivers. Start with one scene, not the whole video, and take it through the whole ladder. The rest then follow a known path.

04.32 **The start frame decides face consistency in video: a video model holds a face badly from text, but given a finished frame it just animates it.** Scheme: an image model makes a still poster with the consistent character (character card plus 3-6 brand photos plus a style reference), then the video model gets the poster as `@Image1` (style and start) and the card as `@Image2`. GPT Image holds a face across several iterations.

04.33 **To animate a photo from a reference video (Kling Motion Control), the character in the image must stand in the same angle and at the same distance as in the reference video.** If the person in the video is waist-up, your character must be waist-up too. Ideally the reference video has a static camera, no zooms, no shake. This is a start-frame condition, the video side is in stage 06.

04.34 **Prepare cards and the start frame knowing that the video model copies everything in the picture.** An open door on the picture can become an open door in the video, so car-interior cards have the doors closed on purpose. A neutral character card gives the look but not the acting: the character "turns to stone". Write the reference role as "look and clothes only, not pose and not expression". The first frame must also be readable (an obstacle, an edge, an object) so a previz scene can be built from it (stage 05).

04.35 **References for video must not be sterile: a perfectly clean image is out of distribution for a video model and produces plastic.** Before feeding Seedance, slightly dirty the references (grain, 5-10 percent soft blur, or a film pass). Run skin enhancers and sharpeners only after the video is generated.

### F. Upscale

04.36 **Upscale at the very end and only an accepted frame.** There is no point improving a frame you will reject. Settings matter: with default settings the difference is almost nil, with the right ones the frame transforms. Check the upscaler's current options before running.

04.37 **Upscale always.** Every accepted still and every accepted clip gets an upscale pass. For stills a skin-enhance pass plus a generative upscaler (for example Topaz), and then resize to the target delivery size. The file may become very large, compress it afterwards. For video the order is set in stage 06 (principle 06.53): references for Seedance are not upscaled, clips are upscaled afterwards one by one before assembly. A source photo for Kling Motion Control is upscaled before animation.

04.38 **Low native resolution is fixed by upscale, not by the prompt.** Some image models give only 720p, and turning a photo into a video loses 15-20 percent of quality. Some video models compress quality heavily, so clips go through an upscale pass. Order: upscale first, then effects.

### G. Product shots

04.39 **Every product prompt starts with the product reference and a demand to keep the packaging and typography 1:1.** Structure: Frame (shot, composition, background), Light, Camera, Negative. Choose light so the text on the pack stays readable (soft frontal light or a reflector). The negative always lists: distorted logo or text, deformed pack, "plastic" metal, noise, artifacts. Skin and lips look natural, pores visible. (Nano Banana takes positive wording only, so for it write the same constraints as positive facts, see "Common mistakes".)

04.40 **For one product shoot a set of shot types:** clean studio on white, editorial with a model, macro with a swatch, wet look with drops, flat lay from above, luxury vanity, in hand "on the go", ultra-macro of the moment of application, "drip", product frozen in ice. Each shot specifies camera (mm, aperture, ISO), light and background.

04.41 **For packaging text and ad layouts with writing, pick a model that renders text.** Put literal text in quotes or capitals, name the typography, ask it to render exactly once. For dense text use high quality. Small type is unstable in every model: recheck anything smaller than a headline and fix it in an editor. In ads, the real text is added in post (see 06.69).

### H. Fashion shots

04.42 **A fashion shoot starts with a brief from the brand's goal and an idea that tells a story and makes people want the item.** Brief steps: analyse product and audience, concept, visual elements (style, location, model, accessories, palette), technical execution (composition, angles, light), a series: full look, details, lifestyle. Criteria: shows the features and quality of the item, creates an emotional link, stands out and is remembered, matches the brand's positioning.

04.43 **Fashion idea: take an element of a luxurious life and weave it into the visual; replace the overused trick (a luxury car) with a fresh one** (a rare dog breed whose colours match the item). Search with a Pinterest-style query, ask an assistant for options (for example which dogs look aristocratic), choose by colour.

04.44 **A fashion prompt has eight parts:** subject / character / action; composition, angle and format; pose; surroundings; lighting; textures and realism; artifacts; atmosphere. A prompt is a system, not "make it pretty". Words such as a medium-format body name (luxury ads), "overcast light" (noble drama), "slight motion blur" (a living moment) are chosen for their meaning.

04.45 **Create a fashion character like this:** take a photo of a suitable type (Pinterest), have an assistant analyse the look and write a prompt for Nano Banana; generate 5-10 options and pick the best; then add the model photo plus 2-3 good photos of the item and a final prompt; then angles (frontal anchor, three-quarter as "the most important angle for life", profile, slightly from above). Series: close-up of the face, full body in motion, low angle, 9-frame detail storyboard "on the model", a close-up of one frame.

### I. Infographics and text in frame

04.46 **Product-card infographics aim to highlight the product, show its benefits and build an information hierarchy.** Write the prompt like a brief for a product designer, not like a pretty interface. Give required labels verbatim. After generation always check labels, numbers and arrow order: the model is not a source of truth for facts. Some models build charts, tables and exact numbers on request, and accept a PDF or text as the data source.

### J. Ultra realism

04.47 **Ultra realism comes from words about amateur shooting:** amateur photo, candid pose, photo shot on iPhone, casual framing, slightly tilted, visible skin texture, pores, RAW iPhone look, clear background. If realism is not enough, add artifacts: JPEG compression and slight motion blur (hand shake). Film grain, halation and lifted blacks are covered in stage 02.

04.48 **Realism depends less on the prompt than on the look reference and a phone-shot camera feel.** Amateur flash snapshots in the moodboard (night street, close faces on a grey wall) set the tone. Skin that is alive, real light and speed blur are hard to get from a plain prompt. If your image model cannot do this, use real photos as references and keep the face from real photos.

04.49 **In a realistic frame, describe skin as a fact: visible pores, micro-texture, "no plastic effect, no over-smoothing".** A photo realism word in the prompt ("a real photograph", "shot on film") switches the mode.

### K. Choosing a model per task

04.50 **One task can run through several models: each has strengths and you cannot predict them in advance.** Budget time and credits for the trials.

04.51 **Course hints for model choice (Higgsfield ids, check `models_explore`):**
- `nano_banana_pro`: reference cards (character, location, car, creature), start frame, native 4K, angles, product and fashion shoots, up to 14 references.
- `gpt_image_2_6`: text inside images, point edits, multi-step edits.
- `seedream_v5_pro`: point edits, second run of a start frame.
- `soul_2`: portraits and fashion looks, when the agent's model note says so.
- Midjourney is outside Higgsfield and has no API, so use it only if the user already has it.

04.52 **Two versions of a model can be two separate models: a text-to-image model and an edit model.** The edit version changes exactly what you ask, keeps the rest, and can assemble an image from several references at once. Check whether the model you need exists as both.

### L. Other

04.53 **Paid generations run only after the user agrees.** The agent walks the project from idea to video, and the user approves stages and says "ok" before paid steps. Save frames right after generation so they appear in the project.

04.54 **Start a new model with a model note.** Ask the agent to find the official instructions and community practice, then write a note with the formula and the character limit, and after that one line is enough: "write a prompt for such an image in such a model".

04.55 **Make series character images on a white background, 4 variants per prompt, and attach all earlier photos when you ask for a new angle.** The model then leans on several photos and the result is more accurate.

04.56 **A stable photo-prompt template for an identity reference** (observed pattern): (a) first sentence is identity: use the uploaded photo as the exact identity reference, preserve facial features, proportions, skin tone, hairstyle, no reshaping; (b) paragraphs per point: Location, Background, Framing (where it crops), Camera angle (height), Lens/look, Pose (stance, weight on the leg, hands, shoulders separately), Face/expression, Wardrobe (must match), Lighting, Details; (c) clothes itemised: type, colour, material, cut, collar and fastening, features, style; (d) a separate negative field and a duplicate structured JSON (style, camera, lighting, environment, subject, wardrobe, output); (e) one light and one "flash" look across the whole series.

04.57 **Realism comes from documentary details and deliberate imperfection.** Phrases such as "it must look like a real place, not a staged set", "the composition is slightly imperfect", readable signs and background items, a dark blurred background to keep attention on the subject, slight motion blur in the background while the face stays readable. It is the same trick as the ultra-realism words (04.47).

04.58 **Strong perspective and pose are described by body mechanics and camera position, not adjectives.** Example: camera at waist level below the raised leg, forced perspective with one sneaker sole huge near the lens, the torso lowered as a counterbalance, the face peeking from behind the leg. Another: low angle, speakers forming diagonals into depth, the right side empty and dark.

04.59 **A clash between clothes and scene is closed with a list of what must not appear:** wrong location, wrong shoes, wrong fit, sunglasses, daylight, studio background, extra people, duplicate person, extra limbs, bad hands, cropped head or feet, text, watermark. Adapt the list to the frame. Negative lists depend on the model: Nano Banana does not support them (write positive facts instead), GPT Image works well with a constraints block, other tools have their own `--no` style fields.

## Workflow

1. Check the input: moodboard, storyboard piece, references (face 3-5 photos, product, location, clothes without head). If the agent has no model note for the chosen model, write one first (04.54).
2. Choose the model for the task (04.51). Tell the user the model, the number of generations and the credits from `estimate_image_cost`, with the stage checklist and yes/no per item; name any move that is not the method as a deviation. Wait for the user's "yes". (user's ok)
3. Reference cards: character (face angles separately, body without head, combine), objects and location (several angles on one card). Check that clothes, features and texture match the moodboard.
4. Write the base prompt with the agent (formula plus the four inputs). Generate 4 images.
5. Review: what is good, what is not, which gaps. Go back to the source prompt, add, regenerate (04.14, 04.15).
6. For a series: fix references and description, change only the SHOT line, 4-8 variants per angle, save the best (04.16). Collect wide, medium and close shots.
7. Start frame per scene: cards plus scene description, tens of generations, several models if needed, pick one anchor.
8. Edits: "change / keep", one edit at a time. If it does not help, add a new reference and rewrite the whole prompt.
9. Product and fashion frames: use the formulas below, check packaging, logo, skin.
10. Upscale accepted frames (at the very end), save them in `frames/`, log model, prompt and "accepted" in `prompts.md`.
11. Show the user, get the "ok" (checklist below). (user's ok)

If you catch yourself inventing on the fly, the stage is not ready: preproduction was not finished and you go back.

Studio defaults for real people (default; the user may change it): first a pack of references (3-5 photos per person), then one approved portrait per person, and only after the user's "ok" the scenes. Before saying "looks like them", crop the face and put it next to the photo. No more than 2-3 named people in one scene. Skin stays alive, no retouching, except a client's own double and only at their request. For video, a face that Seedance rejects may need another route, see stage 06.

## Formulas

Photo prompt (full examples in `templates/image-prompts.md`):
```
1. Subject: who or what. Not "cat", but breed, colour, details.
2. Location: where. The more exact, the better.
3. Action: what the subject does right now. Pose, gaze, movement.
4. Angle and camera: from where and how. Angle (low, high, eye level, POV), shot size, lens, perspective.
5. Light: where from, which shadows, what contrast.
6. Effects and styling: film, grain, grade, genre.
Priority: if style conflicts with realism, realism wins.
```
One example of our own: "A small tabby cat sniffing a pale rose on a dark wooden table in an old library with tall shelves; low afternoon sun from a high window with dust in the beam; eye level, close-up, 85 mm lens, f/2, shallow depth of field; shot on 16 mm film, fine grain, warm grade."

Fashion prompt, eight parts:
```
1. Subject / character / action
2. Composition, angle, format
3. Pose
4. Surroundings
5. Lighting
6. Textures and realism
7. Artifacts (film, dirt, imperfection)
8. Atmosphere
```
Product prompt: `Reference + preserve packaging and type 1:1 -> Frame -> Light -> Camera -> Negative`.

Nano Banana formula A: `[verb] + [subject] + [action] + [location/context] + [composition] + [style] + [purpose]`, written as full sentences.
Nano Banana formula B (references): what to take from which reference, the link between them, the new scenario, then "keep the exact facial features of the reference".
Nano Banana edit: "Edit the attached image. Change: one specific change. Keep everything else exactly as it is: composition, angle, light, other people, background, grade."

Ultra-realism words: `amateur photo, candid pose, photo shot on iPhone, casual framing, slightly tilted, visible skin texture, pores, RAW iPhone look, clear background`.

Character replacement: `[action command] + [new character] + [link to surroundings] + [keep the style]`, with the canvas and donor roles named.

New model note request: "Find the official prompting instructions for this model and the best community practice. Write a note: the formula (the six parts), the character limit, known quirks, and how to give references."

## Check before "ok"

Ladder checklist:
- [ ] A model note exists for every model we generate in.
- [ ] Reference cards exist for everything that appears more than once. Face and body are built separately and combined. Clothes, features and texture match the moodboard.
- [ ] One start frame per scene. Light and palette come from the moodboard.
- [ ] Reference numbers in the prompt match the upload order.
- [ ] Final frames went through upscale, and only after being accepted.

Per frame:
- [ ] All six formula parts are filled with specifics. No banned adjectives. A constraints or priority block is present (GPT Image: the length is counted; external short-prompt tools: 20-60 words).
- [ ] Every reference has a role: what we take and what we do NOT take.
- [ ] Product frame: packaging and text 1:1, logo readable, metal looks like real chrome, skin has pores, product in focus.
- [ ] Fashion frame: shows the item, matches the brand positioning, the scene colours go with the item.
- [ ] Text in frame and infographics: labels, numbers and arrow order checked against the facts, small text proofread.
- [ ] The face is compared side by side with the reference card, and the frame is not younger, cleaner or prettier than the approved card (default; the user may change it).
- [ ] The emotion of each frame is named in physical words (mouth, eyes, neck) and differs from neighbouring frames. The shots build toward the peak, with a quieter start, not full intensity everywhere.
- [ ] Doors, windows and objects in the picture are in the state they must have in the video (everything in the picture moves into the clip).
- [ ] The prompt has no foreign brands or studio names (describe the properties of the picture instead). Real people only by the studio rule above.
- [ ] For absurd-comedy reels: the odd thing is staged with real people, animals and props, nothing comes alive, flies or glows (default; the user may change it).
- [ ] The price message listed the model, the number of jobs, the credits and the checklist, and the user said "yes".

The stage closes only after the user's "ok".
- [ ] Frame quality (02.70-02.74): light from the shadow side plus a back light; lens and aperture named; 1-3 main colours and the accent match the neighbouring frames; three planes; no clutter; one centre of attention.
- [ ] None of the defects AI makes on its own: dead or grey-green skin, plastic highlights, a glowing outline around the figure and hair, a stock tear on the cheek, flat light without shadows.

## Common mistakes

- A short prompt ("beautiful cat") gives a grey, average image.
- Inventing details instead of carrying them from the moodboard.
- Changing several parts at once, so you cannot see what helped.
- Re-editing a finished picture again and again: Nano Banana eats the quality.
- Commands such as "change the face" instead of a detailed prompt from the start.
- One face reference: the face drifts in video.
- Forgetting accessories and makeup in the first prompt.
- Asking the agent for a prompt without a model note, or not telling it how the assembly works.
- Generating a whole person in several angles at once: "three different people".
- Patching an old prompt instead of rewriting it with a new reference; an edit with no keep list; mixed-up reference order; waiting for one perfect generation; upscaling before acceptance; default upscale settings; a reference card with one angle only.
- Inventing on the fly in production: preproduction is not finished.
- Fashion: the overused trick (luxury car), a dog that does not match the colours, "make it pretty" without structure.
- Replacing a character without naming canvas and donor; starting over when only the clothes are wrong; an unrealistic insert without a Seamless integration block.
- Model weak spots: GPT Image can drift on small details (fingers, teeth, shoulders) and moderates strictly. Nano Banana: tag soup, negative prompts, 10+ references at once. Short-prompt tools: prompts over 60 words, copied syntax that no longer exists.
- Taking a Pinterest reference as is: it is someone's plastic generation, so add uniqueness.
- Telling a model about the face in words and expecting the same face.

## Tools

Always check `models_explore` for current models and `estimate_image_cost` for the price in credits before any paid run. Never rely on a remembered price.

| Tool | Role in this stage |
|---|---|
| `nano_banana_pro` (`generate_image`) | Reference cards, start frames, series, character replacement, product and fashion shots, 9-frame storyboards. Up to 14 references, best with about 6, up to 5 people. Native 1K/2K/4K. No negative prompts. |
| `gpt_image_2_6` | Text inside images, point edits (CHANGE / KEEP), multi-reference, transparent background, infographics, poster start frames. Constraints blocks work. |
| `seedream_v5_pro` | Second run of a start frame, point edits. |
| `soul_2` | Portraits and fashion looks. |
| `media_upload` | Bring the user's reference photos into Higgsfield. |
| `generate_image_batch` | Several variants at once after the user's "yes". |
| Upscalers (a skin-enhance pass, `upscale_image`, or a local upscaler) | Final pass on accepted frames. |
| Pinterest or any image search | References for look, location, type. |
| A text editor | Keep all prompt versions in `prompts.md`. |
