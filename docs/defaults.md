# Defaults: how conflicts in the method are resolved

The method comes from many sources written at different times, and some of them disagree. This file records how each disagreement is settled, so stage documents and the agent do not reopen it. Stage documents cite the ids below (A1, B3, C2).

Three kinds of entries:
- A. Settled rules. A conflict that a newer version, a model difference or a different case resolves. No user decision needed.
- B. Default choices. Taste or business choices. The agent uses the default and the user may change it.
- C. Open questions to test. Sources disagree and only a short test settles it. Until the test is done, use the stated fallback.

Every paid test follows the money rule: show the exact list (model, number of jobs, credits from the `estimate_*_cost` tools) and wait for the user's "yes". Check `models_explore` for current models first. Never state fixed prices.

## Settled rules

**A1. Hook timing.** The idea must be clear from the first frame without sound, and the details open by 3 seconds. Take the strictest and latest norm among 0.5 to 4 seconds. Why: the numbers are different scales, not a dispute of facts, and the strictest is the safest.

**A2. Own idea or adapted idea.** Take a proven mechanic, write your own content and angle. Why: both claims are compatible, and the newer one says the idea must be yours.

**A3. Product or relationship in the hook.** Choose the format before the ideas. A short 15 to 30 second hit puts the brand in the punchline. A story piece of 40 to 120 seconds hooks on a relationship and the product is not the center. Why: two different formats.

**A5. Draft or final at once.** Static and simple scenes: a cheap test of 4 to 5 seconds or a low-resolution draft first, then finish that same take. Dynamic scenes (chase, fight, crowd): generate at the target resolution at once. The estimate includes both cases. Why: motion physics differs between resolutions. A draft is honest only if you finish that very take rather than generate it again at high resolution. Test: C6.

**A6. Mood board: pictures or text.** Two layers. Pictures live in `refs/` for the human. A text of 3 to 5 phrases in `moodboard.md` goes into prompts. Why: they are two layers of one process.

**A7. Storyboard frames and setting frame as video-model input.** For `seedance_2_5` and `kling4_0` with reference cards, storyboard frames are not fed into the video model. Feed reference cards, locations, objects and a setting frame (put the setting frame together with the cards). Exception: ad-type models such as `minimax_h3`, where the approved 3 by 3 grid goes as a reference and `start_image` can be a storyboard frame. A first frame in image-to-video is a separate allowed technique. Why: the newest agent rule is general; the ad method is about one model, so the rule is tied to the model.

**A8. Mood board and references in storyboard frames.** With 30 to 40 frames, each frame gets only the setting frame and the reference card. Add location photos and model photos only when the location is really in the frame and there are few frames. Why: different scale, both right for their frame counts.

**A9. Timecodes: whole or fractional seconds.** `seedance_2_5` uses whole seconds only; the shortest block is 1 second. Kling and MiniMax allow fractions. Write the storyboard in the units of the chosen model. Why: a property of the model.

**A10. Slow motion, distortion, vignette, zoom in prompts.** For `seedance_2_5` there is no default ban. Add slow motion to the negative only if the slowdown is not wanted. For photoreal prompts on other video models the ban holds unless the video explicitly needs it. Do the slowdown at the peak in the edit (speed ramp), not in generation. The taste set per video is B17. Why: rules are tied to model and genre.

**A11. Emotion in the frame.** Before frames, write one emotion per frame beside the storyboard. Emotions differ (an arc). The method idea "build up to emotion" belongs to the story and fits the arc; see B19 for the peak. Why: frame level and story level are different levels.

**A12. Camera shake.** Decide by genre before the previz. Documentary: shake stays and is written into the prompt. Cinematic: the previz is smooth and no shake is added. Seedance repeats any wobble of the previz. Why: different tasks, genre is chosen earlier (B3).

**A13. Prompt length.** There is no single number; length depends on the model. Photo models with long descriptions: from about 2000 characters for realistic scenes. A short style-keyword image model: 20 to 60 words. Kling about 400 characters. Seedance ceiling 4000 to 5000. Storyboard does not set prompt length. Read the length limit from the chosen model's guide. Why: a technical limit and a sweet spot depend on model and task. This is our summary, not a quote of a lesson.

