# Project folder

One video = one folder = one agent session. Every project has the same layout, so the agent always knows where things are, and a file name tells you what it is and which version.

Create it with the agent: "start a new video". The folder goes to `projects/NN-word/`, for example `projects/01-coffee/`.

```
projects/NN-word/
  progress.md       where the project stands: stage, step, the user's decisions, open questions (from templates/progress.md)
  brief.md          what, for whom, platform, frame format, length, deadline, credit budget
  idea.md           logline in one sentence + limits (stage 00)
  script.md         the script (stage 01)
  moodboard.md      3-5 look phrases that go into every prompt + the style block (stage 01)
  storyboard.md     shot table: time, shot size, camera, action, emotion, transition, sound (stage 01)
  prompts.md        every prompt of the project: images on top, a --- line, then video; only the current version stays in place
  experience.md     what worked and what failed in this project, with dates
  refs/             reference cards: faces, bodies, outfits, props, locations; reference videos
  frames/           establishing shots and start frames (stage 04)
  previz/           Blender scene, render frames, previz videos (stage 05)
  video/            raw video generations by shot and take (stage 06)
  audio/            voices, music, sound effects (stage 07)
  edit/             cuts and intermediate files (stage 08)
  drafts/           anything replaced; nothing is deleted
  out/              finished files: final_v1.mp4, final_v2.mp4, cover.jpg
  publish.md        caption, cover, platforms, time (stage 10)
```

## Rules

- **Never overwrite.** A new version gets a new name: `ref_s03_v2.mp4`, `final_v3.mp4`. The old one moves to `drafts/`.
- **Names say what and which version:** `s04_take2_480p.mp4`, never `final_final2.mp4`.
- **All prompts live in `prompts.md`.** The current version sits in place; replaced versions go under a "Replaced" heading at the end of the file with the date and why.
- **Media files stay out of git** (see `.gitignore`). Text files (progress, script, prompts) are small and worth committing.
- **Finished video:** MP4 H.264, yuv420p, CRF about 20, `-movflags +faststart`, sound around -14 LUFS.
