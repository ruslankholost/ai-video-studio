# 07 Sound and voice

This stage answers three questions: where the hero's voice comes from, how it stays the same across a whole series, and how sound is built in the finished video (voice, effects, music, loudness). Sound carries a large share of how a short video feels, and a wrong voice is the fastest way to make a character look fake. Decide voice early, in the storyboard, not after the clips exist.

Principle numbers are kept stable because other files cite them. A few numbers are unused on purpose (07.83, 07.87).

## Input and output

Input (must exist in the project before this stage):
- `script.md`: lines per character, language of the voice, who speaks.
- `storyboard.md`: what is on screen each second and what the sound is (see 07.11).
- `frames/` and `refs/`: a portrait of the hero, needed if the voice is driven by "audio + photo" (07.38).
- `prompts.md` and `video/`: prompts and generated clips. The clips already carry the model's own sound.

Output:
- `audio/`: voice files per character, a note of which voice each character uses (voice name or id), generated effects, chosen music.
- `video/` with the voice replaced, if path A or B below was chosen.
- Sound layers ready for `edit/`: voice, foley, effects, ambience, music, boosters.

## Principles

### A. Where the voice comes from and which scheme to pick

07.1 A voice can come straight from the video prompt: one or two frames plus text give a video with face motion, body motion and a voice. The model invents the voice, but emotion, behavior and camera stay controlled by the prompt.

07.2 In this scheme the voice cannot be fixed. It is slightly different every generation.

07.3 A random voice is fine for a one-off video. For a channel, brand or series, every character needs one voice. Two videos of one character that sound like two different people break recognition.

07.4 For one voice across a series there are two paths. Path A: replace the voice after generation. Path B: provide a finished voice as input.

07.5 Choose path A when the video is already made and a re-shoot is not wanted. It is fast.

07.6 Choose path B for long continuous videos and for lip sync to a song. The audio is set first and lasts as long as needed.

07.7 Create the character's voice once, then reuse it in every video of the series. This is what makes the hero recognizable by ear.

07.8 Sources of a voice, when the user has no recording: a ready voice from the Higgsfield voice list (`list_voices`), a voice designed from a text description (`create_voice`), a clone from a reference recording, the user's own recorded lines, or live actors. Default: a designed or listed voice (default; the user may change it). Live actors only if a client asks.

07.9 A rough synthetic voice track is fine for rhythm and a complete feel of the draft. The final can be replaced with human voices. This was one real case, not a rule.

07.10 Pick the model by task and language, and test several. If a model does not speak the needed language, generate the clip in a supported language, then translate the line and lay a new voice over it (path A).

07.11 Plan sound in the storyboard before generation: for each second, who speaks, what, in which language, which sounds are needed.

### B. Voice inside the video prompt

07.12 A prompt with sound has two blocks: what the character does, and what the character says.

07.13 Always name the language of the speech. Write the line word for word, in quotes. Lip sync lands more accurately.

07.14 The text must fit the clip time. Check with a stopwatch: say the line aloud at the intended pace and time it. More text in the same time makes the character speak faster, stumble and swallow words.

07.15 Emotion of the voice is set by words in the prompt. One added word changes the delivery (for example: whispering, slowly, with a smile, confidently looking at the camera).

07.16 A model may not support the delivery you need (some cannot whisper, some soften aggression). Try the same line on another model.

07.17 Sound is written as its own block after camera and subject: the line word for word in quotes with the language, plus background sound. Example: `Sound: quiet room, rustling petals. A woman says irritably in English: "Did you jump on the table again?!"`

07.18 Describe sound inside every shot, not in one line at the end of the prompt. A single closing line is ignored by Seedance.

07.19 A shot in the prompt holds four elements: action, camera, physics, audio.

07.20 Tie lines and sounds to seconds (for example `0-2s: ... SFX: door click`).

07.21 Forbid everything not requested: subtitles, titles, on-screen text, music. Some models draw broken subtitles or add background music on their own. Add a negative or constraint such as `no titles, no subtitles, no text, no music`. Kling 4.0 uses `no subtitles` and `no background music` as positive constraints (A27).

07.22 No long dashes in spoken lines. Models try to pronounce them.

07.23 If a prompt-enhancing option is on, check that it did not translate the spoken line into English.

07.24 If the model stumbles on a word, reorder the words or use a synonym.

07.25 If a model makes the character talk by default and no speech is wanted, give a facial expression (mouth closed, light smile), switch audio off, and add your own sound in post.

