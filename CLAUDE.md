@AGENTS.md

Claude Code notes:
- The step-by-step loop is the skill `video-studio` (`.claude/skills/video-studio/SKILL.md`). Load it whenever the user talks about making a video.
- The previz is built with the skill `blender-previz`.
- For a cinematic piece or a spec ad ("full Hollywood", "think like a director") also load the skill `ai-director` (`.claude/skills/ai-director/SKILL.md`); the stage documents win over it.
- Higgsfield tools come from the Higgsfield MCP server (setup in `README.md`). If they are missing, tell the user to run `/mcp` and log in.
