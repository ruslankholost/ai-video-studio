# Voice and music

Prompts for the voices, dialogue and music of stage 07 (`docs/stages/07-sound-voice.md`). Voices come from ElevenLabs models run through Higgsfield. Check `models_explore` for the current model ids and `estimate_audio_cost` for credits before any paid run, with the user's explicit "yes" on the exact list.

## Which tool for what

| Job | Higgsfield model | Notes |
|---|---|---|
| Dialogue between several characters | `elevenlabs_v4` | One call, a list of turns, each with its own `voice_id`. |
| A single voice reading a script | `text2speech_v2` | Simple narration or one speaker. |
| Music, with or without lyrics | `elevenlabs_music_v2_5` | Music from a text description. |
| New voice from a description | `create_voice` | Gives a `voice_id` to keep. |
| Existing voices | `list_voices` | Browse before creating one. |
| Replace the voice in a recording, keep the acting | `voice_change` | Use when the user performed the line. |
| Separate vocals from music | `separate_stems` | Cleaning a source. |

Generate through `generate_audio` (or `generate_audio_batch` for many lines). Never mix the tag rules of the models: tags written for one model can be read aloud by another.

## Voice direction

The model reads a scene like an actor. It knows who speaks, what came before, and how the line should sound. Direct it with three things only: audio tags, punctuation, and the context of the scene.

### Audio tags

- Square brackets only, in English, even when the line is in another language: `[shouts] Everybody out!` Round or curly brackets are read aloud.
- Put a tag before the words it affects. It keeps working until the next tag changes it, so tag only the moments where delivery changes, not every line.
- Combine in one bracket with commas: `[whispering, fearful]`, `[low, steady voice, restrained urgency]`.
- A chain runs in order: `[sighs] [sad] Well, that's it.` is a sigh, then a sad line.
- One emotion per line. Opposite tags on the same words blur the performance.
- Free direction works: `[like a sports commentator, speeding up]`, `[starting calm, then losing patience]`, `[out of breath after running up the stairs]`.
- Describe the voice, not an event. An ambiguous tag can turn into a sound effect. Write `[low, gravelly voice]`.
- Match the voice to the tag. A meditative voice shouts badly, a hyper voice whispers badly.
- Give the whole scene at once (up to 10,000 characters per request) rather than single lines. The model acts better with context.
- Before text in another language keep tags short. Long English directions before every line can cause repeated words. Put the long direction once at the start of the scene.

Tag vocabulary (open list, any plain English description works):

```
Emotion:    [excited] [playful] [amazed] [proud] [happy] [triumphant] [smug]
            [angry] [annoyed] [bitter] [frustrated sigh]
            [anxious] [nervous] [scared] [confused] [startled]
            [tired] [bored] [distant] [sad] [crying] [despair]
            [calm] [curious] [thoughtful] [warm] [reassuring]
            [sarcastic] [mischievously] [dry amusement]
Volume:     [whispers] [softly] [hushed] [barely audible] [shouts] [booming] [under his breath]
Pace:       [slowly] [rushed] [snappy] [drawn out] [gradually building energy]
Pauses:     [short pause] [pause] [long pause]
Reactions:  [laughs] [giggle] [soft chuckle] [nervous laugh] [sighs] [exhales sharply]
            [inhales deeply] [gasps] [clears throat] [gulps] [yawning]
Accents:    [British accent] [French accent] [thick Italian accent] [pirate voice]
Character:  [a tired detective who has heard it all before]
Sound:      [applause] [gunshot] [thunder rumbling] [footsteps] [door slams] [phone buzzing]
Dialogue:   [jumping in] [interrupting]
```

### Pauses, stress, pronunciation

- Pauses: `[pause]`, `[long pause]` (about 1.2 s), an ellipsis `...` for weight, a dash `-` for an interruption.
- Stress: capitals on one or two words ("this is VERY important"). Capitals on a whole line sound like shouting.
- Numbers, dates, currency and abbreviations: write them as spoken words ("one hundred percent", "half past two", "twenty-two dollars"). Write a brand as it should sound.
- Exact pronunciation: IPA between slashes inside the text, for example `/ˌbaɪoʊˈkemɪstri/`. SSML and `<break>` or `<phoneme>` tags do not work on v4.
- Keep each line short enough to speak in the time of its shot. Speech runs at about 2 to 2.5 words per second, and v4 reads 10 to 20 percent slower than v3, so leave margin or use `[rushed]` and `[snappy]`.

### Settings

v4 has two sliders:

| Setting | Effect | Default |
|---|---|---|
| `stability` | Lower is livelier and more varied, higher is more even, up to monotone. | about 0.5 |
| `similarity_boost` | How strictly the original voice is held. Too high also copies recording defects. | about 0.75 |

Starting points (adjust by ear):

| Task | stability | similarity_boost | Takes |
|---|---|---|---|
| Ad, reel | 0.35 to 0.45 | 0.75 | 2 to 4 |
| Audiobook | 0.5 to 0.6 | 0.75 | 1 to 2 |
| Teaching video | 0.6 to 0.7 | 0.75 to 0.8 | 1 to 2 |
| Character drama | 0.25 to 0.4 | 0.7 | 3 to 5 |
| Noisy clone | as the task | 0.6 to 0.7 | n/a |

Style and speed settings and presets like Creative, Natural, Robust do not exist on v4. If a parameter is silently ignored, that is why. Set the language explicitly when the line is short or mixed ("ru" for Russian). Use the same settings for every fragment of one voice. Take several takes, the model is not fully repeatable, and pick the best.

## Dialogue turns with `elevenlabs_v4`