07.26 Finished audio can be fed to a video model as a reference. In `seedance_2_5` use `audio_references`. Useful phrasing: `reference @Video1's audio`; `voice and lip sync reference @Audio1 exactly`; `video rhythm references @Audio1's beats`. Whether lip sync holds when a video reference (previz) is also given is not shown by the method. It is open question C3: test it before relying on it.

07.27 When a 3D previz is loaded as a video reference, the safest default is to leave the voice out of that generation and put it in post. A newer case used model voice as a timing guide and replaced it later (A33). Voice in the same generation with previz stays untested (C3).

### C. Fixing the voice: replace, clone, ready-made

07.28 Path A step by step: generate the video, extract the audio track, run it through a voice-change tool with the chosen or cloned voice, put the audio back. On Higgsfield: `voice_change`, with `separate_stems` first if the track mixes voice and noise.

07.29 For a clone, use any recording of the voice: longer and cleaner is better. A minimum of about 10 seconds and an ideal of about 5 minutes is the usual guide for instant clones. Some services need 1 to 2 minutes of clean speech instead (A40). Check the requirement of the Higgsfield `create_voice` tool before recording.

07.30 If the recording has noise, music or echo, switch noise removal on. On a clean recording, leave it off: it makes the voice worse.

07.31 A voice designed from text follows a structure: language and region in the first sentence, then gender, age, audio quality, persona, emotion, timbre, pace, delivery. Without language and region the voice drifts. Full structure and word list: `templates/voice-and-music.md`.

07.32 The preview text of a designed voice must match the emotion of the voice. A mismatch gives a bad voice. A longer preview, at least a paragraph, works better.

07.33 In a multi-voice scene, keep the same voice descriptor for each hero every time.

07.34 When the voice model version changes, test the saved clone and retrain it if it sounds different. For production prefer a saved or library voice over a freshly designed one.

07.35 To lay your own voice over a generated clip: split sound into voices and noises, remove the voices, record your lines, keep street or room noises. Record close to the microphone.

07.36 Clean a recorded voice of echo and noise and level the loudness. If a cleaning service adds a jingle or a spoken signature, cut it and check the voice did not shift in time (A47).

07.37 In a talking-head video, the sound always comes from the original recording.

### D. Syncing video to ready audio (lip sync)

07.38 The "audio + photo" method has three inputs: an image, an audio file, a prompt. There are no more settings, whichever model runs it. On Higgsfield, try `seedance_2_5` with `start_image` and `audio_references`, or `kling4_0`, and check `models_explore` for any avatar-type model that is current.

07.39 The photo decides most of the result. See the photo checklist below.

07.40 The prompt is optional. It controls behavior, emotion and movement, not looks. Do not describe the appearance; it comes from the photo.

07.41 Guide, do not overload: 1 to 3 sentences, 3 to 5 directives, then iterate. Long prompts confuse the model and make the animation worse (A43).

07.42 Audio for an avatar must be clean, free of background noise, calm in pace. Fast speech smears the lips.

07.43 Audio length equals video length. For models with short clips, cut long voice-over into pieces.

07.44 Test on 10-second clips before long generations. Use the better quality tier of a model for avatars; do not save on it.

07.45 This method fits when a finished audio file exists (a song, a voice message, a recorded speech) and exact lip sync is needed, and for talking content.

07.46 Long content and translation into another language need a tool that clones the voice and re-syncs the lips. The source audio must have no background music, because music lowers lip sync accuracy. If the stack has no such tool, translate the lines and use path A or B.

07.47 Know the limits of avatars: extreme angles (head turn over about 45 degrees) distort the face; hands near the face, glasses and microphones create artifacts; a small clothing pattern flickers; a language outside the model's official list may drift in lip sync.

### E. Emotion in tagged speech (ElevenLabs v4 on Higgsfield)

Rules follow the newest ElevenLabs version, v4 (A38). Use `elevenlabs_v4` for dialogue. If a setting below is not exposed by the Higgsfield tool, skip it and steer with text.

07.48 Put the emotion tag directly before the phrase it affects.

07.49 Tag only changes of delivery, not every phrase. One emotion per phrase. A tag lasts until the next tag, and contradicting tags blur the performance.

07.50 Write tags in English in square brackets. Write the spoken text in the voice language. Before non-English text keep tags short; put a long direction once at the start of the scene. Long English directions before every line sometimes cause repeated words.

07.51 A tag describes a voice, not an event. `[low, gravelly voice]` is good. An ambiguous tag may be played as a sound effect.