**A14. Script structure.** Choose by video format (three acts, five blocks, eight cartoon beats, hook-reveal-scenes-finale), not by taste. Why: structures belong to formats.

**A15. How a video begins.** The first second shows an outcome shot from this story, prepared inside the video (B18 sets how much to reveal). After the hook, shot order goes from wide to close, or deliberately the opposite. Why: opening and order after the opening are different levels.

**A16. Quality-boost words.** For photo models do not write `4k, masterpiece, ultra-detailed, ultra realistic`; resolution is a parameter. For Kling and Seedance replace epithets with a visual fact. Do not copy a `cinematic lighting, 4K` line from camera-move tables into finished prompts. Why: most sources agree and the model logic is the same.

**A17. Film stock.** One stock per prompt; do not mix. Why: checked on Seedance; the lists only describe options.

**A18. Block order in a prompt.** Photo: by the lesson formula, subject first. Video: angle and camera open each beat. Kling: the file roles come first. Omni-type prompts: the camera opens the whole prompt. MiniMax: camera at the end after the beats. In one prompt, follow the guide of the chosen model. Why: differs by kind of generation and model.

**A20. Text or picture for the face.** Text holds clothing, light and setting. The picture holds the face. A face identity comes only from a reference card, never from a text description. Why: the newer consistency method reconciles both.

**A21. Reference card format.** For cartoon characters a turnaround sheet (front, side, back, close). For realism separate high-resolution faces and a figure without the head. Use an image model for look, figure and environment; build the face from real photos or from a model that locks identity. Why: look and face are different tasks, and the newer method says so.

**A22. How many face angles.** Default 3. If the face drifts, add up to 5. The photo bases of source material (5 photos of a double) belong to another stage. Why: numbers belong to different stages.

**A23. Face size on a reference.** The face fills at least 30 to 50 percent of the frame and no less than 1024 by 1024. For a realistic card the face fills the whole picture at 4K. Why: one meaning (larger is better), different numbers for different cards.

**A24. Fix a frame or regenerate.** Broad changes early: edit the original prompt and regenerate. One detail on an almost finished frame: fix by dialogue edit. After 4 to 5 edits start again with a reference. A reference card is only regenerated from the source images. Why: newer methods agree; this is our reading, not a lesson's wording.

**A25. How many references.** Optimum is up to 6 per generation. Ceilings are technical: `nano_banana_pro` up to 14 (5 of them human), other models by their guide, Seedance 2.5 up to its documented limit (practice about 25). From 5 images up, faces hold better when roles are stated in a block. A case with 5 photos of a model plus outfit plus accessories is an exception. Why: "up to N" is a technical limit, the optimum is lower.

**A27. Negative prompts.** By model. `seedance_2_5`: a short negative of concrete problems (`Avoid jitter, bent limbs, face drift`); a problem closed by text is also duplicated as a ban. `kling4_0`: no separate negative; only `no subtitles` and `no background music` are mandatory. MiniMax: describe positively; for clean styles a list of bans (`no grain, no vignette, no lens flare`). `nano_banana_pro`: positive only; negatives are not supported. `gpt_image_2_6`: a "without" block works. Write only what relates to the scene, no generic filler. Why: newer model guides override older lessons.

**A28. Reference card background.** A plain single-color background, default `#cccccc`. Why: the value is a choice; being plain matters.

**A29. Prompt language and speech language.** Prompt language follows the model guide. Speech on screen in a language outside a model's published list may still work in `seedance_2_5` (lines stay in the speech language inside a prompt in the model's main language), but test it (C3). `kling4_0` has no official Russian; lay a recorded voice over. Why: prompt language and spoken language are different things.

**A30. Output format of a prompt.** By model: some image models take plain text with a counter, some take JSON, `nano_banana_pro` takes full sentences. Why: a property of the model.

**A31. Aggregator sites and connection.** Do not open aggregator sites or node tools; run everything through the agent and Higgsfield MCP. Connect Higgsfield one way, the one that already works. Why: newer lessons say so and several interfaces lead to one address.

**A32. Clip length of a reference, number of clips, character limits.** No single number. Read the documentation of the chosen host before building and write it into `experience.md`. For character limits use the guide of the specific model; old lessons are outdated for new versions. Why: hosts and versions give different numbers.

