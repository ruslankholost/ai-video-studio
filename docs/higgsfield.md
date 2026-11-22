# Generating through Higgsfield

The user pays for images, video and audio with their own Higgsfield subscription. The agent reaches Higgsfield through its MCP server (setup in `README.md`). Everything here is about spending the user's credits well and never by surprise.

## The money loop (every paid run)
1. **Pick the model by the stage document**, not by habit or price. Check its current limits with `models_explore` (`action: "get"`, `model_id`): durations, aspect ratios, media roles, parameters. Models change often; don't trust memory.
2. **Get the price** with `estimate_image_cost`, `estimate_video_cost` or `estimate_audio_cost`, using the exact params you will send (model, duration, resolution, aspect ratio, media). The quote returns a `quote_ref`.
3. **Ask for "yes"** in one message: what, model, number of jobs, settings, credits, plus the stage checklist with yes/no per item and any deviation from the method named.
4. **Generate exactly what was quoted:** pass `params: {"ref": "<quote_ref>"}` so nothing drifts between the quote and the run.
5. **Wait** with `jobs_wait` (batch jobs) or the job widget, then show the result to the user.
6. **Download** the result into the project folder (`curl -L -o projects/NN-word/video/s03_take1_480p.mp4 "<result url>"`) and log the spend in `progress.md`.
7. **On a timeout, never resubmit blindly.** The job may already be running; look it up first.

`balance` shows the credits left. `transactions` shows what was spent.

## Uploading your own files
References (start frames, reference cards, the previz video, a voice clip) must be uploaded before a model can use them.
1. `media_upload` with the filename (or `files: [...]` for up to 20 at once). It returns an upload URL and a media id.
2. Upload the bytes: `curl -X PUT -H "Content-Type: <mime>" --data-binary @<file> "<upload_url>"` (use the exact curl command the tool returns if it gives one).
3. `media_confirm` with the media id(s) and type (`image`, `video`, `audio`).
4. Pass the media id in `params.medias` as `{"value": "<media id>", "role": "<role>"}`. A finished job id can be used the same way, so a generated image can feed a video without downloading and uploading again.

Write every media id into `prompts.md` next to the file it came from, so the next session can reuse it.

Recurring characters and voices can also be saved on Higgsfield as reusable elements (`manage_reference_elements`, `show_reference_elements`; voices with `create_voice` and `list_voices`). Record their ids in the project too.

## Which model for which stage
Check `models_explore` for anything newer before you start a project.

| Stage | Task | Model id | Notes |
|---|---|---|---|
| 03, 04 | Reference cards, start frames, establishing shots | `nano_banana_pro` | Main image model. Up to 14 reference images (`image_references`). 2k is enough for start frames. |
| 03, 04 | Edits, text in the picture, alternatives | `gpt_image_2_6`, `seedream_v5_pro` | Use when Nano Banana keeps missing a detail. |
| 03 | Realistic people, fashion | `soul_2` | One reference image only. |
| 06 | Main video | `seedance_2_5` | Omni reference: `start_image`, `end_image`, `image_references`, `video_references` (the previz as @Video1), `audio_references`. 4 s minimum. Drafts at 480p. |
| 06 | Cheaper tests | `seedance_2_5_flash` | Same inputs, lower quality. Only for tests the user agreed to. |
| 06 | Alternatives | `kling4_0`, `minimax_h3` | Only when the stage document says Seedance is the wrong tool for that shot (template: `templates/video-prompt-other-models.md`). |
| 06 | Lip sync on an existing clip | `sync_so` | Video plus audio in. |
| 07 | Dialogue, voices | `elevenlabs_v4` | Up to 10 voices in one dialogue; keep one voice id per character. |
| 07 | Single voice, other engines | `text2speech_v2`, `qwen_audio_tts` | |
| 07 | Music | `elevenlabs_music_v2_5` | Set the duration; instrumental with `force_instrumental`. |
| 08 | Upscale | local upscaler first; paid `bytedance_video_upscale` or `topaz_video` only for clips that need it, with a separate "yes" | Upscale only what made the final cut. |

## Rules that save credits
- **Draft at 480p, final only for what made the cut.** Never plan a paid 1080p pass for every clip.
- **One chunk first.** For a video in several chunks, generate the first, check it against the previz, then ask for the rest.
- **Regenerate only the bad shot,** never the whole video.
- **Don't change the model to save credits.** A cheaper model that ignores the previz costs more in retakes. If you think a cheaper route works, test it on the hardest shot, not the easiest, and only with a "yes".
- **Never use free or "unlim" generations unless the user asks.** If Higgsfield returns a question about which balance to use, ask the user.
