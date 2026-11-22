# Film language

A practical reference for describing frames to image and video models: shot sizes and angles, composition, lenses, camera movement, light, emotions, how a character moves, genres, one-take shots, film look, and a style block to paste into prompts. Prompt phrases are in English because the models read English best.

Used at stage 02 (`docs/stages/02-film-language.md`) and again whenever the agent writes a frame prompt (stage 04), a camera line (stages 05-06) or a director note (`templates/script-and-storyboard.md`).

## The core rules

1. Describe the frame, not the event. "They fight in a shop" is an event. A frame is:

   `[lens] + [camera position and height] + [camera movement] + [composition by thirds] + [light inside the frame] + [what is out of focus]`

   Every storyboard segment needs all six. Any element you leave out, the model chooses itself, and it usually picks the boring default (eye level, 50 mm, centered, flat light).
2. Context before shots. A video model must understand the story first. Open any story prompt with a SCRIPT block: genre, stakes, the characters' motivation, what this is not, the place in the story. Then the storyboard directs.
3. Optical rhythm. Alternating lenses is editing rhythm. Wide (14-24 mm) means chaos, scale, chases, comic distortion, everything in focus. Long (85-135 mm) isolates a gag or an emotion and turns the background to mush. Chaos on wide, punchline on tele. Contrasting focal lengths between neighbor shots read as expensive editing. Never two neighboring shots on one lens by accident.
4. Depth from three layers. A flat frame is fixed with a blurred foreground (a shelf corner, a shoulder, an object), a sharp subject, and a background in haze or light about 1 to 1.5 stops darker. Check every frame for a foreground you can add.
5. One light for the whole video, named in every segment.
6. Name the format first (aspect ratio, deliverable). Name the frame size at the start of the prompt: `extreme wide establishing shot`, `medium shot`, `close-up`, `extreme close-up`.
7. Lens lock inside one video: one focal length for the clip, change the framing by moving the camera, or fix a field of view per segment.
8. Write screen direction and transitions in the prompt ("screen direction never flips"). Vague transitions are the most common reason a sequence falls apart.
9. Real footage has accidents, AI footage usually has none. A touch of imperfection (handheld sway, a focus hunt, something walking through the frame) adds realism.

Check before showing a storyboard:

1. A SCRIPT block with genre, stakes and motivation exists.
2. Every segment has all six frame elements.
3. The hook is in the first 1.5 seconds and is the most catching angle of the video.
4. Lenses alternate.
5. The arc goes from wide to close (or consciously the reverse).
6. One light for the video, named in each segment.
7. Speeds alternate with meaning: slow motion only on gags and beauty.
8. Sound is written, and in slow motion the sound stretches and dulls.
9. For a one-take, there is a cut substitute every 8-10 seconds, movements are paths, and the frame never widens back.

## Shot sizes and what they say

| Size | Question it answers |
|---|---|
| Wide / establishing | Where are we? What is this world? |
| Medium | Who is this? What are they doing? |
| Close-up | What do they feel? |
| Extreme close-up | What should I look at right now? |

Pre-generation check: where does the viewer enter the scene (wide)? When do they come close to the hero (medium)? Where must they feel, not just see (close)? Is there one detail worth an extreme close-up? With answers to all four, you are staging a scene, not just generating frames.

The camera as a character:

| Camera | How it shoots |
|---|---|
| Observer | Stays put, medium shots |
| Peeping watcher | Wide shot and slow zoom |
| Conversation partner | Close-ups at eye level |
| Pursuer | Moves behind the hero, handheld |
| Judge | Extreme close-up accents on details |

## Angles and camera position

Prompt template: `<angle name> of a woman <detail>` or `of this woman` when a character reference is attached. Tested with `nano_banana_pro`: create the character first, then try the angles and locations.

Angles that work as prompt openings: establishing shot, eye level, high angle, low angle, dutch angle, profile, three-quarter, close-up, extreme close-up, medium (chest up), full body, cowboy (mid-thigh up), over-the-shoulder, back view, silhouette against a bright background, reflection in a mirror, bird's eye (directly above), worm's eye (ground level), candid, frame within a frame (through a window), leading lines, environmental (in her setting), dramatic side lighting, motion blur, high-angle selfie, overhead (with a described desk scene), overhead from behind, insert (only the hands visible).

Short examples: `low angle shot of a woman shot from below`. `over-the-shoulder shot of this woman, a man sits across the table, the camera films her from behind his shoulder`. `insert shot of a woman typing on a typewriter, many papers on the table, only her hands visible`.

What height and angle mean:

- Eye level: neutral.
- Low (from the floor up): power, threat, monumentality. In comedy: pathos set up to be broken.
- High (from above): vulnerability, smallness, being watched.
- Top-down 90 degrees: ornament, scene geography, a breather.
- Dutch 5-12 degrees: unease, instability. In action comedy: energy.
- POV: involvement, "I am there".
- Over-the-shoulder: dialogue, confrontation.
- Ground level (20-30 cm): feet or wheels, speed, a pressing space.

Composition:

- Thirds: key objects on the lines or intersections. Say it: "face in the right third, bag enters from the left".
- Three depth layers (see core rule 4).
- Leading lines: shelves, corridors, light beams lead the eye to the target.
- One-point symmetry: ceremony, ornament, a long corridor.
- Negative space: emptiness as waiting or loneliness.
- Frame within a frame: doorways, mirrors, shelves isolate a character.
- Foreground framing: always look for something to "dirty" the edge of the frame.

Coverage from a master frame: build one master shot, then ask the image model for close-up, two-shot and wide that keep characters, light, palette and film stock. Lock one scene image and change only the camera line (smooth pan, handheld, overhead) to get a coverage set from one look.

## Lenses and aperture

What the lens choice gives:

- Perspective and distortion: 14 mm distorts space dramatically, 50 mm looks like the eye, 200 mm compresses and pushes the background onto the subject.
- Depth of field: 85 mm at f/1.4 gives creamy bokeh, 24 mm keeps nearly everything sharp.
- Emotion: wide (14-24 mm) adds epic scale and drama, tele (135 mm and up) adds intimacy and isolation.
- Genre code: macro says product detail, 70-200 says reportage or sport, fisheye says skate culture and action.

| Focal length | What it does | Use for |
|---|---|---|
| 8-16 mm ultra-wide, fisheye | Space flung open, barrel distortion, near objects huge, speed exaggerated | Chaos, chases, hook frames, comic distortion, interiors, astro |
| 18-28 mm | Wide working range, lots in frame, little caricature | Architecture, landscape, documentary context |
| 35-40 mm | Honest cinema, mild width | Street, everyday scenes |
| 50-55 mm | Human eye, neutral, documentary | Portraits, most scenes |
| 60-105 mm macro | Textures, products, drops, eyelashes | Product, jewelry, insects |
| 85 mm | Portrait, isolation, flatters the face, background melts | Portrait, romance |
| 135 mm and longer | Space compressed, surveillance, claustrophobia, subject cut off from the world | Isolation, sport, wildlife |
| Anamorphic | Oval bokeh, horizontal flares, "expensive film" | Widescreen cinema look |
| Tilt-shift | Miniature effect, selective focus plane | Miniature city, corrected architecture |

Aperture:

| f-stop | Effect |
|---|---|
| f/1.2-1.4 | Ultra-shallow, creamy bokeh, portrait isolation |
| f/1.8-2.0 | Soft background blur, selective focus |
| f/2.8 | Moderate depth, background blurred but recognizable |
| f/4 | Balanced sharpness, a cinematic default (use f/1.4-2 only for portrait close-ups) |
| f/5.6-8 | Extended focus, travel and landscape |
| f/11-22 | Everything sharp, technical and architectural |

Ready combinations:

- `85mm portrait lens at f/1.4, creamy bokeh` (maximum blurred background portrait)
- `24mm wide-angle at f/8, landscape depth` (everything sharp)
- `50mm prime at f/2.8, balanced depth of field` (universal controlled blur)
- `200mm telephoto at f/2.8, compressed perspective with soft background` (sport, fully blurred background)

Lens as intent: 24-35 mm shows the world, about 50 mm natural conversation, 85 mm and up isolates the subject. Anamorphic: `2.35:1 widescreen, oval bokeh, horizontal lens flare`.

## Camera movement

One movement per shot. Prefer subtle over aggressive. In `seedance_2_5`, push-in, pull-out, pan, tilt, orbit, crane, static, handheld and a slow-motion ramp are reported to work reliably; dolly zoom works only partly and whip pan is inconsistent (community reports, check with a short test). `kling4_0` may drop camera moves after the third in one prompt. Some models over-stabilize handheld, so write "micro-jitter" or "true handheld with light shake".

Five-part line for each move, kept separate from the scene description so the same camera line can be reused when the first frame changes:

`<move name>. Movement: <what the camera physically does>. Speed: <pace>. Framing: <what stays readable>. End: <final composition>.`

Example: `Slow dolly in. Movement: the camera moves physically forward in a straight line toward the subject. Speed: smooth controlled push. Framing: height, lens direction and subject position stay the same while distance closes. End: a tighter composition.`

Move library, by group:

- From a fixed point: static (locked-off, hold one position), pan left/right (horizontal rotation, horizon level), whip pan (fast snap, brief motion blur, land on a sharp second target), tilt up/down (vertical rotation).
- Lens only (the camera does not move): slow zoom in/out, fast zoom, crash zoom (snap, punchy, for accent).
- Straight-line body moves: dolly in/out, truck left/right (sideways), pedestal up/down (whole camera lifts), slider (small slow slide, parallax), push past (glide past a foreground object into the space beyond).
- Around the subject: arc left/right (shallow curve), orbit clockwise or counterclockwise (full circle at constant radius, subject centered).
- With the subject: tracking (match their pace), follow from behind (shoulder height), reverse tracking (backward in front of a walking subject, walk-and-talk), side tracking (parallel, profile view), low tracking (ground or below-waist, footsteps or wheels), vehicle tracking, chase (fast, close, reactive), handheld (operator height, natural sway), body-mounted (camera fixed to the torso or face while the background moves), first-person view (hands or arms visible).
- Vertical and aerial: crane up/down, drone push-in or pull-back, helicopter-style flight.
- Special and transition moves: tilt-shift miniature, infinite zoom into the next world, earth zoom out (street to planet), locked-camera time-lapse, pass-through (move toward a surface or opening and continue into the space beyond).
- Combined: push in with tilt up, orbital descent (circling while lowering to eye level), jib sweep (low to high arc), vertigo or dolly zoom (dolly back while zooming in, once per video), floating drift (slow forward and slightly upward, dreamlike), gimbal rotation.
- Reveals: pull-back reveal (start tight, pull back to show an unexpected environment), focus-pull reveal (start fully out of focus, pull to razor sharp), extreme macro zoom (from a portrait into the iris and beyond), cosmic hyper-zoom (space to street).

