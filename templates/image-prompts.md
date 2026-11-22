# Image prompts

How to write a still-image prompt for each model family on Higgsfield, plus recipes for special tasks. Used mainly in stage 04 (frames) and stage 03 (references). Check `models_explore` for the current model list and `estimate_image_cost` before any paid run. Nothing paid runs without the user's "yes" on the exact list (model, number of jobs, credits).

Default prompt language is English. The user may write in their own language if the model handles it; keep proven English token blocks (film look, lens names) in English.

## 1. General formula (any model)

A prompt is a brief for a photographer, not a wish. Name every element, so the model has no room to average. Short prompts give the average image of the subject, and the average is grey.

Six blocks, in this order:

1. **Subject.** Who or what is in the frame. Not "a cat": breed, coat, ears. Not "a woman": age, build, features, clothing by layer with material and fit, skin texture. For a series, write the main character as a constant and repeat it word for word.
2. **Location.** A specific place, time of day, weather, 4-6 objects, and what sits in foreground, middle ground and background.
3. **Action.** What the subject is doing right now: pose, where they look, what the hands do, how much of the body is in frame, motion frozen or blurred.
4. **Angle and camera.** Distance (close-up to wide), height and angle (eye level, low, high, bird's eye, Dutch), lens feel (24, 35, 50, 85 mm), depth of field, composition and negative space. This block often decides the frame more than any other.
5. **Light.** Source and direction, hard or soft, where the shadows fall, contrast, colour temperature. This block turns an average photo into a frame.
6. **Effects and style.** Medium (35 mm film, digital cinema, phone photo), grain, halation, colour grade, genre, surface texture ("visible pores, fabric wear, no plastic skin").

Close with a **priority line** ("if style conflicts with realism, realism wins") and, where the model supports it, a **constraints line** (see per-model notes).

Rules:
- Facts, not praise. "Stunning cinematic masterpiece, 8K" gives the model nothing. "One hard key light from the left, 4:1 contrast, long shadows" does. Replace each vague word with a visible fact:

| Instead of | Write |
|---|---|
| beautiful light | warm overhead track light, soft highlights |
| dramatic | one hard key light, deep shadows, high contrast |
| cinematic | teal and orange grade, warm highlights, cool shadows, film grain |
| natural | overcast daylight, soft diffused shadows, even exposure |
| golden hour | low warm sun at 15 degrees, long shadows, amber highlights |
| detailed | visible skin pores, fabric texture, worn edges, scratches |
| premium | one hero object, soft studio light, lots of negative space |

- Say "photorealistic photograph" or "shot on film" to switch the model into photo mode. Camera specs set the general look; the model does not simulate optics exactly.
- Numbers and positions explicit: "three bottles, the tallest in the centre", not "several bottles". Empty space is a spec: "clean empty third on each side for a headline".
- Say the purpose of the frame in the first line ("hero frame for a product page", "first frame of a reel"). The model then picks the crop.
- Length scales with the number of decisions you hand to the model. Complex staged frame: 2000-3500 characters, all six blocks. Simple portrait or product shot: 1200-2000. A single edit: 200-600, only the change/keep structure. A mechanical task (remove background, straighten): one or two sentences. Length from filler words does not help; length from concrete facts does. Above about 4500 characters details from the middle get lost.
- A prompt that is a full rewrite after a correction is always sent whole, not as a patch.
- Camera angle words: low angle = camera near the floor looking up; top-down = straight down, 90 degrees; wide = 24 mm with slight edge distortion; Dutch angle = tilted 8-10 degrees; over-the-shoulder; shallow depth of field = 50-85 mm, soft background.

Light recipes:

| Scene | Light |
|---|---|
| Noir, thriller | one hard side key, deep shadows, 4:1, low-key, light cuts the face in half |
| Beauty | soft frontal light, beauty dish above, even fill, soft shadows under the chin |
| Documentary | available light, mixed warm lamp and cool street, unposed |
| Window interior | soft diffused window light from the left, falloff into shadow, warm balance |
| Sunset | low warm sun, long shadows, amber highlights, rim light on the edge |
| Neon night | mixed neon, blue and magenta reflections on skin, wet asphalt reflecting signs |

Style block starters:
- Film look: "shot on 35 mm film, fine natural grain, light halation on bright sources, soft highlight rolloff, warm highlights and cool shadows, visible skin and fabric texture, no AI smoothing, no plastic skin."
- Reportage: "colour documentary photograph, 35 mm reportage lens feel, shallow depth of field, real skin with pores, natural white balance, no commercial gloss."
- Glossy beauty: "clean studio light, soft highlights on skin, saturated but balanced palette, careful retouching without plastic."

Example (own, short):

```
Hero frame for a ceramics shop banner. A hand-thrown matte sand-glaze pour-over dripper with visible throwing lines on the side, on a worn oak table. Early morning in a small kitchen, a steam wisp from a kettle at the back, a linen cloth in the foreground. A hand lifts the kettle and pours a thin stream. Eye-level close-up, 85 mm feel, shallow depth of field, dripper in sharp focus, empty space on the right third for text. Soft diffused window light from the left, gentle falloff, warm balance. Photorealistic photograph, fine film grain, visible clay texture. If style conflicts with realism, realism wins.
```

## 2. nano_banana_pro (main image model, up to 14 references)

**When to use.** Default for frames, reference cards, replacing a character, outfit and product shots, edits by conversation, native 4K, readable short text, up to 5 distinct people in one scene.

**Rules (different from the GPT family).**
1. Natural sentences, like a brief to an art director. No tag soup ("dog, park, 4k, realistic").
2. No booster words (4K, masterpiece, trending). Resolution is a parameter, quality comes from concrete detail.
3. Positive phrasing only: "empty street", not "no cars". Negative prompts are not supported.
4. Start with a strong verb: Create, Edit, Replace, Move.
5. Edit, do not re-roll. If a frame is 80 percent right, ask for one specific change in conversation ("now change the light to sunset"). The model finds the area to change by itself, no mask needed. Say what changes and what stays.
6. Purpose raises quality: "for a gourmet cookbook cover" brings professional light and depth.
7. Text in the image goes in quotes with a font description: "the sign reads 'SALE' in bold red serif letters".
8. Give every reference an explicit role and say what NOT to take (see `templates/characters-and-refs.md`).
9. Fewer than 7 references with a clear role each; more averages the faces.
10. Material beats adjective: "scratched oak table with matte varnish", not "table". Describe light by source and temperature.

**Formula A, from scratch.** Verb + subject + action + location/context + composition + style + purpose.

```
Create [image type]. [Subject: age, clothing, materials, textures]. [Action]. [Location, time of day, atmosphere, set details]. [Composition: shot size, angle, lens]. [Style: light as on set, palette, film or grade]. [Purpose: "for a crime thriller poster"].
```

**Formula B, with references.** What to take from which reference + how they connect + the new scenario.

```
Using the attached images: the character's face and look from images 1 and 2, the location and light from image 3, the product from image 4. [Connection: "seat the character in the armchair from image 3, put the product on the table"]. [New scenario: what happens, composition, style].
Keep the exact facial features from the references: same eyes, nose shape, jaw line, skin texture.
```

**Edit by conversation.**

```
Edit the attached image. Change: [one specific change]. Keep everything else exactly as it is: composition, angle, light, other people, background and colour grade.
```

A chain of small edits works better than one mega prompt: the model remembers the conversation.

**Identity lock** (add to any prompt with a character reference):

```
Keep exactly the same facial features as in the reference images: the same eyes, nose shape, jaw line and skin texture. The face is recognisable as the same person.
```

**Specs to check live (`models_explore`).** Native 1K / 2K / 4K; aspect ratios from 1:1 to 21:9 including 9:16 and 16:9; up to 14 references; SynthID watermark on output.

**Common mistakes.**

| Mistake | Fix |
|---|---|
| Tag soup | Full sentences |
| "no blur, no cars" | "sharp focus", "empty street" |
| Re-rolling the whole frame for a detail | Edit: "change only X" |
| "4k masterpiece ultra" | Resolution as a parameter, concrete detail in text |
| 10+ references | Under 7, each with a role |
| "add a caption" | Text in quotes + font + colour + position |
| Glossy references override the film look | State reference roles explicitly (take identity only, not grade) |

## 3. gpt_image_2_6 and gpt_image_2_5 (GPT image family)

**When to use.** Precise edits that must not drift (product, logo, face), multi-reference composites, transparent background cut-outs, text-heavy layouts, UI or infographic mock-ups, fast drafts. The family reads a prompt as an instruction from left to right, keeps world knowledge and renders readable text. Prefer the newer version; the structure below is the same engine.

**Rules.**
1. Use the six-block formula for generation from scratch. No block is skipped.
2. Complex frames: 2000-3500 characters of concrete facts (see budget below). Optimum 2000-3500, above 4500 details get lost.
3. Facts instead of praise (table in section 1).
4. Constraints work in this family. End with a constraints line: "no watermarks, no logos or brands, no extra text, no extra people in the foreground, no AI smoothing or plastic skin, no floating objects, no anatomy distortion; realistic proportions, clean edges."
5. Say "photorealistic photograph" to get photo mode.
6. Series: describe the main character once as a constant, add "same character, same face, same look in every frame". Give each frame its own angle.

Character budget per block for a complex frame: subject 250-450, location 350-550, action 200-350, angle and camera 200-350, light 250-400, effects and style 250-400, constraints 150-250.

**Edit mode: change / keep.** The core of the newer version. A bare edit with no keep list is the main cause of drift.

```
CHANGE: [exactly one change]
KEEP: [face and identity, pose, light, framing, background, object geometry, text, composition, shadows, reflections: list everything that must not move]
INTEGRATION: [how the new element must fit: light, perspective, scale and shadows match the existing scene]
CONSTRAINTS: [no new objects, no redesign, no logo drift, no watermarks]
```

One change per iteration. In a series of edits, repeat the keep list every time. If a part must stay pixel for pixel (a logo, legal text), tell the user a prompt cannot guarantee it and composite over the original.

**Multi-reference with roles (up to 16 images).**

```
Image 1: identity of the product or character, the authority. Keep geometry, materials, proportions, face or logo unchanged.
Image 2: light reference only. Take direction, softness, shadow contrast. Do not take subject, background or colours.
Image 3: composition reference only. Take framing, object placement, negative space. Do not take palette, text or materials.
Instruction: assemble the scene so it looks shot in one take: matching light, perspective, scale and shadows.
```

"Use as reference" with no role is the main reason the model pulls the wrong colour or background.

**Transparent background (cut-out).**

```
Create a clean cut-out of the product on a transparent background. Keep exact geometry, material, proportions and colour. Remove the surroundings completely. One object in the centre, clean alpha edges, no white halo, no checkerboard, no decorative shadow, no stand. Do not redraw or restyle the object.
```

Also set the transparent-background parameter if the tool offers it; check the alpha edges of hair, glass and translucent materials by eye.

**Sketch to image.** The sketch decides object positions, scale, camera angle, horizon and negative space. It does not decide materials, final light or photorealism. Prompt: "Turn the sketch into [final scene], keeping exact room geometry, camera position and layout from the sketch. Materials: [...]. Light: [...]. Do not add furniture, text or architecture that is not in the sketch."

**Text in the image.** Literal text in quotes or capitals, with typography (font, size, colour, position) and "rendered verbatim, exactly once, no duplicates, no extra words". Short text (3-4 words) is reliable. Dense text (menus, specs, long captions) can have typos: use medium or high quality and read it after generation. For UI, slides and infographics write like a product designer's spec: exact layout blocks, real hierarchy, required labels verbatim, "no invented percentages". Check every label, number and arrow order afterwards; the model is not a source of truth.

**Quality and size.** Low / medium / high (and higher tiers where offered). Use medium or high for text, small details and portraits. Typical sizes: 1024x1536 vertical, 1536x1024 horizontal, 1024x1024 square; larger sizes are possible but less stable. Check the tool parameters live.

**Weak spots.** Fine details (fingers, teeth) can still shift in complex edits, strict moderation may block neutral objects, dense text needs manual proofreading. If a fast variant does not hold a complex edit, try the precise variant if the platform lists one.

**Constraints block (copy).**

```
CONSTRAINTS: no watermarks, no logos or brands, no extra text, no extra people in the foreground, no AI smoothing or plastic skin, no floating objects, no anatomy distortion. Realistic proportions, clean edges.
```

**Checklist before sending.** All six blocks in order. No banned praise words. Constraints at the end. Length counted. "Photorealistic" present if photo wanted. Text in quotes with typography. For edits: change/keep structure, one change. For multi-reference: a role and a "do not take" for each image.

Example (own, edit):

```
CHANGE: Only the colour of the jacket, to deep burgundy.
KEEP: Face and likeness, pose, hairstyle, background, light direction, camera angle, shadows on the wall, fabric folds.
INTEGRATION: The new colour reacts to the same warm window light; highlights stay on the same folds.
CONSTRAINTS: No new objects, no redesign of the jacket cut, no watermark.
```

## 4. seedream_v5_pro

**When to use.** A second opinion model for stylised or editorial images and when `nano_banana_pro` gives a look you do not want. The studio has no tested rules for this model yet.

**How to use it.** Start from the general formula (section 1) in natural sentences, with the purpose of the frame in the first line. Send one cheap test, compare with the same prompt on `nano_banana_pro`, and only then decide whether to continue. Read the model card via `models_explore` for reference limits, ratios and text support, and write what you learn into the project's `progress.md`.

## 5. soul_2

**When to use.** Higgsfield's own image model for photoreal people and fashion-style frames. The studio has no tested rules for this model yet.

**How to use it.** Same approach as section 4: general formula, one cheap test, compare with `nano_banana_pro`, check `models_explore` for reference support and presets. If it cannot take the references you need (identity, outfit), use it only for style exploration and build the real frames on a model that holds references.

## 6. Midjourney (external option only)

Midjourney is not on Higgsfield. Use it only if the user has their own account, and say so before suggesting it. Its strengths are art direction, environments, outfits and style exploration. It is weak at holding the face of one specific person (character and omni reference parameters were removed in V8), at exact layouts and at long text.

- Language: English. Subject first. Only the first 20-60 words really count; the first 5 almost always land. Hard input limit is much higher, but extra words are ignored.
- Formula: `[subject + action], [environment], [style/medium], [light], [shot size/angle], [camera + lens + film], [mood] --ar X:Y --s N [--raw] --v 8.2`.
- References: in the web app, drag images into the prompt bar and choose a role (Image Prompt for who and what, Style Reference for style). Never write URLs or placeholders in the prompt text. `--sref` in text only with a numeric code or `random`. Image and style weights stay as parameters (`--iw`, `--sw`). Refer to images in words ("the man from the reference photos").
- Parameters worth knowing: `--ar` always set; `--s` 0-100 literal, 100-300 balanced, 500-1000 artistic; `--raw` for photo and product; `--chaos` 50-75 for exploration, 0-25 for finals; `--no` with 3-5 items; `--seed` gives about 99 percent match, not 100.
- Removed in V8: `::` multi-prompt weights, `--cref/--cw`, `--quality`, Turbo, and `--oref` sends the job to the older V7. If a prompt contains these, say so and offer a replacement.
- Character across frames is a process: one personalisation profile, one `--sref` code, one recorded seed, the identity text copied word for word, 2-3 iterations per frame. For a hard identity, build the character in `nano_banana_pro` and use Midjourney for environments.
- Light: one main light term plus one modifier. Two light schemes cancel each other.
- Workflow: explore in draft mode, pick a frame, then run it in HD. Edits like inpaint, outpaint and zoom on an HD image drop it back to standard resolution, so edit first, upscale last.
- Style bank: lenses 14-16 ultra-wide, 24 landscape, 35 street, 50 natural, 85 portrait, 100 macro, 200+ compressed; film looks Portra 400 (warm skin), Ektar 100 (saturated), Gold 200 (nostalgic), CineStill 800T (night, neon, halation), Tri-X (dramatic black and white).

Example (own):

```
cinematic street portrait of a young woman crossing a neon-lit intersection at night, wet reflective asphalt, teal and magenta signs, 85mm f/1.8, CineStill 800T look, shallow depth of field, moody --ar 4:5 --s 150 --raw --v 8.2
```

Upload note under the prompt: "Image Prompt: 2-3 photos of the person. Style Reference: the style image."

## 7. Special tasks

### 7.1 Style transfer (take a look from a reference)

Use when the user says "I want it like this reference".

1. Receive the reference (image, link, or a verbal description).
2. Break it into seven components:
   - Light: source (natural, studio, practical), direction, quality (hard, soft, flat), time of day.
   - Colour: dominant hues, saturation, contrast, grade reference (Portra, teal and orange, pastel matte).
   - Camera and lens: shot size, lens feel, depth of field, handheld or static.
   - Texture and grain: clean digital, film grain, retouched or raw skin, visible materials.
   - Composition: thirds or centred, negative space, foreground, symmetry.
   - Mood: intimate, editorial, raw, dreamy, cold, tense; era.
   - Styling: fashion aesthetic, hair and make-up, props.
3. Compress into a reusable style block: `[light source and quality], [palette], [lens and shot size], [texture and grain], [mood in 2-3 words]`.
4. Apply: the style block goes after the character and scene description. Identity first, always. If the style fights the character (very dark scene and pale skin), say so. Change one element per iteration.

On a model that takes reference images, attach the reference and say "take only light, grade and texture; do not take subject, background or composition". On a text-only path, keep the style block short.

Example (own): reference "cold editorial, single spotlight, dark background". Style block: "single hard spotlight from above-front, dark seamless background, high contrast, cool monochrome palette, 85 mm medium shot, clean sharp digital, cold editorial mood". Applied: "[character] stands still, arms at sides, direct gaze, white oversized shirt. + style block. Photorealistic. Preserve face identity."

### 7.2 Replace a character in a frame

Two inputs: the **canvas** (scene to keep) and the **donor** (the new person). Use `nano_banana_pro` or a GPT-family model.

Formula: `[Action command] + [new character] + [link to surroundings] + [style preserved]`.

```
Use image 1 as the base for background and composition. Replace the person in it with the person from image 2. The new person takes exactly the same pose and angle as in image 1 and sits in the same light. Keep the original background and the realistic photo style. Keep the exact face from image 2: same eyes, nose shape, jaw line, skin texture and hairstyle. Everything else stays unchanged.
```

Add at the end against a pasted-in look:

```
Seamless integration: match lighting direction and intensity, match colour temperature and white balance, add realistic contact and cast shadows, match lens, depth of field and grain. The subject must look naturally captured in the location, not pasted in.
```

Variants: move a character into a new location (face and outfit from image 1, place from image 2); keep a character but take the pose from another image. Iterate with one change at a time: "now change only the jacket to a red coat".

### 7.3 Product shots

Always attach the product photo and demand exact preservation: "preserve the product and its typography 1:1: lettering undistorted, correct proportions, real material". One product per frame or per reference; two products in one reference get blended. Describe the product in words as well (material, colour, details), because text holds what is hard to see in the picture.

Frame template: product + frame type, light, camera, and a short "avoid" list (on a model that does not take negatives, phrase it positively: "text sharp and straight, packaging undeformed").

Recipes (one line each, fill in your product):
- Clean studio hero: product centred on white, large softbox in front plus thin back rim light, 85 mm f/8, soft natural shadow underneath.
- Editorial beauty close-up: model's face soft, product in perfect focus, warm beige backdrop, golden-hour side light plus a front reflector, 50 mm f/2.8, natural skin with pores.
- Macro texture: product lying at an angle on a glossy surface next to a large swatch of the product texture, two light sources (soft above, small hard for sparkle), 100 mm macro f/11.
- Wet look: product on wet glass with droplets, backlight for the droplets plus soft front light so the label stays readable, 85 mm f/10.
- Flat lay: top-down, warm off-white background, soft window light, lots of space, only the packaging carries text.
- Luxury vanity: product on light marble with one minimal accent (a ring or thin chain, no logos), warm soft light plus a small reflector for label readability.
- In hand, on the go: product in a hand with a blurred open bag and sunglasses behind (no brands), soft shade daylight, natural nails, 50 mm f/2.8, product in focus.
- Ultra macro on lips or skin: extreme close-up at the moment of application, visible viscosity and wet shine, dark or warm neutral background, small hard light for sparkle plus soft fill.
- Concept frame: product partly frozen in clear ice or gel with bubbles, pastel gradient background, one soft key light plus rim light for a clean highlight line on metal; ask for correct refraction, contact shadows and a readable logo.

Keep the label and logo checks for every result: zoom to full size and compare letters against the product photo.

Example (own): "Use the attached photo of the glass serum bottle as reference. Preserve bottle shape, label text and proportions 1:1. Product advertising photograph, bottle vertically centred on a pale grey seamless background, soft shadow underneath. Large softbox in front plus a thin back rim light for edge highlights on the glass. 85 mm, f/8, sharp, photorealistic. Label text sharp and straight, no extra lettering."

### 7.4 Outfit and character look (identity lock plus outfit lock)

Use for a full-body look of a person in a defined outfit on a plain studio background, to feed later scenes. Fill-in structure:

```
Photorealistic image of the person from the uploaded identity reference images.

IDENTITY LOCK: Keep the person 100% identical to the identity references (same facial features, bone structure, proportions, skin tone, hairline, hairstyle, facial hair).

OUTFIT LOCK: Dress the person in the exact outfit from the outfit reference images: same items, cut, fabric texture, seams, colours, prints and accessories. No redesign, no new logos, no extra patterns. The outfit fits naturally with realistic folds and drape.

Accessories: [list each, "as in the reference photo"]. Make-up: [description].
Age: [AGE]. Height: [CM] cm. Weight: [KG] kg.
Skin: natural micro-texture visible, clean healthy skin, no plastic skin, no over-smoothing.
SHOT: [full-body | close-up]. [3/4 left | 3/4 right | front]. Neutral pose.
Background: solid matte #cccccc. Soft even studio light, minimal shadows.
Optics: 85 mm full-frame equivalent, distance about 2-3 m, minimal perspective distortion, sharp focus.
```

Only the SHOT line changes between angle variants. Outfit rules: the outfit card shows the garment from four sides plus extreme close-ups of details; the prompt also describes every detail in the same words across the series, no synonyms; for wide garments describe volume by comparison ("the leg is almost as wide as the hip") and forbid slimming.

### 7.5 Photo-real "club photo" look (flash snapshot)

A phone or paparazzi flash look that reads as a real candid photo. Use when the frame must not look like a studio or an AI render. Recipe words that carry the look:

- Light: strong direct on-camera flash, crisp subject, hard shadows behind, high contrast, dark surroundings.
- Camera: slightly wide-angle phone snapshot, slightly tilted or off-centre, imperfect composition, optional forced perspective (a foot or hand close to the lens).
- Skin and finish: visible skin texture and pores, no beauty filter, subtle film grain, "RAW phone look".
- Add if it still looks too clean: JPEG compression artefacts, slight motion blur (moving limb and background, face stays readable).
- Background: a real, mundane place at night (petrol station, car park, corridor) with concrete details: pump labels, a neon sign, paving stones, a drain grate. Readable, not over-blurred.

Fill-in structure (works as a block list or as JSON; fields in this order):

```
Task and identity: use the uploaded photo as exact identity reference; keep face, hair, skin tone unchanged.
Expression and mood: [...]
Scene: [real place, time, 4-6 concrete details]
Pose and framing: [shot size, angle, stance, hands]
Lighting: direct on-camera flash, hard shadows behind, high contrast, subtle grain
Wardrobe (must match): [each item with colour, material, cut, fit]
Details: [jewellery, make-up, "no beauty filter"]
Avoid (if the model accepts it): face reshaping, different hairstyle, extra people, extra fingers, daylight, studio backdrop, text and watermark
```

A fixed wardrobe block repeated word for word keeps the outfit stable across a series of such frames. Check hands and the face against the identity photo.

Example (own): "Photorealistic night flash snapshot at a petrol station. Use the uploaded photo as the exact identity reference. Medium shot head to hips, straight-on, arms crossed, weight on one leg, calm slightly haughty look. Fuel pumps with coloured stickers behind, a digital price display to one side, dark surroundings. Strong direct on-camera flash, hard shadows behind, high contrast, visible pores, subtle grain, no beauty filter. Oversized cream quarter-zip sweatshirt, grey cap worn backwards, light-wash wide-leg jeans."

Related ultra-realism words (any model): "amateur photo, candid pose, shot on iPhone, casual framing, slightly tilted, visible skin texture, pores, RAW iPhone look, clean background".

### 7.6 Muse and fashion frames

"Muse" means a character built as a recurring fashion figure: one constant look, many editorial frames. Two sub-tasks.

**Fashion product shoot on a person.**
1. Eight points for a fashion prompt, in this order: subject/character/action; composition, angle and format; pose (stance, gesture, gaze); environment; lighting; textures and realism; artefacts (film, dirt, imperfections, vintage feel); atmosphere.
2. Build the character from a reference by describing it neutrally (age, face shape, skin, eyes, brows, nose, lips, hair, build, vibe) and then asking for the same look and type but not a copy of that person. Do not rate it ("beautiful").
3. Make anchor frames with the line "The same woman, identical appearance and outfit, captured in ...": a front portrait at eye level (base anchor), a three-quarter turn (most important for liveliness, gaze just past the camera), a side profile (confirms face and nose shape), a slightly elevated editorial angle. Each in soft diffused light, shallow depth of field, natural skin texture, muted studio background.
4. Scene frames: the model plus outfit photos plus any animal or prop reference in one prompt, with the location and a camera look ("Hasselblad medium format, overcast light, slight motion blur"). A low-angle shot with a tense leash and a cold, unimpressed look gives a fashion feel.
5. Detail series: ask for a nine-frame close-up grid of the garment details worn on the model, then pick one frame and ask for it large with high texture quality.

**Planner-style models (explicit fill-in rule).** A model that plans the frame itself (such as Muse Image from Meta, external) averages everything you do not name. The same discipline applies to every model: name each element, state the frame purpose first, give counts and positions, and say "empty space" where you need it. If that model is used, face stays held only by a reference image (text does not hold a face), up to about 10 references, a role and a "not taking" for each, no seed, so keep good frames as references. After 4-5 chained edits, restart with a reference instead of repairing the chain. Never name a brand or a studio as a style ("in the style of ..."): describe the image properties instead.

Example (own): "Low angle shot, the woman from images 1-2 holds a very large Afghan hound on a taut lead, the dog in the foreground pulling toward the camera, she does not look at the camera, cold unimpressed gaze, northern Europe in late autumn, minimal modern street, overcast light, medium format look, photorealistic fashion shot."