07.52 Voice the whole scene at once, not line by line. The model performs better with full context. For long texts see 07.56.

07.53 Before working, check that the chosen model understands tags. A model without tag support reads them aloud. Always name the exact model.

07.54 Script-style notes ("she said, her voice trembling") are spoken as words. Remove them from the text.

07.55 If the voice sounds monotone, split the text into short lines, generate in portions, and put pauses on punctuation.

07.56 Voice long text in pieces and keep the intonation at the joins (for example by passing the previous request context if the tool allows it). Without it the voice drifts between pieces.

07.57 Liveliness against stability: a lower stability value is livelier and more emotional, a higher one is steadier up to monotone. In v4 stability is a continuous value, default about 0.5. `style` and `speed` settings and SSML do not work in v4 (A38).

07.58 Write numbers, dates, currencies, abbreviations and brands the way they should sound.

07.59 Stress by capital letters on one or two words only. Capitals on a whole phrase sound like shouting. Pauses: `[short pause]`, `[pause]`, `[long pause]` (about 1.2 s), `...` for weight, `-` for an interruption. For exact pronunciation use IPA between slashes (A38).

07.60 Leave time margin and measure the real length on the finished audio. v4 reads about 10 to 20 percent slower than v3 by user tests.

07.61 Make several takes and pick the best. An artifact in a take is fixed by regenerating with a new seed.

07.62 Check the voice emotion and the face emotion together. A soft voice with an angry face reads as a mistake.

### F. Music, effects, layers, loudness

07.63 Background music is needed in the video even when there is a voice. It gives atmosphere.

07.64 Final mix loudness is -14 LUFS, voice louder than music, music lower under the voice. The editor slider values for music and effects are on other scales and are not converted to LUFS (A41).

07.65 For a "familiar" feeling, instrumental versions of popular styles work. Rights are the user's responsibility; the agent does not discuss licenses unprompted. Prefer generated music or music the user owns.

07.66 Do not ask for music in the generation when the video will be assembled in post. Music inside the clip cannot be separated from noises. Music inside the prompt is allowed only for a finished ad made by one generation (A33).

07.67 Choose music before the edit rhythm: cuts are built on it and land on beats. Tempo changes by act. Generate with `elevenlabs_music_v2_5` (instrumental, stated length, mood, tempo) and check the cost first. If there is no track, work without music but with effects.

07.68 Do not carry a client's original logos, texts or music from a reference into the client's work.

07.69 Build sound in layers, in this order: separation (what the generation gave, voice split off), dialogue, foley, effects, ambience, music, boosters by genre.

07.70 First listen to what sound the generation gave and separate the voice from the rest.

07.71 Dialogue goes first. Everything else is built around it.

07.72 Sound everything meaningful, not everything. Literal sound for every movement ("mickey-mousing") feels unnatural. Yet the denser the meaningful action is sounded, the deeper the immersion.

07.73 Sound follows the speed of the picture. If sound stays flat under a speed ramp, the trick looks like lag.

07.74 Sound and picture can be offset at a cut. J-cut: the next scene's sound starts before its picture. L-cut: the previous scene's sound continues over the new picture.

07.75 Sound hooks hold attention: whoosh on a zoom or move, clicks on a change of shot or an appearing element, hits on accents, ambience, sharp sound stops for tension. Do not forget sound design between cuts.

07.76 Name effects with standard names so they can be searched and generated: riser, impact, whoosh, braam, drone, sub drop, reverse, stinger. Place boosters on key moments.

07.77 Describe a sound for generation as concretely as possible, in English. Not "rain" but "heavy rain on a metal roof at night with distant thunder". When searching a library, search in English too and check the duration.

07.78 Keep all generated effects for fast editing. Store music and effects in `audio/music` and `audio/sfx`.

07.79 The video must read without sound: large, contrasting subtitles. Many people watch muted. Speech subtitles are required; decorative titles are a separate choice (B2).

### G. Checking and working with the agent

07.80 The agent cannot hear. Check loudness and the spectrogram with tools, and write honestly what was checked and what was not ("not checked by ear"). The human checks the voice and tone by ear.

07.81 Paid generation, including voice, runs only after the user's "ok" on the exact list (model, number of jobs, credits from `estimate_audio_cost`). Keys and tokens stay out of the chat.

07.82 In the project, the agent writes the text with emotion tags, generates the voice, saves it into `audio/`, and puts it in place of the generation's voice.

### H. Lessons from tested examples