Meaning of movement:

- Static: observation, tension, a gag "in the frame".
- Slow dolly in: attention narrows, anxiety or realization.
- Dolly out: loneliness, scale revealed, endings.
- Side tracking: a journey together, a parade of details.
- Retreating in front of the subject: a chase toward the camera.
- Arc or orbit 30-90 degrees: heroizing a moment, inspecting a frozen instant (slow motion).
- Snap zoom: a comic or reportage accent.
- Handheld: panic, documentary, here and now.
- Crash zoom plus micro shake: fashion or VHS energy.

Speed:

- Slow motion: beauty, gag, realization. Only on peaks, never more than 3 seconds in a row.
- Speed ramp: normal, slow at the peak, sharp return. Sound stretches and dulls in slow motion and explodes at the return.
- Time-lapse or hyper speed: time as a character.

Realism tricks: handheld, crash zoom, a voyeur view, whip pan, walking backward, something passing in front of the lens, exposure shift when going indoors to outdoors, focus hunting. Combine several. Camera is a cheap variable: one scene image, many camera lines.

## Light

"Cinematic lighting" alone is too vague. Name the source, its direction, its quality, and what it does to the face. Lighting is the largest single quality lever. Settle the light in the image before any motion.

Quality: hard (small source, sharp shadows), soft (large source, gentle shadows), diffused (through a diffuser or bounced), direct, ambient, natural (sun, moon, sky), artificial, candlelight (very warm about 1500 K, flicker), neon glow, fluorescent (cold, slightly green), tungsten (about 3200 K, yellow-orange), spotlight, floodlight, specular or chrome light (mirror-like highlights on glossy surfaces), overcast (soft, even), golden hour, blue hour (cold, blue, detail in shadows), screen glow (colored, lights part of the face), flickering (broken lamp, fire, old TV), continuous, strobe or flash.

Position and function:

- Key: the main and strongest source. Shapes volume and main shadows, usually 30-45 degrees to the camera.
- Fill: weaker, opposite the key, softens its shadows.
- Back light and rim or hair light: separate the subject from the background with a glowing contour.
- Background light: lights only the background.
- Kicker: side-back light that picks out part of the contour and texture.
- Butterfly (key directly above the camera, a shadow under the nose, glamour), Rembrandt (a light triangle under the eye on the shadow side, very dramatic).
- Side light (90 degrees): maximum texture, sharp contrast. Top light: deep eye sockets, can be sinister. Under light: unnatural, "horror" shadows.

Image characteristics: contrast (high: deep shadows, few midtones, noir; low: many midtones, soft shadows), low key (dark tones dominate, mystery, noir), high key (light tones, minimal shadows, optimistic), hazy or foggy, lens flare, glow, shade and shadow, reflections, hotspot (overexposed area), specular highlights.

Light in the frame description (at least one line per segment): name the source, direction, temperature and what is in shadow. A backlight from depth gives silhouettes and halos, side light sculpts the face, underlight gives unease. Haze (powder, dust, smoke) makes light visible, so motivate it with the story.

Working practice:

- Three-point roles, near 2:1 key to fill for soft, 3:1 for more contrast. Wording: "strong key from camera-left, soft fill from camera-right, subtle hair light".
- Source plus direction, not "soft light": "soft north-window key from the left, low fill", "late-afternoon light raking across the workbench", "a thin rim of light along the edge".
- Motivated light and practicals: every light in the frame has a reason ("lit by the harsh fluorescent overhead and the green glow of a monitor"). Make the dominant source clear ("the bonfire is the dominant source, low, warm, orange, unsteady").
- One warm light in the dark and colour contrast: "hard cold key with a single warm accent", "warm gold and cool blue", "neon noir".
- Named looks: noir ("hard side light, deep shadows, venetian-blind pattern"), chiaroscuro, candlelight with soft three-quarter light.
- One dominant colour temperature per scene (about 3200 K tungsten or 5600 K daylight) plus a controlled secondary practical. The face is the brightest area. Protect highlights.
- Do not mix contradictions ("soft diffuse" with "razor-sharp shadows"). Test with a 5-10 second clip first.
- Low key describes contrast, not colour.

## Emotions on a face

Describe an emotion through physical features, not a label. The six features to cover: eyebrows (the key indicator), eyes (opening, direction, moisture), mouth, muscle tension (jaw, forehead, neck), skin color (flushed, pale), overall pose (head, shoulders, gaze direction).

