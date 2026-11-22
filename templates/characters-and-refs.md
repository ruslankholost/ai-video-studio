# Characters and references

How to build reference cards (face, body, outfit, props, location), what each reference does in a prompt, how to keep a character the same across shots, and how to make a digital double of a real person. Used mainly in stage 03. Image prompt syntax lives in `templates/image-prompts.md`; video prompt syntax in `templates/video-prompt-seedance.md`.

Nothing paid runs without the user's "yes" on the exact list (model, number of jobs, credits from `estimate_image_cost`). Full sets of cards are made only after the faces and the storyboard are approved.

## 1. Why cards

The model does not remember a character. Every generation draws them from scratch. Text cannot hold a face: "brown eyes, dark hair" fits a million people. Images and video hold the face. Text holds clothes, light and setting. A card is one sheet that shows one character, garment or product from several sides, uploaded as a reference. One image of a face from one side makes the model invent the rest, and the face drifts in video.

## 2. Intake: ask before generating

Generate nothing until you know:

1. Who is the character: a real person, a realistic invented person, or a stylised cartoon?
2. What does the user have: photos, video, earlier generations? Can a real person film themselves?
3. Which video model is the target (`seedance_2_5` by default)?
4. Is it an ad? For clothes or a product? How many items, and is there a description (material, details, colour)?
5. How many episodes and locations?
6. How many looks (outfit changes) per character?

Pick the card types from the answers. Usually several: a character card, an outfit or product card, and one establishing frame per episode.

## 3. Which card for which case

| Case | Card |
|---|---|
| Real person, likeness must be maximum | Video reference of the person (section 4) plus a photo pack |
| Realistic invented character, must look consistent | Three separate 4K face portraits (front, three-quarter, profile) plus a full-body figure with the head cut off, joined in one row |
| Clothing ad | Character card plus a separate outfit card plus a written description in the prompt |
| Product ad | One card per product, plus a description in the prompt |
| Cartoon or stylised character | One turnaround sheet from one prompt |
| Location | Location card or a few reference photos of the place, plus an establishing frame |
| Prop that matters | Its own card, all sides, details close up |

**Real person, video reference.** The person films themselves: slowly turns the head (front, three-quarter, profile both ways), lifts and lowers the head, says a sentence and smiles so the mimic is visible. Even soft light on the face, calm plain background, camera at eye level, face large and in focus, no glasses, hat or facial hair unless they will be in the film. A photo shows one or two sides in one expression; a video shows the whole head and how the face moves. On `seedance_2_5` it goes in as a video reference.

**Realistic character, split faces.** Generate each face in its own image, 4K, face filling the frame (use `nano_banana_pro`; check native 4K in `models_explore`). The smaller the model draws a face, the less likeness it keeps, so six angles on one sheet give six tiny, averaged faces. Generate the full-body figure in the outfit separately and cut off the head, so the face is taken only from the portraits. A new outfit means a new full-body image and a rebuilt sheet; the faces stay. Join the images with a script or code (ffmpeg, Python Pillow) or by hand in any editor:

```
Build a character reference card. The folder holds three portraits (front, three-quarter, profile) and a full-body photo.
1. Three faces large, each the full height of the sheet. Do not shrink them more than needed.
2. Cut the head off the full-body photo at the chin. Faces come only from the portraits.
3. Everything in one row, even gaps, no labels, frames or text.
4. Save as PNG and show me.
```

**Clothing ad.** An outfit card: the garment full length from four sides (front, back, left, right), plus extreme close-ups of every detail (buttons, zips, elastic, fringe, seams, stitching, print, labels, hardware), in the same flat light on a plain background. The prompt also describes the garment in words: material, colour, cut, fit, every detail. Use the same words in every prompt of the series, no synonyms. The model replaces small details with similar ones (fringe becomes a straight edge) and slims wide clothing; close-ups show what the detail looks like, text says it is mandatory.

**Product ad.** One card per product: all sides, close-ups of clasps, hardware, logo, seams, material texture. Two products on one card get blended into one.