**A33. Music, voice and sound in generation.** Do not put music into generation when the video is assembled in post. Music inside a prompt is allowed only for a finished ad made by one generation. Voice: no voice in a previz generation is the safe default; a model voice is allowed as a timing guide and then replaced with your own (newer lesson). Whether lip sync holds with a video reference plus an audio reference is C3. MiniMax H3 sound is C5. Why: different scenarios; the newer lesson wins.

**A34. Camera: per clip or per shot.** Seedance has one main move per clip plus a camera in each time segment per the master prompt. Kling opens every beat with the camera. Do not write a priority-of-angle rule in the prompt. Why: different levels, no direct contradiction, and the newer guide drops that rule.

**A35. Sound inside a shot or one line.** Write sound in every shot (a single closing line is ignored). For `seedance_2_5` videos over 15 seconds, sound by timecode. For Kling, `AUDIO` in every beat. Why: guide and lesson agree.

**A36. Editing a video prompt.** By model. Omni-type: change one variable at a time but resend the full prompt. `seedance_2_5`: resend the whole prompt. Kling: edit a finished video with an edit command on `@Video1`. Why: a model difference.

**A37. Choosing a model for a task.** If a face is in the frame, use a ready reference frame, not text. Choose the model by task and by the newer version; check `models_explore`. Speech and lip sync: test per language (A29). Older model lists are outdated. Why: the questions answered by different lessons were different (language and price versus task).

**A38. Voice model rules.** Work by the newest ElevenLabs rules (v4, via `elevenlabs_v4`). Stability is continuous, default about 0.5. `style` and `speed` are ignored and SSML does not work. Capitals on 1 to 2 words only. IPA between slashes for exact sounds. Spell abbreviations as they sound. Pauses: `[short pause]`, `[pause]`, `[long pause]` (about 1.2 s), `...` for weight, `-` for an interruption. Use the v3 rules only if working on v3. Why: v4 is newer; older notes belong to v3.

**A39. Tags and text bounds in speech models.** Script-style words are read aloud; square-bracket tags are not spoken (two kinds of tags). The text bounds for v3 are more than 250 and up to 5000 characters. Why: different tag kinds, and lower and upper bounds, not a conflict.

**A40. Length of a recording for a voice clone.** By service: instant voice clone minimum about 10 seconds and ideal about 5 minutes; another service needs 1 to 2 minutes of clean speech without noise. Read the requirement of the Higgsfield voice tool. Why: different services.

**A41. Loudness.** Final mix -14 LUFS, voice louder than music. Editor slider values for music and effects are other scales and are not converted to LUFS. Why: different scales.

**A43. Avatar prompt and multishot prompt.** Avatar from photo and audio: 1 to 3 sentences and 3 to 5 directives, no appearance description. Multishot generation: a long prompt of 5000 to 8000 characters is allowed. Why: different inputs, no contradiction.

**A44. How often to change the shot.** Leader measurement: a new place every 3 to 5 seconds, shots of 1.5 to 2.5 seconds. Lessons say every 2 to 3 seconds, or 1.5 seconds in a 19-second video. They do not contradict, and our rule does not cancel the lessons. Why: different platforms and genres.

**A45. Where upscale stands.** For Seedance, do not upscale references and slightly "dirty" them (grain, 5 to 10 percent blur). Detail and skin enhancers only after the video. For Kling motion transfer, upscale the source photo of the double before animating. Upscale finished clips one by one before the edit, before grain and grade; do not upscale the assembled video a second time. The order is checked in C7. Why: different video models; two lessons favor clip upscale before the edit and the newer skill does not directly disagree.

**A46. Number of storyboard frames for motion.** 6 key frames for code-based motion, a 3 by 3 grid (9) for generation, 6 to 9 panels through a motion agent. Why: a difference of technique.

**A47. Voice cleaning service signature.** Check both ends of the audio: the first 20 seconds (a jingle at the start) and the last phrase (a spoken signature at the end). Why: sources differ and the check is cheap.

**A48. Copies and reuploads.** Conservative rule: no more than 10 similar videos per account in 30 days, each copy has its own sound and a new hook. Do not present claims of "reach cut by 90 percent", "10 to 60 thousand views per copy" or a 70 percent match threshold as official. Why: the cautious source cites a platform publication; the others are a host's words. Own measurement: C8.

