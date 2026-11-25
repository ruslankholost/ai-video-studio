---
name: ai-director
description: Director's method for a cinematic AI video, from concept to finish. Use it when the user wants a "full Hollywood" piece, a spec ad, or asks the agent to think like a director: concept test, look bible, master prompt, references before motion, Blender greybox as camera reference, Seedance prompt, review and hand finish. Works on top of the stages in docs/stages; the stage documents and the user's decisions win.
---

# AI director: one method

A compact director's method collected from public breakdowns of creators who make viral AI films and ads (2025-2026). It does not replace the stages: open the stage document first, then use the matching part here. The user's decisions and `docs/lessons-learned.md` win over this file. Nothing paid is generated without the user's "yes" on that exact run.

## 0. Concept (text only, before anything else)
- **The test:** it must be something that could never have been shot practically. If a crew could shoot it, it will not stand out.
- Formulas that keep repeating among creators who went viral:
  1. A known thing in a world it was never in (a familiar genre, hero or situation moved into a new world).
  2. A spec ad for a brand everyone knows, with an unexpected twist. Label it spec or fan-made, never pass it off as official.
  3. An extreme visual analogy: a disaster chases the hero and the product saves them with its main property blown up to the scale of the disaster.
  4. A recurring original world or characters (slower, bigger: series).
- Comedy and absurdity beat beauty for reach. The first shot must be the viral one (first 1-4 s). 20-45 s, every shot a new image or beat, no dead seconds.
- People in the story behave like real people in that situation; the tension comes from their real stakes (late for work, the car is trapped). No actions invented only to keep the hero busy.
- Give two versions per idea (clear and unexpected). The user picks.

## 1. Look bible (one page per project, before any image)
Aspect ratio; one or two focal lengths for the whole piece; key light direction and one dominant colour temperature plus one controlled accent ("hard cold key with a single warm accent", "one warm light in the dark"); palette in three words (1-3 main colours, `docs/stages/02-film-language.md` 02.72); film stock or grain line; negative list; reference image file names. Every later prompt repeats it. "Cinematic lighting" alone is banned: name the source, direction, quality, the shooting side and what it does to the face (02.70).

## 2. Master prompt
Build ONE hero frame until light, lens, shadow, blur and framing are right, then freeze that wording as the master and only swap the subject, action and camera line for variants. Clause order most official guides agree on: format, subject, action, setting, camera and lens, light, style and texture, constraints. Edits as Lock (what must not change) / Change (one thing) / Amount. Check: camera, tone, lighting, texture. For image edit models pin with "keep the exact camera angle, the exact silhouette".

## 3. References before motion
Character sheet (front, back, face close-up), prop sheet, environment still with the character in it, then a texture pass, then a separate lighting pass, all as stills (stages 03 and 04). Coverage (close-up, two-shot, wide) is generated from the master frame keeping light and palette. References hold identity better than prose; one reference per element.

## 4. Blender greybox = camera and timing reference, when needed
Only for a long take without cuts, or a camera move the prompt failed to hold twice (stage 05); then use the `blender-previz` skill. Short shots with simple moves are held by the start frame, the cards and the prompt.
- Render each shot as its own continuous clip, 3-8 s, at most 720p H.264, no cuts inside a reference. Check the current host limits on Higgsfield before uploading.
- Keep a library of named camera moves (push-in, orbit, whip-around, overtake); write each as `<move>. Movement / Speed / Framing / End` (02.66) and paste it into the camera block of the video prompt.
- One continuous greybox camera move can carry several worlds: a 30 s one-take that trucks through connected rooms, each a different world, with one consistent character. The split-screen breakdown (reference board, generation, greybox) is a post of its own.
- A phone camera-tracking app can record a handheld take straight into Blender; this gives the camera a human feel the keyframes do not.

## 5. Generation prompt (Seedance 2.5)
Use `templates/video-prompt-seedance.md`. Ten blocks in one prompt: global style (one visual rule at the top), logline, characters, location, first frame and blocking, shot by shot with cut type and duration, optics and camera per shot, physics, lighting (source, motivation, direction, fall on faces), audio (one sound rule at the bottom). Split roles explicitly: the image gives the look; the Blender video gives "camera movement and timing only, do not reproduce the grey materials or simplified geometry". At most 5 shots or 15 s per generation; drafts at 480p; regenerate only the failed shot. Realism comes from camera accidents: handheld micro-jitter, focus hunting, exposure shift, something crossing the frame.
- Photoreal close-ups of people used as references can trip the "real person" moderation; pass character cards plus the previz.
- Untested: lip sync to a pre-voiced track while also using a video reference. Test once before relying on it.

## 6. Review
Start, middle and end of each take against its Blender reference: camera direction, subject placement, foreground order, face and scale drift. Check every out-point frame by frame: the model often snaps back to its start frame after the action. Then watch the cut for emotion, voices and readability, and run the finished-video defect list (stage 08). Keep accepted takes with their references.

## 7. Hand finish
The human layer is what the best names sell: painting over frames, print texture, editing from many takes. Grain after upscale, grade, sound design, the user's own lettering or drawn overlays where the look allows it.

## 8. Distribution
Post the piece, then a breakdown of how it was made; breakdowns often outperform the piece itself. Time pieces to a new model launch or a big cultural moment. Famous faces and other people's IP raise reach and carry legal risk.