Prompt shape: `Close-up of a character's face showing [emotion]: [brows], [eyes], [mouth], [tension], [skin], [pose]`.

| Emotion | Physical recipe |
|---|---|
| Joy | wide genuine smile with teeth, crow's feet, raised cheeks, brows slightly up, relaxed forehead, slight head tilt up |
| Sadness | mouth corners down, lower lip trembling, brows drawn together and angled up in the middle, glistening eyes, drooping lids, gaze down, pale |
| Anger | brows pulled down to the nose bridge, vertical lines between them, intense stare, flared nostrils, clenched jaw, thin lips or a shout, flushed |
| Fear | eyes wide with whites visible, brows high and together, horizontal forehead lines, mouth open or tight, pale, frozen |
| Surprise | brows high, eyes round, jaw dropped in an "O", brief frozen face, slight head back |
| Disgust | nose wrinkled up, upper lip raised, cheeks up, eyes squinted, brows down, head pulled back or away |
| Contempt | one mouth corner raised in a smirk, one brow slightly up, dismissive sideways or downward look, chin raised |
| Embarrassment | flushed cheeks, gaze away or down, shy smile, hand near face, shoulders slightly hunched |
| Guilt | downcast eyes, brows drawn with a slight furrow, mouth down, slumped shoulders, biting the lower lip |
| Pride | chin up, slight smile, confident gaze forward or up, chest out, shoulders back, relaxed brows |
| Envy | narrowed eyes fixed on the target, slight frown, tense jaw, sideways glance, tight mouth |
| Jealousy | intense stare, brows drawn into a deep furrow, clenched jaw, thin lips, flared nostrils, anger mixed with hurt |
| Anxiety | brows raised and pulled together, darting eyes, pressed lips or lip biting, tense jaw, pale or flushed, sweat on forehead |
| Hope | soft smile, bright eyes looking up or forward, brows slightly raised, relaxed forehead, warm skin |
| Disappointment | frown, lowered or half-closed dull eyes, brows drooping, deflated, shoulders slump |
| Relief | visible exhale, gentle smile, soft or half-lidded eyes, tension leaves jaw and forehead, shoulders drop, maybe tears |
| Love | warm smile reaching the eyes, tender gaze, relaxed brows slightly raised, glowing face, slight head tilt |
| Hatred | narrowed piercing glare, severely furrowed brows, clenched jaw, lips hard or in a snarl, flared nostrils |
| Boredom | drooping lids, distant unfocused gaze, flat brows, neutral or slightly down mouth, a suppressed yawn, head on a hand |
| Curiosity | wide alert eyes, raised brows, head tilted, mouth slightly open or pursed |
| Admiration | wide sparkling eyes, raised brows, mouth slightly open in awe or a soft smile, gaze fixed on the object |
| Sympathy | soft eyes, brows raised and together, soft frown or gentle smile, head tilted |
| Determination | jaw set firm, unwavering gaze forward, brows slightly lowered together, thin lips, slight forward lean |
| Confusion | asymmetric brows, one eye squinted more, head tilted, mouth twisted or open, maybe a hand scratching the head |
| Confidence | chin slightly up, steady direct eye contact, relaxed brows, slight smile, firm jaw, shoulders back |
| Shame | eyes down, brows together and raised in the middle, flushed, hands covering the face, shoulders hunched inward |
| Delight | brilliant smile with teeth, sparkling crinkled eyes, raised brows, cheeks high, head slightly back |
| Nostalgia | dreamy distant gaze, soft smile of memory, slightly unfocused eyes, happiness mixed with melancholy, moisture in the eyes |
| Peace | eyes gently closed or half-lidded, all muscles relaxed, slight gentle smile, smooth forehead, calm breathing |
| Panic | eyes extremely wide, brows at maximum, mouth wide open or gasping, pale or flushed, trembling features, tense everywhere |

Build emotion up to its peak across a shot sequence rather than putting maximum emotion in every frame.

## How a character moves

Short phrases that models read and render well. Use one or two per shot, and add micro-motions for realism.