**Cartoon.** One sheet, one prompt: faces large (front, three-quarter, profile) and full body (front and side). A stylised character is held by shape, colour and silhouette, which small size does not damage.

**Turnaround sheet prompt (cartoon, or a classic reference sheet):**

```
Create a professional character reference sheet strictly based on the uploaded reference image. Clean neutral plain background, laid out as a technical model turnaround, reproducing the visual style of the reference exactly (same level of realism, rendering, textures, colour treatment). Two horizontal rows.
Top row: four full-body images side by side in this order: front, left profile (facing left), right profile (facing right), back.
Bottom row: three detailed close-ups of the face with visible skin texture, aligned under the top row: front portrait, profile, three-quarter.
Absolute identity match in all panels. Relaxed A-pose, same scale and alignment across views, correct anatomy, clear silhouette, even margins, same head height in all full-body poses, same face scale in all portraits.
Identical studio light in all panels, natural controlled shadows. Result: a sharp print-ready sheet with high detail.
```

## 4. Rules for every card

- One card, one character or one product. Two on a sheet get mixed.
- Plain background and even soft light. The background of a reference leaks into frames: a car-interior card once brought the studio walls into the car windows. Hard shadows are taken for face features and fabric folds.
- No labels, frames, arrows or text on the card. The model carries them into the frame.
- Skin alive, with pores, no retouching. A smooth card gives plastic skin in video.
- New look, new card (for the split-face type, a new full-body image).
- Fix a card by regenerating from the sources, not by editing on top. Mistakes of the old card survive spot edits.
- Each card has a role in the prompt: what to take, what not to take. For a character card take only look and clothes, not pose, expression or background. A card is shot in a calm pose; without this line the character goes stiff in the film. Pose and emotion are written in the acting of each shot.
- Face angles: at least three (front, three-quarter, profile). For a photo pack of a real person see section 8. Keep angle count as a project decision and write it in `progress.md`.
- Image sizes for cards: at least 1024x1024, face filling 30-50 percent of the frame on face references; flat even light and one shooting session or style across a set.
- Under 7 references per generation with an explicit role each; more slots average the face. `nano_banana_pro` tracks up to 5 distinct people in a scene, each needs their own reference and role.
- Background colour of cards: any plain colour, for example mid grey `#cccccc`. The value is a choice; plain is the rule.

## 5. The role of each reference in a prompt

Every reference file gets a number, a role, and a "do not take". Without roles the model guesses, and the result is unpredictable. Numbers in the prompt must match upload order exactly; a swapped order puts the heroine's face where the car should be.

| Reference | Take | Do NOT take |
|---|---|---|
| Character card | face, body, clothes (the only source of appearance) | pose, expression, background, light |
| Outfit card | garment, cut, fabric, colours, details | the person on it, pose, background |
| Product card | geometry, materials, label, logo, colours | shooting environment, reflections of the set |
| Location photo or card | environment, layout, light direction if stated | camera position, composition, any car or people in it |
| Light reference | direction, softness, contrast | subject, background, colours |
| Composition reference | framing, object placement, negative space | palette, text, materials |
| Style reference | grade, texture, mood | subject, composition, identity |
| Pose reference | body pose and position | identity, clothes |
| Previz or motion video | camera movement, positions, routes, timing | faces, acting, hands |
| Audio reference | voice, music | anything visual |

Image prompt wording (plain English):

```
Image 1: the character, the only source of face, body and clothes. Keep geometry, face and clothing unchanged. Do not take pose, expression or background.
Image 2: light only. Take direction and softness. Do not take subject, background or colours.
Instruction: build the scene so it looks shot in one take, with matching light, perspective, scale and shadows.
```

