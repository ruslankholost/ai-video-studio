# 09 Agent and project

This stage runs through all the others. It describes how the agent (Claude Code, or another coding agent that reads `AGENTS.md`) is set up, how one video lives in one project folder, and how work moves from idea to delivery while the user only approves. Read it once when you set up the studio, and read it again at the start of every project.

## Input and output

Input:
- The decision to make a video and a short working name (plain words, no dates, for example "spare-option" or "coffee-ad").
- A coding agent with a paid plan, opened in the studio folder.
- A Higgsfield subscription connected to the agent (images, video, audio, upscale).
- Optional local tools: Blender (previz), ffmpeg, Python.

Output:
- A configured studio: `AGENTS.md` (agent rules), `docs/`, `templates/`, `scripts/`, `projects/`, and a `.env` for any extra API keys.
- A project folder `projects/<NN-word>/` (for example `projects/03-coffee-ad/`) built from `templates/project-folder.md`, with a `progress.md` from `templates/progress.md`.
- Inside the project: brief, script, storyboard, one prompts file, project experience notes, folders for images, video, previz, work files and final output.
- The project then goes through stages 00-08 and ends with a delivery in the output folder.

## Principles

### A. Roles and how the agent works

1. **The user is the director, the agent is the executor.** The user sets the task, looks at results, corrects, and says "ok" on paid generations. The agent does, checks and shows. Eyes and taste stay with the human; the agent takes the manual work.
2. **An agent runs a chain of steps; a chat answers questions.** The agent reads, creates and edits files, runs code and programs, checks the result and fixes it. Give it a task, not a question.
3. **The model is the same; the tools around it differ.** Files, terminal, skills and project memory (`AGENTS.md`) make the difference. A plain chat window can advise on editing. A coding agent on your computer edits.
4. **The agent works only inside the folder it was opened in.** Always start it from the studio or project folder, or it cannot see the files it needs.
5. **The setup in one line:** user (director), agent, `AGENTS.md` (rules), skills (detailed instructions for one job), connections (the agent's hands: Higgsfield, optional local tools).
6. **Every project follows one order:** brief, preproduction, production, postproduction, delivery. At each step the agent loads the right skill or reads the right stage document on its own. At the end of each stage it gives a short summary and asks "continue?". The user does not have to name skills.
7. **Preproduction decides most of the result, so do not rush to generations.** Weights: preproduction 50 percent, production 25, postproduction 25.
8. **Ask for the frame format before the first generation.** Changing the format later means redoing every generation.
9. **The studio works with any agent that reads `AGENTS.md`.** Use the agent the user already pays for. All prompts in this repo are plain text and work in any of them.
10. **Use the strongest model with high reasoning effort for video, 3D and long tasks; lower effort for small edits.** Effort is how long the model thinks before acting. In a 3D scene a wrong number means a car facing backwards or a camera inside a wall, so use high effort there.
11. **The agent cannot hear sound or see a screen.** It checks audio by loudness numbers and a spectrogram and writes "not checked by ear". It checks video with a contact sheet of frames; at about 5 frames per second it can miss text on a face. It does not know what is on the user's screen unless told.
12. **Invent nothing in facts.** Dates, numbers, prices and names come from the user's material or checked sources. If sources disagree, show the disagreement and let the user decide.

### B. One video, one folder, one session

13. **One video = one folder = one agent session.**
14. **A new project gets a new session; a big new step gets a new chat.** On every step the agent rereads the whole conversation, so a long chat gets more expensive with every message.
15. **Collect corrections into one list and send them in one message.** Do not hurry a long task with questions. When a usage limit ends, wait for the reset; the history stays. For an unrelated question, clear the context first.
16. **Every project has the same folder structure.** The agent always knows where things are, and the user knows from a file name what it is and which version. Set the order up on day one, because after a month there are dozens of folders. The scheme is in `templates/project-folder.md`.
17. **Name files by meaning: scene, take, quality.** `part1_take2_480p.mp4`, not `final_final2.mp4`.
18. **Nothing is overwritten.** A new version gets a new working name; the old one moves to the drafts folder as `draft_<what>_vN.<ext>`. Every assembly is a new file: `_v2`, `_v3`.
19. **Rejects are not deleted; they go to drafts.** A good frame from an old take can always be brought back. The command phrase is "reject".
20. **Every generation is saved at once into the project folder** (images, video, previz each in their folder). Intermediate material (check frames, cut pieces) goes to the work folder.
21. **Keep a library.** Copy every approved reference card, generation and finished video to a shared library folder as `<who or what>__<description>.<ext>`, with a line in an index file. In half a year it is the studio's bank of characters and locations.
22. **Write project experience at once.** Every mistake and every trick that worked goes into the project's experience file with a date and an example. A rule that applies everywhere also goes into `AGENTS.md`, so the next project does not repeat the mistake.
23. **Never hand the agent a password.** If an installer asks for an admin password, the user types it in the terminal and then tells the agent "done".
24. **Programs are installed by the agent, not by hand.** The user pastes one request for their system (section "Setup prompts" in the Workflow). The agent checks what is installed, installs only what is missing, and shows a table: program, version, ok or what to do. If something fails, paste the whole error and write "fix it".
25. **Install only the official agent plugin or app, and trust the folder when asked.** Look-alike extensions exist. Without folder trust, extensions run in a limited mode.

### C. AGENTS.md and brand notes

26. **Your style, rules and formats are written once in `AGENTS.md`; the agent reads it at the start of every session.** Do not write the file by hand: ask the agent to draft it and ask what to change.
27. **`AGENTS.md` grows by itself.** Each "do not do that" or "always do it this way" from the user is added to the rules section with a date and a short example. After a month the agent works the way the user wants without reminders. Example rule: "never suggest bubble gum bubbles".
28. **Never overwrite an existing rules file.** Add the missing sections at the end.
29. **Sections of the studio rules file:** Who I am, How we work, Folders, Files and versions, Generations, Checking and delivery, Saving usage limits, My rules. Four questions fill "Who I am": name or handle; niche and audience; platforms; default frame format.
30. **Editing rules live in the same file:** loudness target, formats (9:16 and 16:9), subtitle size, folder layout of a video, delivery (mp4, cover, text for the post), "you cannot hear sound", "I send corrections as a list". See stage 08.
31. **A brand file holds one client's visual rules in text:** palette with a role for each hex color, fonts and sizes, subtitle style, motion on beat fractions, 3-5 signature moves, transitions, safe zones, sound, and a list of "never do". One client, one brand folder. Name the brand in every prompt ("Brand: coffee-ad") and depart from the file only when the user asks.
32. **Write rules as checkable statements.** Not "be careful with money" but "no paid generation before the user's explicit yes". Not "make it pretty" but "warm side light, golden hour, soft shadows".
33. **API keys live in one `.env` file. They never go into chat or into other files.** Read the file masked, for example `sed -E 's/=.*/=<hidden>/' .env`. A key can spend the user's money. If a key leaks, revoke it and issue a new one.
34. **Instructions work on three levels:** personal preferences (who you are, how to talk to you), project instructions (where the work happens and what is remembered), skills (how to do one job). In this repo they are `AGENTS.md` plus the agent's own settings.
35. **A good instruction has five parts:** role, context, style, rules, format. Do not try to write a perfect one at once. Start with the basics, work for 2-3 days, then paste the mistakes and ask the agent to add rules that close them. The agent learns from real examples, not from a description of style.
36. **For writing and planning, split the roles:** a screenwriter, a storyboard artist, a director, an analyst. Each owns one stage. The matching prompts are in `templates/script-and-storyboard.md`.

### D. One prompts file

37. **All prompts of a project live in one `prompts.md`, and only the current version stays.** Prompts get lost in chat; with 40 of them you cannot find the old one to rerun a single shot. A rewritten prompt replaces the old one in place. Layout: images on top, a double rule `---`, video below; under the rule for Seedance: the upload order of files, a readable version for review, and the version that goes into generation.
38. **Read and fix a prompt before generating, while no credits are spent.** Open the file in the editor's preview mode.
39. **The agent edits the prompt in place, from the user's words.** A correction means rewriting the whole prompt, not patching pieces. Corrections can be dictated by voice, second by second.
40. **Long prompts are written by the agent, not by the human.** Hand-writing 2000-3000 characters for every shot costs half a day per shot. Describe the scene in plain words and ask the agent to write the prompt. The user stops writing prompts and builds the system that writes them.
41. **Give the agent context:** all references, the idea and script, the piece of the storyboard for this shot, and what is going on in the assembly (which tool, what goes in, what must come out). The last item is skipped most often and decides the most. A prompt written without context is written in a vacuum.
42. **The order of references in the prompt matches the upload order.** The agent writes the upload order explicitly. If the order is mixed up, the model puts the heroine's face where the car should be.
43. **Say what is wrong point by point** (angle, shot size, object in the background, blur), or give a new reference and ask for a full rewrite, or edit on top of the frame and forbid touching the rest. A detail changes by forbidding change to everything else: "same face, same skin tone, same pose, same clothes, same background and light, change only the hair".
44. **A video prompt has one block per shot on whole seconds,** a reference link for every reference visible in it, its own camera move, and the acting of each character in body and face. Time is always whole seconds, because the model does not read fractions.
45. **Negatives are specific to the scene** (snow, car driving backwards). Do not write generic junk such as "extra fingers". Some models have their own negative block; follow that model's template (stage 06).
46. **A skill's signature or tool note never goes inside the prompt body.** Models draw any text they find in the prompt into the frame.
47. **A screen with text in the frame (phone, sign) is a separate reference with the exact text.** Check the letters by eye.

### E. Progress tracking and drafts

48. **Each project keeps a `progress.md` from `templates/progress.md`.** It records the stage, what is approved, what is open, what was generated and what it cost. A new session reads it first, so no state lives only in a chat.
49. **Outputs are ordered by the work:** characters, locations and objects, storyboard, previz, raw generations, processed. Within a group, keep story order so that gaps are visible. Old versions and rejects sit in drafts and are marked as such in `progress.md`.
50. **After each new generation or version the agent updates `progress.md` in the same turn.** The user never has to rename or sort files by hand. If the user moved or renamed files, the agent asks before reorganizing.
51. **Generated files are shown as a contact sheet in chat,** not one frame at a time (saves usage limits). The file is also saved to the project folder under its meaningful name.
52. **Check video with a contact sheet, not on trust:** the style of each frame, the direction of motion across several frames in a row, faces and hands. Check the finished file itself, not intermediate ones.

### F. Approval stages and "ok" before paid generation

53. **Paid generation only after the user's explicit "yes" on the exact list.** Before any paid run the agent shows: model, mode, frame format, duration, resolution, with or without sound, which files go in and in what role, the price in credits from the matching `estimate_*_cost` call, the prompt, the number of jobs, and the stage checklist with yes/no per item. A "yes" for one run does not carry over to the next. A move that is not the method is named as a deviation. Never state fixed prices from memory.
54. **Cheap first: a draft, low resolution, a short test of 4-5 seconds.** Expensive when it looks right. Order a draft in draft mode so it can be finished at full resolution as the same take (stage 06). Build a long scene in batches of 10-15 seconds. Regenerate only the bad shot.
55. **After a generation the agent states how many credits went.** Plan time and credits for rerolls: up to 95 percent of generations can be bad. That is normal.
56. **The agent starts generations through the connection.** The user does not paste prompts, upload references or download by hand. The phrase "references and prompt are approved, generate" makes the agent show settings and price and wait for "ok".
57. **The agent runs the stage approvals.** At the end of brief, preproduction, production and postproduction it summarizes and asks "continue?". Inside stages there are further approval points: the edit plan before render, the storyboard before animation, the 3x3 storyboard before video ("no video is generated before ok"), the blocking in Blender ("show it and wait for ok"), the numbers table before generation.
58. **Do not promise "two minutes and done".** Generation and corrections usually take 30-90 minutes. Say so, together with the price, before the "ok".
59. **Do not rush to generations without preproduction.** Storyboard frames are not fed to the video model. What goes in are reference cards of characters, locations and objects that run through the video. A reference card (a sheet of views) is only for things that repeat.

### G. Skills for each model, because model knowledge goes stale

60. **The agent's training data is old.** Without a skill, asking for "a prompt for image model X" gives something generic and averaged.
61. **A skill is a document with instructions for writing prompts for one model:** formula, character limit, practices. It is built once and grows: when you find a new trick, say "add this to that skill".
62. **To build a skill for a new model:** ask the agent to find the official instructions, read forums for practice and strengths and weaknesses, and write the skill. It must contain the formula written out and the recommendations (how many characters, the model's limit). After that, one line is enough: "write a prompt for such-and-such image in such-and-such model". The prompt for building a skill is in "Formulas" below.
63. **Keep skills in the repo and keep them current.** This repo carries its own skills under `.claude/skills/`. When a model changes, update the skill instead of trusting memory. Name the skill in the request when the agent does not pick it up on its own.
64. **Read any third-party skill or plugin before connecting it.** Check its files for hidden characters (direction switches, zero-width characters), because hidden instructions get planted there. Install extensions only with the user's consent and an explanation.
65. **Skills give stability.** Without a skill you explain every time and the result is unpredictable. With a skill the agent already knows the format. The more exact the skill and the clearer the request, the more stable the result.
66. **A good skill rejects "dynamic shot" and demands specifics** (operator commands). Example: "camera slowly pushes in from medium to close-up, shallow depth of field".
67. **Do not sign posts with tool names.** No line like "made with tool X" in publishable text. Tools are credited only in a "how it was made" breakdown or when there is a partnership.
68. **Keep a task-to-skill table in the rules file.** Pick the model by the task: a small model for simple jobs, a medium one for balance, the strongest for the main work. If unsure, use the strongest.

### H. Connections, keys, models

69. **Higgsfield connects as a connector** in the agent's settings (custom connector, address `https://mcp.higgsfield.ai/mcp`, sign in to Higgsfield). No API key is needed. A subscription is required. The free check is "show my Higgsfield balance". Terminal fallback: `claude mcp add --transport http --scope user higgsfield https://mcp.higgsfield.ai/mcp`, then authenticate in `/mcp`.
70. **Choose one connection path.** Connecting both through the terminal and through the web account doubles the tools.
71. **Keep any other service key in `.env`** (see 33). Voice and music run through Higgsfield (`elevenlabs_v4`, `elevenlabs_music_v2_5`), so no separate key is needed for them. Add keys only for a service you really use.
72. **If the user uses another provider for a step** (an upscaler, a cleaner for voice recordings), its key goes into `.env` with an empty value when unused. The agent creates `.env` itself.
73. **Before a new task the agent checks models and balance.** It never guesses model ids or limits. The model list changes, so call `models_explore` for current models and the balance tool for credits. If there is no Higgsfield connection, the agent still writes prompts and the user generates by hand.
74. **Setup is one request: "set up the working environment".** The agent checks what is connected and installed and shows a table, then creates the studio structure, the rules file and `.env`.
75. **Aggregator websites are not opened as separate windows.** Reference picking happens through the agent and the connection (references attached with `@` in generation calls). The agent replaces manual work in browser windows.
76. **Payment and regional access of services are the user's own matter.** The agent never enters payment details.
77. **Plans:** the coding agent needs a paid plan (free plans do not include it or only cover short tasks); Higgsfield needs a subscription with credits. Heavy use of the agent needs a higher tier because of the usage window.

### I. Voice input

78. **Voice is faster than typing.** A dictation app that types into any window lets the user explain in one minute what takes five minutes to type. Put the cursor in the agent chat and dictate.
79. **Corrections by voice, by second and scene:** "in the third shot the camera is too low, and let the heroine look at him, not out of the window". The agent rewrites the prompt in place.
80. **A whole project can be dictated.** The agent writes the script, splits it into steps, picks the video model, writes the prompts and counts the cost. The user still approves each paid step.
81. **Character voices are made by the agent** (stage 07) and placed in the video, with the generation's own voice set to zero. Check voice and sound on the finished file: duration, loudness, a transcript of the start and end.

### K. Saving usage limits

82. **Rules for saving limits:** a new project means a new session; corrections as one batch with one render; look at frames as one contact sheet; run long renders in the background without asking every minute; keep brand and video in separate chats; while editing, render still frames, not the full video; use templates for what repeats.
83. **The agent can also program on the side** (rename 300 files, build a portfolio site, make a request bot) and run a content batch from a template: descriptions and folder layout for a set of videos.
84. **You can follow the work from a phone** with the agent's remote-control feature, if the computer is on and online.

## Workflow

Setup, once:

1. Install the code editor and open the studio folder (trust the folder when asked).
2. Install the official agent plugin or app and sign in with the paid account.
3. Optional: a voice dictation app.
4. Paste the program request for your system (see "Setup prompts") and read the table the agent returns.
5. Choose the strongest model and high effort for video and 3D work.
6. Connect Higgsfield (principle 69) and run the free balance check.
7. Put extra keys, if any, into `.env`. The agent creates the file; the user types the values.
8. Ask: "set up the working environment". The agent checks the table, makes sure `AGENTS.md` exists, asks the four "Who I am" questions and writes the answers into `AGENTS.md`.
9. "Ok" from the user: the setup table is all green.

New project:

1. The user says: "start a new project <name>". The agent makes `projects/<NN-word>/` from `templates/project-folder.md`, copies `templates/progress.md` into it as `progress.md`, and asks for the task. Frame format is asked before the first generation.
2. Open a new agent session for this project only.
3. Go through stages 00-08 in order. At each stage the agent reads that stage document, works, and at the end gives a summary and asks "continue?" (principle 57).
4. The agent writes all prompts into `prompts.md`. The user reads the file and says "references and prompt are approved, generate".
5. Before each paid run the agent sends the price message of principle 53 and waits for the user's "yes" on that exact list. **Ok needed.**
6. The agent runs the generation, saves results into the project folder, updates `progress.md` and shows a contact sheet.
7. A shot the user does not like: "reject". The agent moves it to drafts, notes why, and proposes how to redo it.
8. After each step the agent writes what worked and what did not into the project experience file with a date. Rules that apply everywhere go into `AGENTS.md`.
9. Approved assets are copied into the library.
10. Delivery: mp4 H.264, yuv420p, CRF 22, faststart, sound at about -14 LUFS, as a new version `_v2`, `_v3` (details in stage 08).
11. At the end of the project, update `progress.md` and record the final cost.

Setup prompts (the agent-ready text lives here and in `AGENTS.md`):

- Windows program check: "Prepare my Windows computer for video work. Check what is installed and install only what is missing with winget: Git for Windows (tell me to restart the editor afterwards), Node.js LTS, ffmpeg, Python 3. If Windows asks permission I will click Yes. At the end show a table: program, version, ok or what to do."
- Mac program check: same idea with Homebrew (if missing, give me one command to paste into the terminal where I type my password), Node.js, ffmpeg, Xcode Command Line Tools (they include Python 3).
- Free Higgsfield check: "Check the Higgsfield connection: show my credit balance and find the video model I plan to use, with its durations, formats and accepted references. Generate nothing."
- First agent test: "Read all files in this folder. Write a 2-3 sentence summary for each. Collect everything into summary.md with a table of contents." The agent installs in the terminal with the vendor's install command; `/clear` clears the context between unrelated tasks.

## Formulas

Prompt for building a model skill (principle 62):

```
Find the official instructions for writing prompts for <model>, and read forums and guides for best practices.
Write a SKILL for the agent on writing prompts for this model. Every prompt follows this formula:
1. Subject: who or what is in frame.
2. Location: where it happens, as exact as possible.
3. Action: what the subject does now (pose, gaze, movement).
4. Angle and camera: from where and how it is filmed.
5. Light: where it comes from, shadows, contrast. This is critical.
6. Effects and style: film, grain, color grade, genre.
Include the model's character limit and recommended length. Count characters before output.
```

Example of a request that needs the user's "ok" (adapt names to your video):

```
Generate the video in Higgsfield with seedance_2_5, omni reference, 30 s, 4:3, with sound. First a 480p draft in draft mode so it can be finished at full resolution later. Take the previz, images and prompt from the project folder, and the upload order from prompts.md.
Show settings, the estimate_video_cost result and the stage checklist first. Run it only after my yes. Save as seedance_v1_draft.mp4 and show frames as a contact sheet next to the previz.
```

Project instruction in five parts (principle 35):

```
Role: you are the producer of my short videos.
Context: we make vertical videos for <platform> for <audience>.
Style: short sentences, plain words, no filler.
Rules: nothing paid runs without my explicit yes; every correction I give goes into AGENTS.md with a date.
Format: after each stage, a summary of at most 5 lines and the question "continue?".
```

Table "Without an agent / with an agent":

| Thing | Without an agent | With an agent |
|---|---|---|
| Prompts | Lost in a chat | All in `prompts.md`, only the current version |
| Starting a generation | Paste prompt, upload references, set options | Say "references and prompt approved", check the price, say yes |
| Result | Download, rename, sort | Saved by the agent under a meaningful name and logged in `progress.md` |
| Rejects | Deleted or lost | Moved to drafts, still available |
| Voice | Generate apart and put under the video by hand | The agent makes the voice and places it in the video |

Chat or agent:

| Plain chat | Agent |
|---|---|
| Answers a question | Does a task |
| One step at a time | A chain of steps on its own |
| You steer every step | You set the goal, it acts |
| Does not touch files | Reads, creates, edits files |
| Forgets context | Remembers within the task |

Task to model type (principle 68). Pick current model ids with `models_explore`:

| Task | Use |
|---|---|
| Idea, script, hook | stage 00 and `templates/idea-toolkit.md` |
| Storyboard, angles, camera | stages 01-02, `templates/script-and-storyboard.md`, `templates/film-language.md` |
| Characters, references | stage 03, `templates/characters-and-refs.md` |
| Frames | stage 04, image model `nano_banana_pro` |
| Previz in Blender | stage 05, `.claude/skills/blender-previz/SKILL.md` |
| Video prompts | stage 06, `seedance_2_5` first |
| Voice, music | stage 07, `elevenlabs_v4`, `elevenlabs_music_v2_5` |
| Edit, sound, delivery | stage 08, `templates/montage.md` |

## Check before "ok"

The studio is ready only with the user's "ok".

Studio:
- [ ] The editor is installed and the studio folder is open and trusted
- [ ] The agent is installed from the official source and signed in
- [ ] ffmpeg, Node.js and Python are installed (table is green)
- [ ] The model and effort are chosen
- [ ] Higgsfield is connected and the balance is visible
- [ ] Any extra keys are in `.env` and nowhere else
- [ ] `AGENTS.md` exists, the "Who I am" answers are in it, folders exist

Project:
- [ ] The folder `projects/<NN-word>/` was made from `templates/project-folder.md`; the name has no date; the agent session is new
- [ ] The task is filled in and the frame format is stated before the first generation
- [ ] Project rules are in `AGENTS.md`; for a brand there is a brand file and prompts name the brand
- [ ] All prompts are in one `prompts.md`; old versions did not spawn extra files
- [ ] Before every paid run the user saw the model, mode, format, duration, resolution, sound, files and roles, the credit estimate, the prompt and the checklist, and gave a "yes" for that exact run
- [ ] No storyboard frames were fed to the video model (only reference cards)
- [ ] Reference numbers in the prompt match the upload order
- [ ] A draft or a 4-5 second test came before the finish
- [ ] No version overwrote an older one; rejects are in drafts
- [ ] `progress.md` is current after the last generation
- [ ] Keys are only in `.env` and never appeared in chat
- [ ] Experience notes are written with dates
- [ ] Video was checked with a contact sheet; sound by loudness and spectrogram; the report honestly says "not checked by ear"
- [ ] Delivery: mp4 H.264 yuv420p CRF 22 faststart, sound at about -14 LUFS; version `_vN`

## Common mistakes

- Running the whole project in a plain chat: prompts sink, and with 40 of them the old one cannot be found.
- Moving every prompt by hand into Higgsfield: files pile up with unclear names, and one video takes hours.
- Deleting rejects or losing them among files.
- Installing a look-alike plugin; installing programs by hand instead of using the setup request.
- Pasting keys into chat, or posting and sending the `.env` file.
- Running a free plan and expecting it to cover long agent work.
- A long chat: it costs more with every message. Not clearing context between unrelated tasks lets the old context disturb the new one.
- Starting the agent from the wrong folder; a vague task ("help me with the project"); panicking when the agent asks permission (read what it wants and confirm if right); expecting an instant result on a hard task.
- Asking for a prompt without a skill: averaged and generic. Explaining the same thing again every time. Writing long prompts by hand.
- Not telling the agent what is going on in the assembly: a prompt in a vacuum.
- Patching an old prompt instead of rewriting it with the new reference.
- Mixing up the reference order at upload relative to the numbers in the prompt.
- A generic negative ("extra fingers") instead of one specific to the scene.
- Feeding storyboard frames to the video model.
- Reorganizing files without asking after the user moved them.
- Treating an audio cleaner's result as checked without checking the file (jingle at the start, signature at the end).
- Not fixing the frame format before the first generation.
- Trying to write the perfect instruction at once. Using a plain chat with no project: no memory between sessions.
- Vague words like "dynamic shot".
- Connecting a skill or plugin without reading its files.
- Calling a generation "done" without checking the file itself.
- Agent enters terminal commands, but the user types the admin password; after installing Git on Windows, restart the editor.

## Tools

| Tool | Role in this stage | Notes |
|---|---|---|
| Code editor with a terminal | work window: files on the left, the agent in the center, the open `prompts.md` on the right | free |
| Coding agent (Claude Code or another that reads `AGENTS.md`) | writes scripts and prompts, runs generations, sorts files, edits, checks | paid plan; usage window of a few hours, so save limits |
| Higgsfield MCP (`https://mcp.higgsfield.ai/mcp`) | images, video, audio and upscale from the agent; upload of references (`media_upload`); balance and model list (`models_explore`) | subscription with credits; `estimate_*_cost` before any paid run |
| Voice dictation app | speaking tasks and corrections instead of typing | optional |
| ffmpeg, Node.js, Python 3, Git | programs the agent runs; the agent installs them on request | winget on Windows, Homebrew on Mac |
| Blender | previz (stage 05) | optional, free |
| `scripts/check_prompt.py` | checks a prompt against the rules before a paid run | local |
| Skills in `.claude/skills/` | one skill per job or model | keep current; read third-party skills before use |
| Contact sheet (ffmpeg) | frame grid for checking video | local, free |