- Walking and approaching: `walking toward camera with steady pace, natural motion, frontal perspective` (reads face and detail); `calm walking pace looking at camera`; `slow cinematic walk past camera, slight head turn, natural confidence` (stylish intro); `walking sideways in profile, smooth lateral motion` (fashion, character reveal); `walking away from camera, confident back view` (scene endings).
- Running and action: `running with dynamic motion, arms driving, realistic stride`; `intense sprinting, explosive leg drive`; `chase scene running, fast pursuit energy`; `jumping with extended legs, athletic leap`; `boxing punches, athletic fighting motion, aggressive stance`.
- Dance and grace: `dancing with fluid body motion`; `contemporary dance, expressive flowing motion`; `spinning 360 degrees, graceful rotation, ballet-like motion`; `twirling in dress, fabric flowing, playful spin`; `yoga pose transition, flowing movement, mindful body control`.
- Talking and gesture: `expressive hand gestures while speaking`; `big expressive gestures, animated body language`; `sitting and leaning forward slightly while speaking` (intimate, confessional); `pointing gesture, directing attention`; `crossing arms confidently, strong stance`.
- Stillness and life: `standing still with subtle body sway, natural breathing motion`; `leaning casually against a wall, relaxed posture, minimal movement`; `idle movement, small unconscious gestures, realistic micro-motions` (the most important for realism: adjusting clothes, shifting weight, small gestures).
- Turns and looks: `turning head slowly toward camera, controlled deliberate motion` (strong hook, a moment of contact); `slow body turn, 180-degree rotation, smooth controlled motion` (character introduction); `looking over shoulder, mysterious glance back, cinematic timing`.
- Drama and accent: `sudden stop movement, sharp pause, intense body control` (cut-off action); `crouching down slowly, controlled descent, dramatic pose`; `kneeling down gracefully`; `collapsing dramatically, emotional breakdown, theatrical fall`; `reaching toward camera, extending arm, emotional connection`; `pacing back and forth, nervous energy`.
- Light and playful: `laughing with natural facial motion, loud laughter`; `playful bouncing steps, light energetic motion`; `slow exaggerated motion, almost slow-motion body language` (surreal or comedic); `blowing kiss gesture`; `hair flipping motion, fashion editorial style`; `hand through hair, casual elegance`; `brushing off shoulders, confident dismissive gesture`; `stretching arms upward, morning routine feel`.
- Reactions: `catching falling object, reactive motion, quick hand movement`; `stumbling forward, losing balance, natural recovery motion`.

Rule: write movement as an action with a speed and a quality ("slow, deliberate"), never only a mood.

## Genre playbook

One genre is one coherent set of choices. Do not mix sets inside a video without reason.

- Thriller and noir. Lens 35-50 mm base, tele for surveillance (compression equals claustrophobia), wide for disorientation in tight spaces. Dutch angle (the world is wrong), high angle (victim), low angle (threat), POV. Light: low key, one hard source, deep shadows, half-lit faces, backlight, blind stripes. Movement: slow creeping pushes, static watching shots, a rare dolly zoom at the realization. Rhythm: long takes, then a sharp burst, silence before the hit.
- Horror. High angle (watched, small, vulnerable), tilts as "camera is the victim on the floor", mirrors and reflections. Wide with distortion for an unhealthy space, long-lens surveillance from hiding. Light from below the face, single practicals in darkness, silhouettes in doorways. Slow push toward a door or corner, handheld for panic, a static shot where "something is wrong". Technique: negative space, an empty half of the frame where something should appear.
- Comedy and action comedy. Wide (14-24 mm) exaggerates movement and features. Fisheye as a funny mirror, used sparingly. Tele isolates the punchline. Devices: snap zoom on a gag, extreme close-ups of everyday actions, fast cuts on sound beats, a gag in the background while the foreground is serious, breaking a cliche (the hero jumps the fence in style and the fence breaks). Light: high key, brighter than average, readable faces, but keep it cinematic with backlight and atmosphere. Rhythm: setup wide, punchline close, slow motion on the absurd moment.
- Drama and romance. 50-85 mm, natural flattering perspective, shallow depth for intimacy. Eye level, over-the-shoulder for dialogue, moving closer to faces as emotion grows. Soft light motivated by windows, warm skin, diffusion or bloom for romance. Slow "breathing" moves, static on the key line. Slower editing, pauses work.
- Documentary, mockumentary, UGC. Zooms 24-105, a "found" frame, sometimes slightly missed focus and reframing. Handheld with natural breathing, sharp pans to an event, snap zoom as in reportage. Available mixed light, honest blown-out windows. Interview static at 35 mm with live cutaways, a look at the camera for mockumentary.
- Action and chase. Wide close to the body means speed. Long lens across the movement makes the subject "run in place" in a compressed space. Camera retreating in front of the chase, side tracking, low at ground level (wheels, legs), FPV flights. Shots get shorter toward the peak. Speed ramp: ramp up, slow motion at the stunt peak, sharp return. Cut on sound hits.
- Ad and product. The product is a character: a hero shot on a pedestal of light, macro of texture, slow motion on interaction. Macro for textures, 85 mm for the product in hand, wide for the brand world. The product always has the best light in the frame, with its own rim. Final: product plus slogan held 1.5-2 seconds.
- Music video. One visual motif per clip (light, color or place), camera movement on the beat, slow motion on hooks, symmetry and ornamental top-downs as breathers.

## One continuous shot (oner)

A shot with no cut. Costly and gripping, and possible because video models generate continuous takes natively.

Why it works: real time (events are not compressed, so the brain believes it), no escape (a cut is always a micro-rest for the viewer), the space feels real (no cut where you could be fooled), density of attention (longer holds need more information tracked over time), and a clean trick (people rewatch to find the cut, and rewatch is a metric). In a feed where clips are 40-50 seconds and self-contained, a minute of continuity stands out by itself.

Main problem: rhythm. Editing is rhythm, so remove cuts and you must replace them. Five cut substitutes:

| Device | How it works |
|---|---|
| Change of setting | Street, then car interior, then entrance hall. Each transition is an event |
| Reveal | The camera pulls back and shows what we did not see. A "hit" in place of a cut |
| Scale shift | A close-up flows into a wide and back. One shot, different sizes |
| Entering and leaving | Someone enters, someone leaves. The cast changes without a cut |
| Speed change | The camera holds still, then rips. The difference in pace is the rhythm |