Video prompt rules (`seedance_2_5`, omni reference with start image, image references, video references and audio references):
- Give a role line per file: "@Image1 is the only source of look and clothes, not of pose or expression", "@Image7 gives only the cabin interior, not the environment outside or the light on set; the white factory walls and concrete floor must not appear, outside the windows is a moving motorway".
- A group that must be used together gets one shared role ("@Image4, @Image5, @Image6 are the same car from different angles, use all three").
- With more than two reference cards, add a split of duties and an avoid line: "avoid identity mixing between references".
- Negation through a reference: "unlike @Image4, in this world all cars fly".
- A previz video reference gives camera, positions, routes and timing, not faces or acting. Previz dummies have no faces or hands: if you do not write the acting, the model copies the dummy literally (still body, empty face). Write "@Video1 gives only camera movement, character positions, route and timing, not appearance, expression or hand action" and describe the acting in each shot.
- Check the model limits live (`models_explore`); numbering of `@Audio` and `@Video` is separate from `@Image`.
- For other video models (for example `kling4_0`) the same rule holds: state the role of each file, what to keep, and what not to take. See `templates/video-prompt-other-models.md`.

## 6. Establishing frame: one per episode

One image that holds everything together: character, product, location, light, colour and style of the film, generated from the cards.

- One establishing frame per episode in one location. A 30-second film with three locations gets three.
- Put it under every storyboard generation of that episode.
- Put it into the video generation together with the cards.
- Why: cards hold face, clothes and product, not the world. Without it each storyboard frame gets its own light, palette and scale: the product gets bigger or smaller, the room warm then cold. The establishing frame is the standard the model checks against.
- Describe the card in the prompt of the establishing frame and never skip that description.
- Do not put a mood-board reference into every storyboard frame.

## 7. Consistency in text

Text holds what is easy to say; the picture holds the face.

**Master identity block** (3-5 lines, copied word for word into every prompt, never paraphrased, placed first):

```
[NAME], [age range], [skin tone / look],
[hair: colour, length, texture, style],
[eyes: colour, shape],
[face: shape, jaw, cheekbones, nose, lips],
[distinctive marks: moles, freckles, scars],
[build],
[default energy]
```

Rules for the block:
- Specific, not relative: "almond-shaped dark brown eyes", not "beautiful eyes".
- Anatomical face terms: "soft oval face, slightly rounded jaw".
- A range for age ("22-26"), not "young".
- Three to five lines. Longer, and the end is ignored.
- Only stable facts: hair, clothes, wear, marks. Facial expression does not go in the block.
- Distinctive marks always mentioned, in the last line.
- Hair colour with a contrast ("warm dark brown, not black"); eye colour twice.

| Feature | Drift risk | Fix |
|---|---|---|
| Hair colour | medium | name it with a contrast |
| Eye colour | high | repeat twice in the prompt |
| Skin tone | medium | reference plus a natural light phrase |
| Face shape | high | anatomical words, reference image |
| Age | high | a range |
| Build | low | usually stable |
| Distinctive marks | very high | always mention, last line |

**Identity lock** (any prompt with a reference):

```
Keep exactly the same facial features as in the reference images: the same eyes, the same nose shape, the same jaw line and skin texture. The face is recognisable as one and the same person.
```

**Face drift: fix the symptom, do not re-roll blindly.**

| What drifted | Targeted fix in the prompt |
|---|---|
| Eyes | "the same almond-shaped grey-blue eyes, same set" |
| Jaw, face oval | "the same jaw line and face oval as in the reference" |
| Skin tone | "same skin tone and texture with visible pores, no smoothing" |
| Face proportions | "same proportions: eye distance and nose length per the reference" |
| Age | "exactly the same age as the reference, no rejuvenation" |

For video prompts add "keep consistent facial features throughout" and repeat the identity block as a reminder at the end if the model is weak at holding it.

**Before each new scene with an existing character:**
- the identity block is copied verbatim, at the start;
- eye colour named, age range given, distinctive marks included;
- reference image attached, each with a role;
- a face-priority line last: "IMPORTANT: preserve face identity, sharp facial features, consistent character look".

