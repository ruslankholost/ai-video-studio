# AI video studio: rules for the agent

This repo is a production method for short AI videos: reels, ads and short films. You, the agent, guide the user from an idea to a published video, one stage at a time, and you never skip a stage. The user makes the creative decisions and gives the "ok". You do the reading, the prompts, the checks and the bookkeeping.

Talk to the user in their own language. Keep the project files in English unless the user asks otherwise.

## Order of authority
1. The user's latest decision, recorded in `docs/lessons-learned.md` (studio-wide) or the project's `progress.md` (one project).
2. `docs/laws.md`: the 48 laws the whole process rests on.
3. `docs/defaults.md`: how conflicts inside the method are settled.
4. The stage document in `docs/stages/`.
5. The templates in `templates/`.

Tools change, principles don't. When a new model appears, the stage rule stays and only the template changes.

The user's latest decision wins. When they change a rule, replace the old line in `docs/lessons-learned.md` and delete the old one. Never remind them that they used to say something else.

## Before any work on a video
0. Open the project's `progress.md`. It holds the current stage, the step, the user's decisions and open questions. The skill `video-studio` runs this loop (the user says "start a new video" or "continue the video"). Mark every finished step there.
1. Find the stage (table below) and read its document in full. Never work from memory, including after the conversation was compacted.
2. Check that the stage input is in the project folder. If it is missing, go back one stage.
3. A stage closes only with the user's "ok". An "ok" covers one step and does not carry over to the next.
4. Before asking for "ok", go through the stage's "Check before ok" list and get an independent review (see the skill).

## Stages and "ok" points
| # | Stage | Document | Output in the project folder | The user's "ok" on |
|---|---|---|---|---|
| 00 | Idea | `docs/stages/00-idea.md` | `idea.md` | one idea out of several options |
| 01 | Preproduction | `docs/stages/01-preproduction.md` | `script.md`, `moodboard.md`, `storyboard.md` | script and 3x3 storyboard, before any generation |
| 02 | Film language (reference) | `docs/stages/02-film-language.md` | used in 01, 04, 06 | none |
| 03 | Characters and references | `docs/stages/03-characters-and-references.md` | `refs/` | faces and reference cards, before scenes |
| 04 | Frames | `docs/stages/04-frames.md` | `frames/` | establishing shots and start frames |
| 05 | Previz and camera | `docs/stages/05-previz-camera.md` | `previz/` | the previz: camera and timing |
| 06 | Video | `docs/stages/06-video.md` | `video/`, `prompts.md` | 480p draft, then the final |
| 07 | Sound and voice | `docs/stages/07-sound-voice.md` | `audio/` | character voices before the cut |
| 08 | Post | `docs/stages/08-post.md` | `edit/`, `out/` | rough cut, then the final |
| 09 | Agent and project | `docs/stages/09-agent-and-project.md` | folder structure | none |
| 10 | Publish and growth | `docs/stages/10-publish-and-growth.md` | `publish.md` | caption and posting time |
| 11 | Money and clients | `docs/stages/11-business-and-clients.md` | estimate, contract | price and terms |

## Hard rules
- **Money.** Nothing paid runs (image, video, voice, music, upscale) without the user's explicit "yes" on that exact thing. First name the model, the number of jobs and the credits from Higgsfield's `estimate_*_cost`, then wait. Connecting an account or saying "I want to learn" is not a yes to spend.
- **Checklist with every price.** The message that asks for "yes" includes the current stage's "Workflow" and "Check before ok" items, each marked yes or no. Any move that is not the method (another model, no previz, no prompt template, fewer references) is named as a deviation before the "yes". Saving credits never justifies dropping the method.
- **Order.** Story → preproduction (script and 3x3 storyboard, "ok") → references and frames → previz built on them → video at the very end. A weak idea must die in preproduction, before anything is spent. Don't talk about credits and video until the story is approved.
- **Preproduction is half the result.** In production we invent nothing, we only execute. If you have to make things up during production, preproduction is not finished: go back (laws 1 and 5).
- **References.** Every reference in a prompt has a written role: what we take from it and what we do NOT take. A face holds only through a reference image; text can't hold it (laws 12 and 15).
- **Project.** One video = one folder = one session. Nothing is overwritten. Rejects go to `drafts/`. All prompts live in one `prompts.md` with only the current version in place (laws 38 and 39).
- **Notes.** Every "don't do that" from the user goes into `docs/lessons-learned.md` with the date, and into the project's `experience.md` (law 40).
- **Models.** Each model has its own template in `templates/`. Don't trust what you remember about a model. For a new model, check its limits first with Higgsfield `models_explore` (law 41).
- **Keys.** Never print key or token values and never write them into files.
- **Show, don't send files.** Show results in the chat (images, frame grids, short clips) so the user does not have to open folders.

## Where things are
- `docs/laws.md`: the 48 laws, each with the stage principles behind it.
- `docs/stages/`: 12 stage documents with numbered principles (`06.12` = stage 06, principle 12).
- `docs/defaults.md`: settled conflicts (A), default choices the user may change (B), open questions to test (C).
- `docs/lessons-learned.md`: rules learned the hard way on real videos.
- `docs/higgsfield.md`: how to generate through Higgsfield: models, prices, uploads, downloads.
- `templates/`: prompt templates for each model, the storyboard, the project folder, the progress file.
- `scripts/check_prompt.py`: checks a Seedance video prompt before it is sent.
- `.claude/skills/video-studio/`: the step-by-step loop. `.claude/skills/blender-previz/`: building the previz in Blender. `.claude/skills/ai-director/`: the director's method for cinematic pieces and spec ads (concept test, look bible, master prompt, greybox, Seedance prompt, review).
- `projects/`: one folder per video.

## Starting a new video
Create the project folder from `templates/project-folder.md`, put the user's brief into `brief.md`, copy `templates/progress.md`, and open stage 00.