**A49. Render CRF.** For social delivery CRF 22 (21 only inside the copies tool). Why: one goal, compatible numbers.

**A52. Folder structure and rules file.** Base structure: `gen_image`, `gen_video`, `out`, plus `previz` and `drafts`; add `voice` when voice-over is made. Details in `templates/project-folder.md`. One studio rules file; sections for edit and brands are appended, nothing is overwritten. Why: no single scheme in sources; this fits the "append, don't erase" rule.

**A53. Number of stages.** Not a conflict. Three pillars, five project stages and four or five pre-production steps are levels of detail.

**A55. Where to look for clients, platform fees, size of a portfolio.** Plan more than 20 platforms rather than 12. Assume the worst fee on freelance marketplaces, 10 to 20 percent. A messenger channel is for the portfolio and free chats, not for cold outreach; the first contact is better on a social network. Portfolio: at least 3 cases, goal 5 to 8. Why: newer sources, or a difference of role.

**A56. How many outreach attempts.** Plan 20 cold messages a day and 100 a week, hundreds of attempts in total. Do not plan "10 messages means 1 to 2 clients". Why: the newer source is stricter.

Also settled while checking the laws:
- "One strange thing" versus "absurd without effects": the second wins. The strange thing must be shootable with real people and props.
- "Count generations and price at the idea stage" versus "do not talk credits before the story is approved": count for yourself, name the number to the user only before a paid step.
- "Titles are mandatory": speech subtitles and decorative titles are different things. Speech subtitles stay mandatory; decorative titles are B2.

## Default choices (the user may change them)

**B1. Series or standalone ideas.** One main hero and one style across the channel, each video a complete story. Alongside the videos, "how it was made" posts. Changes what the project keeps: a series engine, constant reference cards, a recurring look. (Default; the user may change it.)

**B2. Title card in the first second.** A short one-line rubric label for 0.5 to 1 second in one consistent style, used as a channel sign. No other decorative fonts. Speech subtitles are separate and required. Pick fonts that look designed, not defaults. (Default; the user may change it.)

**B3. Which realism.** The look is chosen per genre and written into the style sheet (`moodboard.md`) before the first generation: for example film grain for thriller and heist, an amateur phone look for domestic comedy. One look inside one video. (Default; the user may change it.)

**B4. Prepayment, 100 percent or 50 percent.** Deferred until the first client appears. Go through B4, B11, B12, B13 and B14 again before the first client conversation. Until then the studio makes no price promises.

**B5. People in the previz.** Simple dummies without hands; hands only where a gesture matters. Positions and paths come from the dummy, acting comes from the prompt. (Default; the user may change it.)

**B6. Previz render.** A fast gray render without shadows. Turn shadows on only if a test shows the model confuses depth. (Default; the user may change it.)

**B7. Order: images before previz or previz first.** Reference pictures (faces, locations, objects, setting frames), then a dummy previz built for them, then video. Stage order stays 03, 04, 05, 06. A weak idea is still killed earlier, in pre-production: script and a 3 by 3 storyboard with "ok" before any generation. (Default; the user may change it.)

**B8. Skin retouching.** No retouching. Skin stays alive on reference cards and in scenes (`no beautification`). Retouch a client's double only when the client asks. (Default; the user may change it.)

**B9. Length and frequency.** 30 to 60 seconds per video; a steady publishing rhythm that the user sets (three videos a week with a "how it was made" post between them is a good start). Not chasing very long videos for platform payouts. (Default; the user may change it.)

**B10. Synthetic voice or live voices.** Synthetic voice by default (`elevenlabs_v4`), one voice per character for all roles in the series, saved once and reused. Live actors only when a client asks. (Default; the user may change it.)

**B11. Price list.** Do not publish one price list until the first three real projects show the real cost. Sources differ by an order of magnitude because markets and products differ. Deferred with B4.

**B12. Surcharge for transferring rights.** Recommended: plus 30 to 50 percent. Deferred with B4; confirm with a lawyer for the user's country.

**B13. Free first projects.** Recommended: up to three projects free or symbolic for reviews, with a fixed generation budget cap set in advance. Deferred with B4.

