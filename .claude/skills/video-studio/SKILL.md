---
name: video-studio
description: "Entry point for making an AI video in this repo: guides the user from idea to publication through stages 00-11, one step at a time, asks \"shall we go on?\" after each step and runs a check before every \"ok\". Use when the user says \"start a new video\", \"new reel\", \"continue the video\", \"where are we with the video\", \"let's make a video\", or does any work on a video in this repo."
---

# Video studio: run a video through the method

The user wants a director who misses nothing. Things get missed when work is done from memory or from a summary. So there are three rules: every step comes from the stage document, read again; every step is marked in the project's `progress.md`; every "ok" is preceded by the stage checklist and an outside review.

Order of authority is in `AGENTS.md`: the user's latest decision (`docs/lessons-learned.md`) → laws (`docs/laws.md`) → defaults (`docs/defaults.md`) → stage document (`docs/stages/`) → templates (`templates/`).

## Session start
1. Read `AGENTS.md` and `docs/lessons-learned.md` in full. If the repo is a git clone, run `git pull` to get the latest method.
2. Check that the Higgsfield tools are connected (for example `balance`). If not, point the user to the setup in `README.md`. Without them you can still do stages 00-02.
3. Find projects: `projects/*/progress.md`. Show the user in one or two lines where each video stands ("01-coffee: stage 01, step 3, waiting for your script notes") and ask: continue this one or start a new one?
4. New video: create `projects/NN-word/` from `templates/project-folder.md`, copy `templates/progress.md` into it, ask for the brief (what, for whom, platform, length, credit budget), then stage 00 from step 1.

## Every step
1. Open the current stage document. Read it in full when entering the stage. Before each step, read that step in "Workflow" again and the principles it points to. Never work from memory or a summary, including after the conversation was compacted.
2. Check the stage input ("Input and output"). If it is missing, go back one stage.
3. When entering a stage, copy its "Workflow" into `progress.md` as a checklist with the same numbers.
4. Do the step. If the step needs the user's words or decision (brief, their ideas, a vote, an "ok"), ask and wait. Don't invent it for them.
5. Show the result in the chat, write it into the project files, mark the step in `progress.md` with the date and the user's words. Ask "shall we go on?".
6. If the user changes the idea or a decision, note in `progress.md` which steps it rolls back and tell them in one line.

## Before any paid run
1. Read the stage's "Workflow" and "Check before ok" again.
2. Get the price: `estimate_image_cost`, `estimate_video_cost` or `estimate_audio_cost` for the exact settings you will send.
3. Send one message with: what you will generate, model, number of jobs, settings (resolution, length, references), credits, and the stage checklist with yes/no on each item. Name every deviation from the method.
4. Wait for an explicit "yes". Run exactly what was approved, nothing more.
5. Log the spend in the "Credits spent" table of `progress.md`.

## Before the "ok" on a stage
1. Go through the stage's "Check before ok" item by item and write in `progress.md` what is done and what is not.
2. Independent review. If you can start a sub-agent, give it only paths, not your conclusions. In Claude Code use the Agent tool with a cheaper model (`sonnet` or `haiku`). Prompt: "Read docs/stages/<stage>.md in full and every file in projects/<project>/. List what the stage requires that the project is missing or did weakly: skipped steps, principles, checks, outputs. Only a list, each item with the principle number or the line of the document. Change nothing." If you cannot start a sub-agent, do the same pass yourself, slowly, against the document.
3. Fix what was found or show it to the user. Only then ask for the "ok". An "ok" covers one stage and does not carry over.

## Keep in mind
- Generate only through the method in the stage document. Video is Seedance 2.5 with the previz as @Video1 and the template prompt (stage 06). A shortcut that saves credits but skips the method wastes more credits later.
- Check every image at full size before showing it, and check start frames in pairs (same place, same direction, same props, real sizes, hands, no doubles).
- Before the money stages, test the ending on paper: if the last shot is not a turn, the video will not be watched to the end, however well it is generated.
- Every "don't do that" from the user goes into `docs/lessons-learned.md` (with the date) and into the project's `experience.md`.
- Previz: skill `blender-previz`. If Blender is not installed, say so and offer to install it; don't skip the previz silently.
