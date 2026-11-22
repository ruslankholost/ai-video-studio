# 03 Characters and references

This stage builds everything that must look the same across shots: the face and body of a character, clothes, objects, a location, and the light and palette of a scene. The reason is simple: the model does not remember a character, every generation draws them from zero. Without this stage every shot shows a different person and a different car. Long prompts and tables are in `templates/characters-and-refs.md`.

## Input and output

Input: `script.md`; `storyboard.md` with the written-out list of characters, locations and recurring objects; `moodboard.md` (clothes, light, palette, face references); the decision which video model the generation goes to.

Output in `refs/`:
- a reference card for each character (of the type chosen under 03.15) and a text description of the clothes;
- cards for clothes and for a product, if this is an ad;
- cards for locations and recurring objects (anything that appears more than once);
- a setup frame for each episode in one location;
- a note "role of each reference: what we take, what we do not take" (it later goes into the prompt file).

For real people and doubles also: a photo base or a video reference. Sub-folder names inside `refs/` are set by the project (see `templates/project-folder.md`).

## Principles

### Why pictures, not words

03.01. A face cannot be held by text; it is held by pictures and video. "Brown eyes, dark hair" fits a million people. A reference card is one sheet where one character (a garment, a product) is shown from several sides. The face is held only by a reference. A text description of looks does not give consistency. Clothes, light and surroundings are held by description, the face and a specific product are not. Where a text identity block still helps, see 03.24 and the resolved rule: text holds clothes, light and setting, the picture holds the face. Identity of a face is a reference card, not a text description.

03.02. One image is not enough. If you show the face in one angle, the network starts to invent the rest, and in video the face floats. The more quality references from different angles, the more stable and realistic the final video.

03.03. Seedance holds a face badly from text, but if you give it a ready image it animates it. GPT Image holds a face through many iterations (you can redo a scene 10 times and the face stays). So fix the face in a picture before video.

03.04. Detailed text is needed where the picture holds badly: if every detail is written, the network does not forget it. The more detailed the prompt, the more predictable the result.

### A real person: neuro-double and photo base

03.05. Scanning yourself is the most important step: this is what the network will refer to. Shoot until the photos look like you in life. If the photos do not look like you, everything after is worse.

03.06. Photo base: 5 key face photos with no filters (front, 3/4 left, 3/4 right, profile left, profile right), photos with emotions (smile, laugh, neutral, surprise), face details (teeth, features of the smile), different distances. If small details of clothes matter (collar, buttons, seams, print), one extra close-up is needed; if there are tattoos, the clothes must not hide them. Default number of face angles on a card is 3, raised up to 5 if the face drifts. The 5-photo base is a separate stage from the card.

03.07. Shooting rules: head as for a passport (watch the chin), camera grid with the top line on the eyes, phone lens at least x2 (x0.5 and x1 distort, x4 often gives digital "plastic").

03.08. The network erases small disproportions because it aims at "beautiful", and the uniqueness of a face is in them. Generate more variants (for instance 8 images per angle) and pick the closer to the original. The test is "I believe it".

03.09. For maximum likeness of a real person a video reference is better: the person turns the head (front, 3/4, profile both ways), raises and lowers it, says a phrase and smiles; even soft light, plain background, camera at eye level, face large, no glasses, hat or hair over the face unless they will be in the video. Reason: on a photo the model sees one or two sides and one expression, in a video it sees the head from all sides and the mimic. Whether Seedance accepts such a reference with a real face is the open test C1 (see 03.69).

03.10. The double prompt consists of a `#cccccc` background, living skin texture, studio light, age, height and weight, an obligatory `identity lock` and an optional `OUTFIT LOCK`; only the `ANGLE` line changes (and age, height, weight, and the clothes binding). Seven ready prompts (front, 3/4 left and right, profiles, full length, portrait photo) and the emotion prompt are in `templates/characters-and-refs.md`.

03.11. Change only one variable at a time (the SHOT line): references, clothes description, makeup and lighting stay fixed. For a series: copy the base prompt, change SHOT, 4-8 variants, choose the best, next angle.

03.12. Smiles and emotions are made with a separate prompt with an `Expression lock` (repeat the mouth shape, visible teeth, height of the corners, cheek lift, squint); remove earlier uploaded photos from the dialog, keep only the smile photo.

03.13. If the network will not make full length, write the shoes or "barefoot" in the prompt.