**Checks on every frame.** Compare each frame with the approved character card: did the person get younger, cleaner or prettier? If so, fix it before animation. A series of identical-looking frames in one session beats ten different ones; if one element keeps drifting, repair that element only.

## 8. Digital doubles of real people

A digital double is a real person (the user, a friend, a model with consent) as a character in generated scenes. Order matters.

1. **Photo pack first.** Three to five photos per person: front, three-quarter, different light. Add stills from the person's own 4K video if there is any. Shoot until the photos look like the person in real life; if the photos do not look like them, everything after is worse. Plain background, soft even light, camera at eye level, face large and sharp, no glasses or hat unless they belong to the look. A short video turning the head and smiling (section 3) is the best source.
2. **One approved portrait per person.** Generate the portrait set with the double prompt (below), one person per job. The user approves the faces before any scene is made.
3. **Then scenes.** Scenes use the approved portraits as references, with roles (section 5). Spend credits on full sets only after the faces and the storyboard are approved.
4. **At most 2-3 named people per scene.** More, and the likenesses blend.
5. **Likeness check.** Before saying "it looks like them", crop the face from the frame at full size and put it next to the photo. A small face in a wide shot always looks right and tells you nothing.
6. **Mixing a real person and an avatar in one video:** two steps. First a composite still (avatar inserted into the source frame) on an image model. Then animation on `seedance_2_5` with references: the source frame, a four-angle sheet of each person (front, three-quarter left, three-quarter right, profile), the composite, and a strict instruction to keep the source frame. Tie each sheet to the character's name.
7. After the double is made, outfit and body can be adjusted. A double may be cleaned of blemishes and redness; cards for invented characters are not retouched (section 4).

**Double portrait skeleton.** Same prompt for all angles; only the RACURS line (and age, height, weight, outfit lock) changes.

```
Photorealistic studio portrait of the person from the uploaded reference images.
Solid matte background colour #cccccc.
Natural skin micro-texture visible (pores, fine details), but clean healthy skin: remove acne, blemishes and redness, no plastic skin, no over-smoothing.
Neutral colour grading, no beauty-filter look.
Soft even studio light, minimal shadow.
Keep identity 100% identical to the reference images (same facial features, bone structure, proportions, skin tone, hairline, hairstyle, facial hair).
OUTFIT LOCK (only if outfit references are uploaded): use the exact outfit from the outfit references: same items, cut, fabric, colours, accessories and shoes; no redesign, no new logos, no extra patterns.
Age: [AGE]. Height: [CM] cm. Weight: [KG] kg.
RACURS: [one of the lines below]
Optics: 85 mm full-frame equivalent portrait lens, camera distance about 2 m, minimal perspective distortion, no wide angle, f/5.6, sharp focus across the whole face.
```

RACURS lines:
- Front: "Front view, facing the camera straight on, eyes into the lens, neutral expression."
- Three-quarter left / right: "Three-quarter [left|right] view (head turned about 30-40 degrees), eyes toward the lens, neutral expression."
- Profile left / right: "True [left|right] profile (nose pointing [left|right]), neutral expression, natural posture. Pay special attention to the curve of the nose and lips; they must be exactly 1-to-1 with the reference."
- Full body: "Full-body front view, standing straight, natural posture, correct head-to-body proportions for the stated height and weight." (Start the prompt with "Photorealistic studio full-body portrait".)
- Close-up: "Close-up of the face showing facial detail."
- Emotion: replace the identity block with an expression lock: "Replicate the exact smile from the smiling reference photo: same mouth shape, tooth visibility, lip-corner height, cheek lift and eye squint." Pick the angle in RACURS (three-quarter or front).

Photo pack typically feeds: front, three-quarter left and right, profile left and right, full body, emotions. Fill age, height and weight with numbers. Remove the outfit lock if it is not needed.