07.84 Clip length equals speech length. Do not leave an empty tail after the last line: the character freezes without blinking or breathing.

07.85 In speech shots check three places first: the inside of the mouth and teeth, the hands, a frozen strand of hair. These are where models fail most while the face holds.

07.86 Compare voice models on one line and one frame, so the difference shows in the speech and not in the text.

## Workflow

1. In the storyboard write for each second: who speaks, what, in which language, which sounds are needed (07.11).
2. Decide: one-off video or series (07.3). One-off: voice from the prompt (07.1). Series: path A or B (07.4 to 07.6).
3. Create the hero's voice once: list pick, designed voice or clone (07.7, 07.8). Save the voice id in the project notes. Test the line on a short text first.
4. Pick the video model by language (07.10) and write the sound block of the prompt: line word for word, language, sound per shot, ban on music and subtitles (07.12 to 07.23).
5. Price message: list model, number of jobs and credits from `estimate_audio_cost` or `estimate_video_cost` with the checklist below. Wait for "yes". Name any step outside the method as a deviation.
6. Generate and review: speech, language, subtitles, music, cut-off words (07.14, 07.21 to 07.24).
7. Path A: extract the track, split stems if needed, `voice_change` to the hero voice, put it back. Path B: voice the text with tags (07.48 to 07.61), prepare the portrait by the photo checklist, give the three inputs to the video model (07.38 to 07.44).
8. Clean a self-recorded voice (07.35, 07.36).
9. Build layers in order: voice, foley, effects, ambience, music, boosters (07.69 to 07.78). Check loudness (07.64).
10. Run the checklist and show the result. The user listens to the whole video; the stage is closed only by their "ok".

## Formulas

Full voice prompts and tag lists live in `templates/voice-and-music.md`. Here only what concerns video models and the edit.

Prompt with sound, two blocks:
```
The woman turns to the camera and says in English: "Everything you look for outside is already inside you. Stop and listen to yourself."
```
With emotion: add the delivery before the quote, for example `says in English, whispering, slowly:` or `says with a smile, joyfully:`.

Sound block of a video prompt (07.17):
```
Sound: quiet room tone, soft rustle. The man says calmly in English: "..."
```

Audio inside a shot (07.18, 07.19):
```
[Shot 3, 1s, FOOD MACRO]
Action / Camera / Physics ...
Audio: ASMR cheese pull and sizzle, deep bass rumble.
```

Audio references in `seedance_2_5` (07.26): `reference @Video1's audio`, `voice and lip sync reference @Audio1 exactly`, `video rhythm references @Audio1's beats`.

Avatar prompt, four parts (07.41): role and context, expression, movement intensity, camera. Example: "A confident business trainer. Friendly, engaged face with thoughtful pauses. Light head movement, natural nods, eye contact. Slow push-in." Working directives: role (news anchor, teacher), emotion (calm, warm, excited), gestures (subtle hand emphasis, light nods), camera (medium close-up, slow push-in).

Voice scheme, short:
```
Generate video with the model's own voice
  -> separate stems -> voice_change to the hero voice   (path A)
OR voice the script with the hero voice (elevenlabs_v4)
  -> feed audio + portrait to the video model           (path B)
Then add effects and music in post, mix to -14 LUFS
```

Choosing a model, short (always confirm with `models_explore`, models change):
- Talking head with lip sync and sound in the video: test `seedance_2_5` first; compare with `kling4_0` (no official Russian speech; lay a recorded voice over it).
- Speech in Russian or a language outside a model's official list: test a short line first (A29, C3), or use path A.
- Cheap draft of dialogue: `seedance_2_5_flash` or `wan2_6` at the lowest quality, if their audio is acceptable.

Sound layers, in order: 1 separation, 2 dialogue, 3 foley (steps, cloth, touches, breath), 4 effects (hits, engines, clicks), 5 ambience, 6 music, 7 boosters.

Boosters: riser (rising tension before an event), hit or impact (accent on a cut), whoosh (fast pass or transition), braam (low trailer roar), drone (long tension hum), sub drop (low bass drop), reverse (suck-in before an event), stinger (short sharp scare). Generation prompts for them are in `templates/voice-and-music.md`.

Mix check commands (local, optional):
```
ffmpeg -i mix.wav -af ebur128=peak=true -f null -
ffmpeg -i mix.wav -lavfi "showspectrumpic=s=1700x300:legend=0:scale=log:fscale=log" spec.png
```
Music ducking under hits and final loudness: `sidechaincompress` then `loudnorm=I=-14:TP=-1.2:LRA=9`.