03.14. After getting a copy of the double you may touch up (clothes, body): there is no reason for the double to be less attractive. Resolved: this retouch applies only to a client's double and only on their request. On cards and in scenes the skin stays alive, no retouch (see 03.22).

### Reference cards: what and how

03.15. Choose the card type by situation (consistency method): a real person with maximum likeness, a video reference; a realistic character, 4K faces by angles plus a body with no head; clothes advertising, a separate clothes card plus a description in the prompt; product advertising, a card per product; cartoon, one sheet from one prompt (a turnaround sheet: front, side, back, close-up). Before choosing, ask 7 questions: who is the character; what do you have in hand; what is the video in; is it an ad; how many episodes and locations; how many looks; where do we work. "Generate and assemble nothing until you know."

03.16. The classic card (a spread sheet with small figures) spoils the face in realism: Nano Banana unifies faces ("the smaller the character in frame, the blurrier and more generic the face") and with each generation the character looks less like themselves. Such a card is good for cartoon characters and 3D, not for realism.

03.17. The new card: close-ups of the face (front, 3/4, profile) as separate pictures in 4K (the face fills the frame, maximum pixels and likeness) plus the full-length figure separately; the head of the figure is cut off and the face is taken only from the portraits; they are joined in one row by the agent with a short script. Three images are enough. A request for the join is in `templates/characters-and-refs.md`.

03.18. Face and body are made separately. Generate a whole person in several angles at once and the face floats on each: the model rebuilds the features every time. Do not generate all 6 angles on one sheet: the faces come out small.

03.19. The figure is separate also because when clothes change you change only the full-length photo and rebuild the sheet; the faces stay. A new look means a new card.

03.20. Label one card in the prompt with a name ("Reference card NAME") and refer to it in every prompt: "face strictly from the reference card NAME". If the face on the full-length figure does not differ from the close-ups, still cut it; if variants are needed (for example with and without glasses), keep both.

03.21. Editing a card is a new generation from the sources, not an edit on top: mistakes of the old card survive spot edits.

03.22. General rules for any card: one card is one character or product; plain background (default `#cccccc`) and even soft light (background of the reference leaks into the frame, hard shadows are taken for features and folds); no captions, frames, arrows or text (the model carries them into the frame); skin is alive, with pores, no retouch (a smooth card gives plastic skin in video).

03.23. Fix clothes with text: the agent looks at the clothes image and writes a description of 300-500 characters (up to 800 when there are many details), and it is pasted into every generation. Even with a good card and the note "take the character from the card" the network loses small details of clothes. Use the same words in all prompts of a series, no synonyms; describe the volume of wide clothes by comparison ("the trouser leg is almost as wide as the thigh") and explicitly forbid narrowing.

03.24. A clothes card: from all 4 sides (front, back, left, right) plus extreme close-ups of all details (buttons, zips, elastic, fringe, seams, stitching, print, labels, hardware), even light, plain background. The network replaces small details with similar ones (fringe becomes a straight edge). A text identity block for the character (name, age, hair, eyes, face shape, distinctive features, build, default expression, in this order, copied word for word, put at the start) can hold what the picture does not, but it never replaces the face reference.

03.25. Object cards: if an object appears in two different shots and must look the same, it needs a card. Without a card each shot gets a different car. Each product gets its own card: two products on one card get mixed into one. Several angles in one card are better than one perfect angle, because the object turns in video. In one real project there were five cards (location, car, costume, creature).

03.26. A card is made only for what repeats: a single object or place for one episode needs one picture. Character cards, locations and recurring objects go to the video model.

03.27. For a product, the photo must come with the condition "keep the packaging and text 1:1" and a negative list (logo distortion, pack deformation). Every prompt starts with the reference and the demand to keep packaging and text 1:1. Negatives depend on the model (see 03.76 below on negatives).

03.28. For object characters (a box turns into a hero) the prompt demands that the pack design in front is kept, the inscription readable and not covered, "one unified body"; number the characters.

03.29. A figure can be made in an outside image tool with no face lock, but such a tool does not hold the face of a specific person. Use it only for the figure in clothes, a location and a setup frame, and make the face from real photos on the card.