**B14. Contract and legal.** Use a template only after a legal check in the user's country. Deferred with B4.

**B16. Platform signature in published text.** No signature of a course or club in posts. Mention tools only if there is a partnership or the post is a "how it was made" breakdown. (Default; the user may change it.)

**B17. Optics and slowdown.** By default a clean camera. Special tricks (slow motion up to 3 seconds, wide angle 14 to 24 mm, a snap zoom, one dolly zoom per video) only on gags and peaks, and each is marked in the storyboard. (Default; the user may change it.)

**B18. First frame: show the outcome or not.** Do not reveal everything in the first seconds. The hero struggles and the turn comes at the end. The first frame may show an outcome only as a riddle, never as the resolution. (Default; the user may change it.)

**B19. Emotion: strongest at the start or built up.** Build up to the peak: wide, medium, close, extreme close at the peak, a quieter start. Emotions differ from shot to shot and are readable. (Default; the user may change it.)

## Open questions to test

**C1. Real faces in Seedance on Higgsfield.** Sources disagree: one lesson loads a reference card made from real photos, another says the model rejects references with real human faces. Test: one `seedance_2_5` generation, 3 to 5 seconds, with a reference card from a real photo of the user themselves (never a client or an artist), plus a variant "full-length photo". Cheapest: minimum length, 480p, price known beforehand from `estimate_video_cost`. Until the result: do not put real faces into Seedance references; use a stylized face or a different model.

**C2. Previz format and minimum frame area.** Sources: 4:3 at 640 by 480, a vertical 480 by 854, a host that wants a minimum side length and a minimum area. Test: upload the same previz to the chosen host at 640 by 480, 480 by 854 and 960 by 720. Cheapest: run the host's input validation before rendering; if it rejects the file the cost is zero.

**C3. Lip sync with a video reference and an audio reference; non-English speech.** Not shown whether lips stay in sync when both a video reference and an audio reference are given; a non-English language may be outside the published list. Test: a 5-second clip with one line in the target language: (a) the model's own voice, (b) your recorded voice as `audio_references`. Cheapest: one dialogue shot of minimum length at 480p, price from `estimate_video_cost`. Fallback: put the voice in post (path A).

**C4. Previz in Kling or only in Seedance.** One lesson says the Blender link works only with Seedance; a newer guide says white models and a depth map are supported in Kling, and one test kept both cars. Test: one previz (5 to 8 seconds, two objects) in `seedance_2_5` and in `kling4_0`; compare whether objects stay. Cheapest: a short previz, 2 generations, price from `estimate_video_cost`.

**C5. Sound of MiniMax H3.** One guide says it is fully silent; one lesson says it returns a video with its own sound. Test: one `minimax_h3` generation of 5 seconds; look for an audio track. Cheapest: the shortest length. In any outcome, put sound in the edit.

**C6. Does a 480p draft predict the final.** Motion physics may differ between 480p and 1080p. Test: one dynamic scene (chase or crowd) at 480p and at high resolution; compare motion. Cheapest: 5 seconds at two resolutions, price from `estimate_video_cost`. The result decides which scenes are generated at final quality at once (A5).

**C7. Order of upscale.** Check that upscaling every accepted clip before the edit beats upscaling the assembled video, and that detail enhancers after the video do not damage it. Test: one clip in both orders; compare. Cheapest: one 5-second clip, one pair of runs. The price depends on the tool and is not known until estimated.

**C8. Copies on a trial account.** Check the claims (10 to 20 copies, 10 to 60 thousand views each, a 90 percent reach cut on reupload) against the cautious rule (10 similar videos per 30 days). Test: on a test account post 3 copies with different sound and hook and watch reach. It costs time and some risk to the test account, not money.

**C9. Compound camera moves and Dutch angle.** Sources conflict: "one shot, one move" versus `push in with tilt up`, `vertigo`, `orbital`; and tilt of 30 degrees versus 5 to 12 or 8 to 10 degrees. Kling may lose moves after the third (not verified). Test: one shot with a compound move (3 moves in a row) and three tilt angles (5, 10 and 30 degrees). Cheapest: 5-second shots at 480p. Until tested use 5 to 12 degrees, on which two guides agree.