## Check before "ok"

Voice
- [ ] For a series, each hero has the same voice in every video (07.3, 07.7, 07.33).
- [ ] The language of speech is stated and the model supports it (07.10, 07.13).
- [ ] Each line fits the clip time, timed with a stopwatch or on finished audio (07.14, 07.60).
- [ ] No unwanted subtitles, titles or surprise music (07.21).
- [ ] No cut-off lines, no swallowed words, no spoken dashes (07.14, 07.22, 07.24).
- [ ] If tags were used: the model understands them, none was spoken aloud, tags only at changes of delivery (07.48 to 07.54).
- [ ] Numbers, dates, abbreviations and brands sound right (07.58).
- [ ] Voice emotion matches face and scene (07.62).
- [ ] No empty silent tail after the last line (07.84).

Lip sync and avatar photo
- [ ] Close-up, front view, one person in frame.
- [ ] Good light, eyes open.
- [ ] No glasses, microphones or hands near the face.
- [ ] Audio is clean and calm; length equals video length.
- [ ] Prompt is short and does not describe looks (07.40, 07.41).
- [ ] A 10-second test was done first (07.44).

Sound in the edit
- [ ] Music chosen; tempo changes with the acts.
- [ ] Voice split from the generation's sound.
- [ ] Everything meaningful on screen has sound: steps, hits, movements.
- [ ] Boosters sit on key moments.
- [ ] Voice louder than music; mix at -14 LUFS; loudness and spectrogram checked and the report says "not checked by ear" where true (07.64, 07.80).
- [ ] The video reads without sound: subtitles in place (07.79).
- [ ] Export matches the platform format.

The stage is closed only by the user's "ok" after they listen to the full video.

## Common mistakes

- A random voice across a series: the audience cannot recognize the character.
- More text than fits the video time: fast speech, stumbles, swallowed words.
- Models adding subtitles or music nobody asked for; long dashes spoken; the enhance option turning the line into English.
- Asking a model for a whisper or a language it does not do. Test the line on another model.
- Models that talk by default even with audio off.
- Music inside the generation: it cannot be separated from noises.
- Voice in the same generation as a 3D previz without a test (07.27).
- Sound described in one line at the end of the prompt: ignored.
- Avatar: long prompt with looks described, fast speech, background noise, extreme angles, hands near the face, small clothing patterns, saving on quality tier.
- Voice settings: noise removal on a clean recording, too much stability (monotone), too high similarity (artifacts), too much style exaggeration (unstable) where the tool has these.
- Old-version habits in v4: not naming the model (tags read aloud), advising `style`, `speed`, SSML or old stability presets, capitals on a whole phrase, contradicting tags on one phrase.
- Short scripts under about 250 characters on v3-type models are unstable (only if working on v3).
- Flat sound under a speed ramp (looks like lag); mickey-mousing every movement; sounding and grading shots that will be cut.
- Room echo in a self-recorded voice; a cleaning service that adds a jingle or a signature.
- No subtitles for viewers who watch muted.

## Tools

Higgsfield (check `models_explore` for current models and `estimate_audio_cost` or `estimate_video_cost` for credits before any paid run; nothing paid runs without the user's explicit yes on the exact list):
- `elevenlabs_v4`: dialogue and many voices, tagged speech (07.48 to 07.62).
- `text2speech_v2`: plain text to speech when tags are not needed.
- `elevenlabs_music_v2_5`: music (07.67).
- `create_voice`, `list_voices`, `create_voice_from_confirmed_audio`: create and reuse the hero voice (07.7, 07.8, 07.29).
- `voice_change`: path A, replace a voice in finished audio (07.28).
- `separate_stems`: split voice from noise and music (07.28, 07.70).
- `generate_audio`, `generate_audio_batch`: effects and ambience from English descriptions (07.76, 07.77). `mirelo_text_to_audio` is game-only, skip it.
- `generate_video` with `seedance_2_5`: own sound, audio references, lip sync with `start_image` plus `audio_references` (07.26, 07.38). `kling4_0` as an alternative for avatars; it has no official Russian speech.
- `media_upload`: bring your own recordings into a project.

Local, optional: ffmpeg for loudness and spectrogram checks and for ducking, a free editor for splitting and layering. A cleaning service for voice recordings is optional; if it adds a jingle or a signature, check both ends of the file (A47).

Open questions that touch this stage: C3 (lip sync with a video reference and with non-English speech), C5 (sound of MiniMax H3). See `docs/defaults.md`.