03.30. Reference parameters for Nano Banana Pro: at least 1024x1024, the face takes 30-50% of the frame (for a realistic card the face fills the picture in 4K), 3-6 angles (front, 3/4 left, 3/4 right, profile, full body), even soft light on all, one shooting session. Not more than 6 references per generation (more slots averages the face into mush). The model tracks up to 5 different characters in a scene, each with its own reference and an explicit role.

### Role of each reference

03.31. Each reference has its role: what we take and what we do NOT take. For a character card only looks and clothes, "without pose, facial expression and background". Without this clause the character in the video turns to stone. Write pose and emotion in the acting of each shot.

03.32. An object or location reference card drags its shooting environment with it, and it creeps into any window, opening, reflection or background. A real case: the interior card of a car dragged the walls of a studio into the car windows. Add a clause "do not take the surroundings and light of the card".

03.33. References are marked by numbers in the prompt, and the numbers must match the upload order: if the order is mixed up, the model puts the heroine's face where the car should be. For several characters, number them in the request and upload photos in the order they are mentioned.

03.34. If references are not given roles the model mixes them into mush and guesses. Format: `role / take / do not take` for each reference. Every reference gets an explicit role, or the model guesses.

03.35. Fix identity with a direct phrase, not hope: `Identity Lock` ("keep exactly the same facial features..."), `Strict 1:1 replication of reference image @Image1... no beautification or stylization`, `Use @Image1 as strict identity reference`.

03.36. Face drifts by features and is cured spot by spot: eyes, oval or jaw, skin tone, proportions and age each get their own phrase "as in the reference". Do not regenerate blindly.

03.37. Each hero in each segment of the video prompt has their own picture and tag (`Hero (@Image7)` in every segment, not only at the start). This way faces do not mix.

03.38. Resolved by number of frames: with 30-40 storyboard frames feed only the setup frame and the reference card into each frame, not moodboard pictures. If moodboard pictures go into each of 30-40 frames, the network drags extras from them: color, effects, face features, the face floats and color jumps. With few frames, add location and model photos where the location is really in frame. A city or interior is described in words via the agent; if you change clothes from someone else's photo, cut the head off (crop) and lay the clothes on a plain background.

03.39. The video model gets character cards, locations and recurring objects, plus the setup frame together with the cards. Frames of a storyboard as pictures are not fed to Seedance or Kling. Exception: the first frame in image-to-video is a separate allowed device, and MiniMax H3 takes an approved storyboard grid as a reference (see stage 01, 01.66).

03.40. A smooth clean reference gives plastic in video. Before the video model slightly degrade references (grain, 5-10% blur). Hierarchy: a soft, well-lit frontal frame in the identity slot and a sharp detailed frame in its own slot. Optimum up to 6 images per generation; technical limits are higher (see 03.69 on counts).

### Setup frame and locations

03.41. Reference cards hold the face, clothes and product, but not the world. A setup frame is one picture where character, product, location, light, color and style of the video are together. It is generated from reference cards and works as an anchor: all video frames inside the scene take light and palette from it, and the scene does not fall apart. One setup frame per episode in one location (a 30-second prompt with 3 locations has 3 setup frames).

03.42. A setup frame is not the first frame of the video but a frame with all the atmosphere: the model full length, the location, photo style, grain. Each reference gives its own (angle, pose, surroundings), and everything is assembled in one large prompt plus a description of the reference card (without it, details are lost, for example headphones). Tune color with a levels adjustment. Generate many variants and choose the main frame of the whole video.

03.43. One setup frame is dozens of generations (up to 95% of generations are unsuccessful, that is normal). Run the same prompt through several models: what one did not pull, another does.

03.44. The setup frame goes under all storyboard generations of the episode and into the video model together with the reference cards. One course source says it does not usually go into the video itself, but is put under each frame; the studio default is the first: it goes into Seedance and Kling together with the cards.

03.45. A location is assembled from 5-6 images (including a terrace if it will be in frames). Three ways: Pinterest; a description of a picture made by an agent and a detailed prompt; invent from scratch. From the reference make a location prompt, then a 9-frame director's storyboard of the location (4 generations), and bring the liked frames (close, medium, wide) to quality with the command "make this image detailed and high quality". In the grid the network draws extra surroundings, and these frames can be fed as a location reference.

03.46. A location from another angle: if you have only the setup frame, describe in detail what is there (sofa, wardrobe, two doors), prompts of 1000-1500 characters with every "screw"; a fallback is a 3D world from one photo (lower quality, artifacts may carry over).