Send the scene as a list of turns. Each turn has its own `text` (tags inside) and its own `voice_id`. Any number of speakers, up to about 2,000 characters across all turns in one request, so cut long scenes into pieces.

```json
{
  "model": "elevenlabs_v4",
  "turns": [
    {"voice_id": "VOICE_A", "text": "[cautiously] Excuse me, is this seat tak-"},
    {"voice_id": "VOICE_B", "text": "[jumping in] Free! [cheerfully] Sit down."}
  ],
  "stability": 0.4,
  "similarity_boost": 0.75
}
```

Check the exact field names with the tool's schema before the first call, they can differ from this sketch.

- An interruption: the first line stops on a dash, the next starts with `[jumping in]` or `[interrupting]`.
- A shared scene can be set by a tag on the first turn (`[courtroom]`).
- Before writing, make a table: speaker, voice description, `voice_id`.
- Leave a small silence before and after each line in the timeline, to cut and place it in `templates/montage.md`.

## One voice per character

1. At casting (stage 03) decide the voice of each character together with the user and record it in the character sheet (`templates/characters-and-refs.md`).
2. Browse `list_voices` first. A library voice is predictable and works with tags.
3. If no voice fits, design one with `create_voice` using the structure below, listen to the previews, and pick one. Voices made from a description take tags but sound less expressive than library or cloned voices, so prefer a library voice for the main character.
4. Write the `voice_id` and the settings (`stability`, `similarity_boost`) in the character sheet. Reuse exactly those values for every line, in every video of the series.
5. Test one neutral line and one emotional line in the chosen voice before committing the rest.
6. Voice a person's own recording with `voice_change` only with their consent.

Voice description structure:

```
Native <language and region>. <Gender>, <age range>. <Quality>.
Persona: <2 to 5 words>. Emotion: <2 to 3 adjectives>.
<One or two sentences on timbre, pace and delivery.>
```

Rules for it:
- Language and variant in the first sentence, or the voice drifts.
- Use `thick accent`, not `strong accent`. Never write "accent" when you mean intonation.
- Avoid the words reverb, echo, phone and tape. They damage quality unless a lo-fi effect is wanted.
- Quality marker: Ok, Good, Very good, Excellent, Studio or Broadcast quality.
- Preview text is at least a paragraph and matches the emotion of the voice (a calm dreamy voice gets a long smooth sentence, an energetic host gets an exclamation).
- Timbre words: deep, warm, smooth, rich, gravelly, raspy, breathy, light, husky, mellow. Pace words: speaking quickly, at a normal pace, deliberate and measured, relaxed and conversational.
- High guidance follows the description strictly, low guidance gives cleaner sound. Generation gives three variants.

Example:

```
Native English, neutral American accent. Female, 25 to 30. Excellent quality.
Persona: energetic lifestyle blogger. Emotion: playful, bright, confident.
Light, clear timbre with a smile in the voice; quick conversational pacing, punchy emphasis on key words.
```

## Examples of tagged lines

```
[excited, warm] Know what a Monday morning and good coffee have in common? [pause] Nothing... [playful] until you try ours. [confident] Roasted fresh every week. Delivered in TWO hours.
```

```
[vulnerable, quietly] I waited for you all winter. [pause] Every evening I put out two cups... [crying] and then I poured your tea away. [long pause] [bitter] And you just... forgot to call. [despair, barely audible] You just forgot.
```

Long text, split into fragments: keep the same voice and settings, and link fragments by passing the previous request id where the tool supports it, so intonation holds at the joins.

## Music with `elevenlabs_music_v2_5`

Describe the music in plain English: genre, mood, tempo in BPM, instruments, structure, length, whether it has vocals. Say "instrumental" if there are none. Give the length to the second of the video. Examples:

```
Slow cinematic piano with soft strings, 70 BPM, melancholic, builds gently to a warm ending, instrumental, 24 seconds.
```

```
Upbeat lo-fi hip hop, 90 BPM, dusty drums, warm bass, light vinyl crackle, steady loop-friendly groove, instrumental, 30 seconds.
```

- Decide the cut rhythm from the music (or the music from the cut) before the final edit; see `templates/montage.md` for beat alignment.
- The user is responsible for rights to any music they supply. Generated music is for use in the project as the platform permits, check its terms for commercial use.
- Use `separate_stems` to pull vocals or drums out of a source track when needed.

## Sound effects prompts

Generate one-off sounds with a plain description of the real sound. Be concrete: "heavy rain on a metal roof at night with distant thunder", not "rain".

```
cinematic riser, building tension, 6 seconds, dark thriller
deep cinematic impact hit with long reverb tail
fast whoosh transition, camera swipe
dark ambient drone, slow tension build
sub bass drop, deep boom
reverse suck-in effect before impact
footsteps on asphalt, city street, daytime
city street ambience, traffic, distant horns
car seatbelt unbuckle click
strong highway wind noise inside a car with the door open
```

Layer effects under the picture in the edit and keep them quieter than the dialogue.

## Check before "ok"

1. The model id is stated for every audio job, and tags are in square brackets in English.
2. Tags sit on changes of delivery only, one emotion per line.
3. No style, speed, SSML or preset settings are used with v4.
4. Numbers and abbreviations are written as spoken, capitals on at most two words in a row.
5. Every character has one `voice_id` and settings recorded in the character sheet.
6. Each line fits its shot with margin for slower v4 pace.
7. Dialogue scenes are under about 2,000 characters per request, and long text is split with matching settings.
8. Music has genre, mood, tempo, length and "instrumental" or lyrics stated.
9. The user approved the exact list of jobs and the credits from `estimate_audio_cost`.
