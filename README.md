# AI video studio

A step-by-step method for making short AI videos (reels, ads, short films) with an AI agent. The agent leads you from an idea to a published video through 12 stages: idea, preproduction, film language, characters, frames, previz, video, sound, post, publishing. You make the creative calls and say "ok"; the agent does the prompts, checks and bookkeeping, and never spends your credits without asking.

Images, video and audio are generated on [Higgsfield](https://higgsfield.ai) with your own subscription.

## What you need
- **An agent.** Built for [Claude Code](https://claude.com/claude-code) (terminal, desktop app or VS Code). Other agents that read `AGENTS.md` (Codex, Cursor and others) work too.
- **A paid Higgsfield subscription.** All generation goes through it.
- **Optional:** [Blender](https://www.blender.org) 4.x or 5.x for the previz (stage 05), [ffmpeg](https://ffmpeg.org) for the edit, Python 3 for the checker script.

## Setup (Claude Code)
1. Install Claude Code: https://docs.claude.com/en/docs/claude-code/setup
2. Get this repo and open it:
   ```
   git clone https://github.com/ruslankholost/ai-video-studio.git
   cd ai-video-studio
   claude
   ```
3. Connect Higgsfield (once):
   ```
   claude mcp add --transport http higgsfield https://mcp.higgsfield.ai/mcp
   ```
   Then type `/mcp` inside Claude Code, pick `higgsfield` and log in with your Higgsfield account in the browser.
   If you already added Higgsfield as a connector on claude.ai (Settings → Connectors → Add custom connector → `https://mcp.higgsfield.ai/mcp`), Claude Code logged in with the same account sees it too, and you can skip this step.
4. Say: **"start a new video"**.

The agent creates a folder in `projects/`, asks for your brief, and starts stage 00.

## Other agents
Point the agent at this folder. It reads `AGENTS.md` first. Ask it to follow `.claude/skills/video-studio/SKILL.md` as its working loop, and connect Higgsfield's MCP server (`https://mcp.higgsfield.ai/mcp`) the way your agent adds MCP servers.

## How it works
- **Stages.** `docs/stages/00-idea.md` through `11-business-and-clients.md`. Each has principles, a workflow, a "check before ok" list and common mistakes.
- **Laws.** `docs/laws.md`: 48 rules the whole process rests on.
- **Lessons.** `docs/lessons-learned.md`: rules learned on real videos. Add your own; your latest decision always wins.
- **Templates.** `templates/`: prompt formulas for each model, storyboard, project folder, progress file.
- **Skills.** `.claude/skills/`: `video-studio` (the step-by-step loop), `blender-previz` (previz in Blender with check scripts), `ai-director` (director's method for cinematic pieces and spec ads).
- **Projects.** `projects/NN-word/`: one folder per video, with a `progress.md` that tells any new session where you stopped.

## Money
The agent never generates anything paid without your "yes". Before each run it shows what it will make, the model, the number of jobs and the price in Higgsfield credits, plus the stage checklist. Drafts are made at 480p; only the shots that made the cut get upscaled.

## Updating
`git pull` in this folder gets the latest version of the method. Your projects stay as they are.