Rule: at least one substitute per 8-10 seconds. A one-minute take holds 6-8 events or it falls apart. Passing through a window, door, arch or gap is the strongest substitute because it combines a change of setting, a reveal and a scale shift in one move.

Three rules for AI models (learned from practice):

1. Path, not points. If you describe a start and an end position with no route, the model connects them with a cut, the cheapest way.
   Bad: `The camera overtakes the car on the left and ends up facing it head-on.`
   Good: `The camera stays at window height and slides forward along the left side, overtaking the car. Passing the lens in order: rear fender, rear pillar, lowered window, the heroine's elbow on the door edge, side mirror, front fender. Even movement, no jerks.`
2. The frame only narrows. On a continuous push-in, never describe in the next block something that no longer fits the frame. The model resolves the contradiction by widening with a cut. Each block describes a subset of the previous one. To show the wide again, write a separate pull-back as a movement.
3. Continuity marks between blocks. Time-coded blocks inside one take must each continue the previous one: `[12s-15s]: the camera continues the same arc without stopping...` The words "CUT" and "switch to" are banned inside a take because they invite the model to cut.

Hidden joins, for when a long video is built from several generations: pass behind an object (a pillar, a wall, a character's back), a whip pan (the seam is hidden in the smear), a fade into black, white or smoke, a pass through a dark zone (tunnel, doorway, shadow). Plan the join in advance and place it where the camera is moving and the picture is smeared.

Trap: a long take is not made for its own sake. Ask first: what does this scene lose if it is cut? If the answer is "nothing", skip it. Good reasons: mounting tension a cut would reset, proof of real space, one emotional arc, a reveal that only works if the viewer trusts there was no edit.

Oner checklist:

1. You answered "what does the scene lose if cut".
2. A cut substitute at least every 8-10 seconds.
3. Every camera move is written as a path.
4. The frame never widens back after a push-in.
5. Continuity marks between blocks, no CUT.
6. If several generations are joined, the seam is in a smear or behind an object.
7. Light works from every side the camera will pass.
8. Choreography of characters and objects is written before the camera move, not after.

## Film look, effects and realism

Film look lives mostly in the light. Grain and grade are the seasoning. If a frame is "not cinematic" with right grain and grade, the problem is flat multi-source high-key light.

### Principles

1. Clean gives away digital. Film signs: halation (a warm glow around bright sources), lifted blacks (milky, no pure black), organic grain that is uneven (denser in shadows), soft highlight roll-off, slight optical softness instead of digital sharpening.
2. A named film stock beats the word "cinematic". Models know the color science of real stocks. One stock per prompt, no mixing.
3. Style without a scene creates a new scene. In image-to-image, write a SCENE LOCK first, then the style.
4. In image-to-image, transformation dominates. If the "keep" block outweighs the "change" block, the model returns the source. Put the transformation first with force ("STRONG, clearly visible") and keep the preserve line short.
5. Contradictions kill a prompt. "clean sharp focus" with "slight softness" makes the model ignore both. Check for mutually exclusive commands before sending.
6. A reference image beats text style. Glossy references pull the result to their look and ignore the film look in text. Fix: state the roles ("references only for face identity and location, do not take style or grade from them, style strictly from the description below") or degrade the references with a film pass.
7. Too-clean references give plastic in video. A sterile image is out of distribution for a video model. Before feeding a reference to Seedance, soften it slightly (grain, 5-10 percent soft blur or a film grade). Skin enhancers and sharpeners only after video generation, never before.

### Film stocks and cameras

Pick a stock by genre and mood. Use one.

| Genre or mood | Stock | What it gives | Key tokens |
|---|---|---|---|
| Crime thriller, lamp-lit interiors, night | Kodak Vision3 500T | Tungsten balance: amber lamps, cool teal shadows, dense grain, strong halation | `Kodak Vision3 500T, tungsten interior with cool window spill, rich teal shadows, glowing halation around tungsten lights, textured grain` |
| Warm drama, portraits, daylight | Kodak Portra 400 or 800 | Warm creamy skin, fine grain, soft overexposure | `Kodak Portra 400 color science, warm creamy skin tones, slight highlight overexposure, very fine organic grain` |
| Neon night, city, signs | CineStill 800T | Signature red halation around neon, moody night | `CineStill 800T, signature red halation around neon lights, moody nighttime tones` |
| 70s retro, faded family archive | Kodak ColorPlus 200 or Gold 200 | Faded warm palette, soft edges, print texture | `Kodak ColorPlus 200 palette, soft focus edges, gentle vignette, scanned print texture, slight color fade` |
| Cold nature, greens | Fujifilm Pro 400H | Cool greens, soft pastel | `Fujifilm Pro 400H, cool greens, soft pastel rendering` |
| Hard black and white, documentary | Kodak Tri-X 400, Ilford HP5 | High contrast, heavy grain | `Kodak Tri-X 400 pushed, high contrast black and white, heavy grain` |
| Found footage, horror, glitch retro | Expired film | Light leaks, purple shift, dust, scratches | `expired film stock, light leaks from frame edge, purple color shift, dust and scratch textures` |

Other stocks and cameras in the same family: Kodak Ektar 100 (saturated, clean), Cinestill 50D and 400D (daylight cinema), Fuji Velvia 100 (hyper-saturated), Agfa Vista 200 (faded 90s), Polaroid SX-70 (pastel vintage), Lomography Redscale (red-orange shift), Rollei RPX 25 (ultra-fine grain), Ferrania P30 (contrasty black and white, neorealism). Cameras: Arri Alexa 35 (soft digital cinema), shot on 35mm film (honest film), Leica M10 or M6 (soft, soulful), Hasselblad (medium-format luxury), Canon R5 or Sony A7R IV (sharp, clean digital), GoPro (wide, edge distortion, motion energy).

### Effects words

Film grain, lens dust and scratches, chromatic aberration on the edges, light leak or bloom from the corners, floating particles (dust, steam, frost), vignette, motion blur, bokeh circles, double exposure, color shift or cast, halation, overexposure (blown highlights), underexposure (crushed blacks), visible sprocket holes, frame border, cross-processing, infrared look, sepia, desaturated colors, film burn, rainbow flare, dust motes in a light beam, soft focus, anamorphic horizontal flare, date stamp overlay. Place effects at the very end of the prompt.

Final style phrases for the end of a prompt: `feels surreal yet editorial`, `hyperreal, stylish, tactile and strange`, `high-fashion campaign with absurd twist`, `looks expensive, feels spontaneous`.

### Ultra-real "phone photo" look

For an everyday, unretouched image: `amateur photo, candid pose, photo shot on iPhone, casual framing, slightly tilted, visible skin texture, pores, RAW iPhone look, clear background`. If it still looks too perfect, add `JPEG compression` (artifacts) or `slight motion blur` (hand shake).

### Template A, image-to-image film grade over a finished frame

```
Use the attached image as the base. This is an image-to-image color grade and film emulation
pass. Apply a STRONG, clearly visible cinematic transformation to the entire frame while
keeping the scene itself untouched.

SCENE LOCK:
The scene is exactly what is in the attached image: [1-2 sentences: location, characters,
key objects]. Do not invent a new scene. Same composition, same camera angle, same people,
same poses.

[Stock and base, for example:]
Teal and orange style, muted tones, cinematic shot, film grain effect, realistic, Arri Alexa 35, f/4.

LIGHTING
- Mixed color temperature: warm highlights on skin, cool cyan-green shadows.
- Faces partially in shadow, sculpted by light.
- Uneven exposure, imperfect falloff. Background slightly noisier than subjects.

FILM LOOK
- Real cinematic film still, not AI-clean.
- Organic film grain, uneven, clumping slightly in shadows.
- Gentle halation and bloom on highlights: [list the bright sources in the frame].
- Slight softness, no digital sharpening.
- Muted saturation, lowered midtones, lifted milky blacks, no pure black anywhere.

MOOD
[One line for the genre, for example: "Grounded crime thriller. Quiet danger. Control."]

PRIORITY RULE
If cinematic style conflicts with realism, realism wins. If lighting conflicts with identity,
identity wins. If style conflicts with the base image content, the content wins, but the
grade and film texture must still be applied at full strength.

Constraints: no new objects, no new people, no scene changes, no logos, no text, no watermarks.
```

Never add `clean sharp focus`, `4k ultra sharp` or `HDR` to this template. They fight the film look.

### Template B, bake the film into a from-scratch generation

Add this block at the end of a normal frame prompt (subject, action, environment, camera, lighting):

```
Kodak Vision3 500T color science, tungsten-balanced: warm amber from practical lamps, cool
cyan-teal daylight spill. Green-cyan tint in shadows typical of scanned negative. Soft highlight
roll-off, no blown whites. Gentle halation around bright light sources. Lifted milky blacks.
Fine organic film grain, denser in shadows. Slight chromatic aberration at high-contrast edges
near the frame borders. Subtle vignette. Slight optical softness, no digital sharpening.
Natural skin texture with visible pores and subtle oil, no plastic smoothing.
```

### Template C, low-key light for a "pretty but not cinema" frame

Use when light is flat, everything is visible and pastel. Put it into the generation prompt or give it as a relight edit.

```
Light: low key, exposure set for the highlights. The only source is hard [neutral milky white /
warm gold: choose and name it, or the model drifts to golden hour] sun from the window. The beam
cuts through haze as a visible knife of light and paints a bright stripe on [surface]. [Subject]
stands on the edge of the beam: light slides along [hair / shoulder / hands], half the face is in
deep shadow. All other sources are off: [lamp] is a dark silhouette. The rest of the scene sinks
into deep shadow: details are guessed, not seen. The window is bright, almost burnt out, with a
soft halo. Shadows are deep and slightly smoky in the darkest places. Dust or smoke glows in the backlight.
```

Why the commands work: "exposure for the highlights" sinks the frame to keep the window bright instead of lifting shadows. "Details are guessed, not seen" lets the model hide the furniture you described, otherwise it lights everything listed. "All other sources are off" is needed because mixed light from two windows and a lamp gives flat pastel. Name the temperature and also forbid the opposite ("no golden yellow"), because "cinematic" defaults to golden hour.

### Common film-look failures

| Symptom | Cause | Fix |
|---|---|---|
| Image-to-image changed nothing | The preserve block dominates | Put the transformation first with STRONG, keep preserve to one line |
| It generated a different scene | No SCENE LOCK | Add a SCENE LOCK describing the frame |
| Graded but looks digital | No halation or lifted blacks | Add both tokens explicitly |
| Plastic skin in video | References too clean, no skin block | Degrade references, add the skin block below |
| Burnt-out white window or lamp | No roll-off | "Soft highlight roll-off, no blown whites" |
| Style is there but realism slipped | No PRIORITY RULE | Add it from Template A |
| Grain and grade are right but "not cinema" | Flat high-key light | Template C |
| The text grade is ignored | Glossy references override | Separate the roles of references or degrade them |
| Light went golden yellow | Temperature not named | Name it: "neutral milky white, no yellow" |

### Film look in video (`seedance_2_5`)

Why video looks cartoonish with perfect references: the video model is trained on slightly grainy, film-like footage. A sterile digital reference (after a skin enhancer or sharpener) is out of distribution and turns to plastic in motion. Cleanliness is the cause, not the cure.

Order of work:

1. Degrade the references (light grain plus 5-10 percent soft blur, or a film image-to-image pass with Template A).
2. Reference hierarchy: the identity slot is a soft, well-lit frontal frame (the face anchor). A sharp detailed frame (pores, fabric) goes in a separate slot. At most 5 images per generation, because more slots average into mush.
3. Add a skin block to every video prompt with people in frame: `realistic skin with visible pores and subtle oil, natural micro-imperfections, film grain, ARRI Alexa 35mm aesthetic, soft subsurface scattering. No 3D, no cartoon, no VFX.`
4. Half of the "cartoon" look is upsampling a soft low-resolution clip. Do the draft at 480p, and for the final pass use a video upscaler (`bytedance_video_upscale`, `topaz_video`, or a local upscaler) after checking `models_explore` and the cost estimate.
5. Post: after upscaling, add grain and halation (an editor's grain overlay), then the final grade. Upscalers eat film texture, so grain goes after, not before.
6. Skin enhancers only for final stills and posters, never before video generation.

Prompt pitfalls: a word for "silhouette of a person" in some languages makes the model draw black shadows instead of people, so write "real, volumetric human bodies, not silhouettes". Fix the crowd size with a count ("exactly N people in the scene, no one else standing"). Switch screens off explicitly ("the screen is off, no picture") or the model draws faces on them. Keep @Image1, @Video1 and time codes `[0s-2s]` as written. Prompt length: stay well under the model limit, because the real limit is attention. Long prompts drop instructions.

Post color and grain: a green tint (for thrillers; a warm grade for other genres) is a color fill on its own clip above the picture in blend mode "overlay" at 20-25 percent opacity (about 15 percent for a dark image). Grain is a separate film-grain clip above everything in overlay with opacity tuned by eye. A clean generation looks plastic. Grain brings back the film feel.

## Style block to paste into prompts

Choose one stock, fill the brackets, and paste the block at the end of an image or video prompt. Keep the block free of contradictions (no "sharp 4k" with "soft").

```
STYLE (applies to every frame)
Film look: [one stock from the table above, with its key tokens].
Light: [source, direction, temperature, what is in shadow]. One light for the whole video.
Lens and camera: [focal length] lens, [aperture], shot on [camera or "35mm film"].
Film texture: gentle halation and bloom on highlights, lifted milky blacks, organic film grain
denser in shadows, soft highlight roll-off, slight chromatic aberration at frame edges,
subtle vignette, slight optical softness, no digital sharpening, not AI-clean.
People: realistic skin with visible pores and subtle oil, natural micro-imperfections.
No 3D, no cartoon, no VFX.
Mood: [two or three words].
Priority: if style conflicts with realism, realism wins. If lighting conflicts with identity, identity wins.
```

Filled example (a quiet drama, daylight):

```
STYLE (applies to every frame)
Film look: Kodak Portra 400 color science, warm creamy skin tones, slight highlight overexposure, very fine organic grain.
Light: soft grey window light from the left, low warm lamp fill from behind, face is the brightest area. One light for the whole video.
Lens and camera: 50mm lens, f/2.8, shot on 35mm film.
Film texture: gentle halation on highlights, lifted milky blacks, organic grain denser in shadows, soft highlight roll-off, slight optical softness, no digital sharpening.
People: realistic skin with visible pores and subtle oil, natural micro-imperfections. No 3D, no cartoon, no VFX.
Mood: quiet, intimate, nostalgic.
Priority: if style conflicts with realism, realism wins. If lighting conflicts with identity, identity wins.
```

A second quick example, a neon street at night: swap the stock for `CineStill 800T, signature red halation around neon lights, moody nighttime tones`, the light for `magenta and cyan neon signs from camera right, wet pavement reflections, faces lit from the side`, the lens for `35mm, f/2`, and the mood for `restless, electric, lonely`.