03.47. Several cards of a location (four) keep the model from collapsing into one composition. Several angles of an object (three angles of a car) help geometry and orientation. A group of cards is labeled with one role ("these three pictures are one car from different sides, use together").

03.48. The consistency chain: every result becomes the reference for the next step (stand-in, 3D style, screens, clip 1 as `@video1` for clip 2). Quality is decided not by tools but by consistency.

### Character replacement and edits

03.49. Character replacement: a structured prompt `[action command] + [new character] + [link to surroundings] + [style preservation]`, otherwise the network redraws everything. With two photos, explicitly separate the "canvas" (background, pose, lighting) and the "donor" (looks, clothes). Keep the pose when interacting with objects and the light direction of the source.

03.50. Against the "pasted in" look add a `Seamless integration` block at the end (light, temperature, contact shadows, lens, depth, grain).

03.51. Edit a detail by forbidding everything else: "keep the girl from photo two unchanged, same face, same features, same skin tone, same pose, same clothes, same background and light, change only makeup and hairstyle". Without the ban the model changes what was not asked. If edits do not help, the model does not see the needed object: add a reference card as a second input and rewrite the whole prompt rather than patching the old one.

03.52. How to edit (resolved): wide changes early on, edit the source prompt and regenerate. One detail on an almost finished frame: edit by dialog. After 4-5 edits, start again with the reference. A reference card is only regenerated from the sources. Rule of thumb: do not start from zero because of clothes if the face is excellent, but do not keep twisting a finished picture, it eats quality.

03.53. Pose from one reference, identity from another: "keep the character from image 1 but put them in the pose from image 2".

03.54. Replacing with an avatar in a talking video: a screenshot of the frame plus 2-3 avatar photos at close angles, pose and angle as in the source, 6-8 generations, then skin enhancer, upscale and motion control.

03.55. A real person and an avatar in one video: two steps. A screenshot of the source video, a composite (avatar inserted in the frame) in an image model, then animation through Seedance with references (source frame, sheets of 4 angles of the man and of the avatar, the composite) and a strict clause to keep the source frame. Sheets of 4 angles (front, 3/4 left, 3/4 right, profile) are bound to the character's name.

### Neuro-model, AI blogger, UGC

03.56. Save a neuro-model in different angles so you can always return to those photos to keep all details. Get angles with an edit command and the angle prompt.