**Making a character from scratch (not a real person).**
1. Ask a text model for a concept (look, age, story, vibe) or describe a reference photo neutrally ("super detailed description of the woman in the photo") and feed that description to the image model, asking for the same type and vibe but not a copy.
2. Generate the base portrait on `nano_banana_pro`. Edit by conversation: hair, brows, lips, outfit, one change at a time ("hair: curly, ash blonde; brows natural, not drawn; lips natural").
3. Get angles by editing the base image: "close-up shot of the face, visible skin texture, maximum realism", "extreme close-up of the eyes and expression", "three-quarter shot of the face", "profile shot, facing sideways", "full-body shot standing elegantly".
4. Strong distinctive marks (a vitiligo pattern, different-coloured eyes) stay in place when they are fixed hard on the card; hands, fingers on fast gestures and hair edges on turns are what break in video.
5. Look prompt that combines references: "cowboy shot of the woman from the first image, wearing the clothes from the second image, in the location of the third image. She stands straight and looks at the camera. Main background light: muted and intimate; second source: direct flash. Visible skin texture. RAW phone look." Add the seamless-integration line from `templates/image-prompts.md` section 7.2.
6. Avatar swap into a talking video: screenshot of the source frame plus 2-3 photos of the avatar in similar angles; same pose and angle as the source, same light, replace clothes, hair and skin tone, run 6-8 generations and pick the best, then improve skin texture, upscale, and animate with a motion-transfer model (static camera).
7. A cast of one character in a place: a location prompt for the place, a nine-frame director's storyboard of the place, then a storyboard with the character in it (attach 4-6 location photos and 3-4 photos of the character). If the face drifts in a frame, send the frame plus all character photos: "make the first image high quality, visible skin texture, high detail; replace the face of the girl in red with the face of the girl from the reference photos". For a missing frame send the character photo plus the location photo and a one-line shot description.
8. Looks from a reference such as Pinterest: take as is, or add uniqueness by describing the photo to a text model and generating from the description. For a viral look ask the figure and features from a reference photo; the model by default makes everything plausible but not unusual.

## 9. Tools

- Faces, doubles, looks, replacement, establishing frame: `nano_banana_pro` (native 4K, up to 14 references, up to 5 people per scene). See `templates/image-prompts.md`.
- Precise edits that must not drift, product and outfit cards: `gpt_image_2_6` or `gpt_image_2_5`.
- Midjourney (external): outfit, figure and environment only. Do not use it for the face of a specific person.
- Video with cards and establishing frame: `seedance_2_5`; see `templates/video-prompt-seedance.md`.
- Use `media_upload` for the user's photos and video; `manage_reference_elements` and `show_reference_elements` for saved references if the account has them; always check `models_explore` and `estimate_image_cost` first.

## 10. Check before generating

- [ ] Intake questions answered; card type chosen for each character, outfit and product.
- [ ] Real person: video reference with head turns, speech and a smile, or a photo pack of 3-5 photos.
- [ ] Realistic character: three separate 4K faces plus a headless full-body figure, joined in one row.
- [ ] Outfit: four sides, close-up details, description in the prompt in fixed words.
- [ ] Product: its own card per item, description in the prompt.
- [ ] One establishing frame per episode in one location, placed under all storyboard frames and into the video generation.
- [ ] Cards: plain background, even light, no text or frames, one subject per card.
- [ ] Every card has a role and a "do not take" in the prompt; pose and emotion are in each shot's acting.
- [ ] Reference numbers match upload order.
- [ ] Real people: faces approved before scenes; at most 2-3 named people per scene; likeness checked with a full-size crop next to the photo.
- [ ] Paid runs: exact list, estimate, and the user's "yes".

## 11. Common mistakes

- Generating before the intake.
- Two characters or two products on one card.
- Busy background, hard shadows, labels, frames, arrows or text on cards.
- Retouching card skin.
- Editing an old card instead of regenerating from the sources.
- Passing pose, expression or background from a card into the film.
- Synonyms in the outfit description.
- Midjourney for the face of a specific person.
- All six face angles on one sheet.
- Skipping the establishing frame, so each frame gets its own light and scale.
- Wrong reference numbering.
- Saying "it looks like them" without a full-size crop next to the photo.