03.57. A reference from Pinterest is taken as is (it is not a real person, it is someone's plastic generation) or made unique: the photo goes to the agent ("write a super detailed description of the girl in the photo"), the description goes to the image model. Pick the generation where the heart beats faster. For virality the figure is set by a reference photo: the network by default makes everything super realistic, and virality needs unusual. Ask for "not a copy: same type and vibe, a different person".

03.58. For animating from a trend video (motion control): a reference with no zoom and no shake; the character on the photo at the same angle and distance (if the video model is waist-up, the character is waist-up); upscale the photo before animation, because turning into video loses 15-20% of quality.

03.59. An avatar blogger: concept and description first (fix age, style, character, vibe, hairstyle), two prompts, 4 generations of each, choose where face and vibe match the plan; then 5 angles (full length, three quarters, close-up, profile, seated) on a white background; add all previously made photos to each new prompt.

03.60. A neuro-clone look: references (5 photos of the model: front, 3/4 x2, waist-up, full length; outfit and accessories without head and face), a prompt with IDENTITY LOCK and OUTFIT LOCK and age, height, weight parameters (it helps reach needed proportions and skin textures). First find gaps after the first generation (forgotten accessories, makeup), then extend the source prompt. Clothes must sit with realistic folds and drape. Keep the prompts in one document.

03.61. Frames for video are assembled by the laws of direction (close, medium, wide). A missing frame is made from the model photo plus the location photo and a short frame prompt. On a storyboard frame replace the face with photo references: "replace the face of the girl in red with the face of the girl from the reference photos". Commands like "change the face to the model" with no reference give a bad result.

03.62. An AI-blogger builder works like a character creator (build, sex, face, eye color, hair, style), and the avatar is called by an `@` link in the prompt. Check the look against the model's moderation in advance: some models block underwear and intimate scenes, others let them through.

03.63. A UGC creator and an AI influencer are assembled in one workflow: a character bio, photo generation, reference card, clothes, three ready scenarios. Then the creator's card plus the product card plus a product description give UGC advertising (3 photos in different locations and a video).

03.64. A fashion series: from the chosen character make a set of angles with anchor prompts (a front portrait as the "base anchor frame", 3/4 as "the most important angle for liveliness", profile "to confirm the face and nose shape", slightly from above), and everywhere "The same woman, identical appearance and outfit". A series-assembly prompt has 8 points (object, composition and angle, pose, surroundings, light, textures, artifacts, atmosphere).

### Style transfer

03.65. Style transfer takes a reference apart into 7 components (light, palette, camera and lens, texture and grain, composition, mood, styling or subject), builds a short style block and applies it to a new scene. The style block goes after the description of the character and the scene. "Never let style override character identity: identity block first, always." On a conflict of style and character (dark scene and pale skin) warn; correct one element at a time.

03.66. For models that cannot take a style reference as an upload (some video models), style goes only as text, 80-100 characters. In Midjourney, `--sref` is taken as a numeric code or `random`, or the style image goes in the Style Reference slot, not as a URL in the text. `--sref` carries color, medium, light and texture, not the subject.

03.67. A reference picture beats a text style: so a face reference is accompanied by an explicit "do NOT take style and grade from the references".

### Video checks that concern the character

03.68. Check video with a contact sheet of frames for faces and hands, not by one viewing: faces, hands, direction of movement across several frames in a row; frame by frame for drift of face or product.

03.69. In tests of Seedance 2.5, face identity held with 5 or more references with a role-separation block, and the anchor held all 30 seconds. Whether Seedance on Higgsfield accepts real faces as references is an open test (C1): one report says it rejects references with real human faces ("Reference content can't include real human faces"), the course shows a card made from real photos. Until the test is done and priced, do not put real faces into Seedance references: make the face stylized or go through Kling. The test: one Seedance 2.5 generation with a card from the user's own real photo (their own face, not a client's or an artist's), 3-5 s, plus a variant "full-length photo". Use the minimum length at 480p and the price from `estimate_video_cost`, and ask for an explicit "yes". Count of references: the optimum is up to 6 per generation. Technical ceilings are higher and differ by model and version (Nano Banana Pro up to 14, with up to 5 humans; GPT Image up to 16; Seedance 2.5 many more). Read the current limit in `models_explore` before relying on a number. More slots average the face. For Seedance, 5 or more keep the face under a roles block; a film-look skill says no more than 5 images. A lesson with 5 photos of a model plus outfit plus accessories is the exception.

03.70. Every newly invented character or product gets one signature trait (identity anchor) that makes the silhouette original and fixes consistency between beats. Never invent character details: always confirm with the user first.

03.71. An example of a neuro-model with distinctive features (vitiligo, silver hair, different eye colors) shows identity holds when the features are rigidly set on the card: in the lesson videos the vitiligo pattern, hair and outfit do not float over all 14 seconds, and the background stays still. Hands and fingers break on fast gestures, and hair edges on turns. Movement needs reference videos with no zoom and no shake.

03.72. A frame for motion control: vertical 9:16, medium-full shot from the knees to above the head, a locked-off camera, the character at the same scale and angle as in the reference video.

03.73. A talking-avatar model (replacing yourself on a talking-head frame): chest-up shot, vertical 9:16, static camera; speech and mimic are kept from the recording, and the character's features go on top of the face (gray curls, freckles, blue eyes, pigment on the hands). The features must follow the face topology on turns and blinking. Artifacts: smoothing of skin and teeth, a seam on the border of hair and background, a hand with an object.

03.74. Stylizing a real performance into a fictional hero (blue skin, dots, braids) works as video-to-video: real clothes and objects stay stable. Artifacts: different irises on fast mimic, a sharp neck cut at the collar, real teeth inside a changed jaw, flicker on the border of hair and cloth. Emotion and speech carry over from the person.

03.75. For a round video message format (a messenger "circle"): the video up to 16 MB, preferably square, the face in the center.

03.76. A UGC factory: three inputs (product photo, description, shooting type); the network assembles eight characters for the product's target audience, writes each its own ad text with a hook and reveal, and animates the photo (clean speech, readable text on labels). The character is picked for the audience, not one for all videos. On negatives (resolved by model): Seedance 2.5 takes a short negative of concrete problems (`Avoid jitter, bent limbs, face drift...`); Kling 4.0 has no separate negative, only `no subtitles` and `no background music`; MiniMax is described positively; Nano Banana Pro takes positive wording only, negatives are not supported; GPT Image takes a "without..." block; Midjourney takes `--no` with 3-5 exclusions. Write only what applies to the scene.

### Studio additions (taste and order; the user may change them)

03.77. Real people: faces first. Start with a pack of references (3-5 photos per person, front, 3/4, different light), one approved portrait per person, one job per person, and the user approves faces before scenes. In a scene use at most 2-3 named people. Spend on full sets only after faces and the storyboard are approved. Before saying "similar", cut the face out at full size and put it next to the reference photo; if in doubt, say you are not sure.

03.78. The common character block holds only stable facts (hair, clothes, wear), never the facial expression: expression goes into the acting of each shot. Compare every frame of the scene with the approved character card: did the character become younger, cleaner, cuter? If yes, fix it before animation.

## Workflow

1. Interview with the 7 questions and choose card types (03.15). Generate nothing until the answers.
2. Real person: record a video reference (03.09) or a photo base of 5 angles with emotions and details (03.05-03.07).
3. An invented character: a description from the agent, 2 prompts, 4 generations of each, choose; then face angles one by one as separate 4K generations; then a full-length figure in the needed clothes; join into one sheet (03.17).
4. For each look (change of clothes) a separate figure and a new card; clothes described in text by the agent (03.23).
5. Clothes and product cards (4 sides, details), cards for recurring objects and locations (several angles in a card).
6. For each episode in one location: a setup frame from the cards (dozens of generations, several models), tune the color.
7. Write the role of each reference: what we take, what we do not take; pose and emotion go into the acting of the shot.
8. Fix the order of references (numbers in the prompt match the upload order).
9. Go through the checklist below, show the user, wait for "ok". Practice task: take your storyboard from stage 01 and make reference cards and setup frames for it, then assemble the first video shot from them. Start with one scene.

Image generations here are paid. Before any run: check `models_explore`, run `estimate_image_cost`, send the price message with the stage checklist and yes/no per item, and wait for an explicit "yes" on the exact list (model, number of jobs, credits).

## Formulas

Character replacement:

```
[action command] + [new character] + [link to surroundings] + [style preservation]
```

Two-photo link:

```
Use [Photo 1] as the base for background and composition. Replace the character in it with the person from [Photo 2]. Critically important: the new character must take exactly the same pose and have the same lighting as in [Photo 1].
```

Identity Lock:

```
Keep exactly the same facial features as in the reference images:
the same eyes, the same nose shape, the same jaw line and skin texture.
The face is recognizable as the same person.
```

Reference-card join request (to the agent):

```
Assemble the character reference card. The folder has three portraits (front, three-quarter, profile) and a full-length photo.

1. Three faces, large, each at full sheet height, do not shrink them more than needed.
2. From the full-length photo cut the head off at the chin: the face is taken only from the portraits.
3. All in one row, even gaps, no captions, frames or text.
4. Save as PNG and show me.
```

Detail edit: "keep the girl from photo two unchanged, same face, same features, same skin tone, same pose, same clothes, same background and light, change only makeup and hairstyle. And then in detail what exactly about the makeup."

Master identity block (order matters: models weigh descriptors by position):

```
[NAME], [age range], [ethnicity / skin tone],
[hair: color, length, texture, style],
[eyes: color, shape, size],
[face: shape, jaw, cheekbones, nose, lips],
[distinctive features: moles, freckles, scars, etc.],
[body: height impression, build],
[default expression / energy]
```

Long forms (skeleton and 7 prompts of the neuro-double, emotion prompt, neuro-model and avatar prompts, look and location prompts, fashion anchors, the consistency method with 5 card types, the identity-drift diagnostic table, replacement prompts, style transfer, roles for references) are in `templates/characters-and-refs.md`.

## Check before "ok"

Before generation:
- [ ] The interview is done, the type of each card is chosen by the answers.
- [ ] Real person: a video reference with head turns, speech and a smile.
- [ ] Realistic character: three 4K faces separately plus a body with no head, joined into one sheet.
- [ ] Clothes: a card from 4 sides plus close details plus a description in the prompt.
- [ ] Product: its own card for each item plus a description in the prompt.
- [ ] Each episode in one location has its own setup frame.
- [ ] The setup frame is put under all storyboards of the episode and into video generation.
- [ ] Cards have a plain background, even light, no text or frames, one object per card.
- [ ] In the prompt each card has a role: what we take and what we do not; pose and emotion are in the acting of the shot.

Production checklist:
- [ ] Close-ups of the face are made: front, three quarters, profile.
- [ ] The full-length character is made and the extra is cropped away.
- [ ] The card is assembled and labeled.
- [ ] The full-length figure has no small face unless needed.
- [ ] Clothes are described by the agent.
- [ ] Every prompt has a link to the card and the clothes description.
- [ ] The setup frame is put into every generation.
- [ ] Recurring objects (car, product) have their own cards.
- [ ] Reference cards cover everything that appears more than once; face and body were built separately; the order of references in the prompt matches the upload order.
- [ ] Clothes, features and textures match the moodboard; the setup frame is one per scene, with light and palette from the moodboard.

For a double: "I believe it" (or the result is liked more than in life); the set of front, 3/4, profiles, full length and emotions is present.

Face check: before saying "similar", cut the face out at full size beside the reference photo; if in doubt, say you are not sure.

A priced "yes" was given for every paid generation, with the stage checklist.

The stage closes only on the user's "ok".

## Common mistakes

- Generating before the interview; two characters or two products on one card; a motley background, hard shadows, captions, frames, arrows or text on cards; skin retouch; editing the old card on top; carrying pose, expression and background from a card; synonyms in the clothes description; an outside tool with no face lock for the face of a specific person; all 6 angles on one sheet.
- A classic card for realism; leaving a small face on the figure; relying on "take the character from the card" with no clothes description; not making cards for recurring objects.
- A whole person in several angles at once ("three different people"); patching the old prompt instead of a new one with a reference; editing a detail with no ban on touching the rest; mixing the order of references; not telling the agent what happens in the workflow (a prompt "in a vacuum").
- A face in one angle; a wide-angle phone lens (x0.5, x1) and x4 when shooting; photos that do not look like you; old photos left in the dialog when generating smiles; tattoos hidden by clothes.
- Twisting a finished picture (the image model eats quality); the command "change the face to the model"; a single reference image; changing several variables at once; forgetting accessories and makeup in the first prompt.
- An unstructured replacement prompt, no canvas and donor named, starting again because of clothes, an unrealistic insert.
- Feeding moodboard references into every storyboard frame; changing clothes from someone else's photo without cropping the head; leaving out the reference card description in the setup frame; asking for a "photo from another angle" with no description.
- A reference video with zoom and shake; the character on the photo at another angle and distance; animation with no upscale (a 15-20% loss).
- The card's background and "own environment" showing up in the frame (a studio in car windows).
- Plastic skin from an overly smooth card.
- Inventing character features: always confirm with the user first.

## Tools

| Tool | Role in this stage |
|---|---|
| Higgsfield `nano_banana_pro` | 4K faces by angles, neuro-double, look, replacement, edits, setup frame; up to 14 references (optimum up to 6), up to 5 humans in a scene; native 4K |
| Higgsfield `gpt_image_2_6` | figure, locations, setup frame, clothes and product cards; holds a face through about 10 redos; up to 16 references |
| Higgsfield `seedream_v5_pro` | the same setup-frame prompt run through several models; check moderation of looks in advance |
| Higgsfield `soul_2` | optional character-oriented image model; check `models_explore` for what it does now |
| Higgsfield `seedance_2_5` | a person video reference (`@Video`) and reference cards as `@Image`; check the real-face rule (03.69) |
| Higgsfield `kling4_0` and motion control | animate a photo from a reference video; video element of a person |
| Upscaling: `bytedance_video_upscale`, `topaz_video` (paid) or a local upscaler; skin enhancer | upscale and skin texture; upscale a double photo before animation |
| The agent (Claude Code or similar) | join the card in one row with a short script, describe clothes, keep the reference folders, write prompts |
| Pinterest, an LLM for photo descriptions | references of look and location, descriptions of photos, prompts |
| A 3D-world-from-one-photo tool | optional: another angle of a location (quality lower) |

How to save characters as reusable elements on Higgsfield is in `docs/higgsfield.md`. Check `models_explore` for current models and `estimate_image_cost` or `estimate_video_cost` for the price in credits before any paid run. Nothing paid runs without the user's explicit "yes" on the exact list (model, number of jobs, credits from the estimate). The price message includes the stage checklist with yes/no per item and names any move that is not the method as a deviation.
