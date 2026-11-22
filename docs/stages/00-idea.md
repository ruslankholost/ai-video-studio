# 00 Idea and concept

Half of a video's result is decided before the first generation. A model draws the picture and does exactly what the prompt says. It does not supply meaning, story or taste. The person supplies those. This stage answers three questions before any script or generation: what is the video about, who is it for, and why will they watch to the end.

No paid generation happens in this stage. Nothing is generated until the user says "ok" on the idea.

## Input and output

Input (should be in the project folder before the stage starts):
- `brief.md`: what we make, for whom, platform, frame format, duration, deadline, credit budget. If it does not exist, step 1 of the workflow builds it.
- `refs/`: reference videos the user or the client likes.
- For a client project: who pays for generations, the prepayment, the number of revisions (see 00.55). Skip for the user's own project.

Output:
- `brief.md`: the filled brief card (template in `templates/idea-toolkit.md`).
- `idea.md`: a one-sentence logline (who, what they want, what stops them); a one-sentence retelling of the video; the "strange thing" or mechanic; 2-3 hook variants; the decision "series or single video"; limits (duration, frame format, number of shots, number of generations); a list of assumptions the client did not confirm; a list of what only a human can decide (group D below); rejected ideas with the reason.
- `refs/` extended with a reference that shows what exactly we repeat (structure and devices, never another brand).
- The user's "ok" on the idea. Without it the stage is not closed.

File names follow the studio convention: `brief.md`, `idea.md`, `script.md`, `moodboard.md`, `storyboard.md`.

## Principles

### A. Meaning before picture

00.01. The idea is invented before generation and written in one sentence. Everybody can generate now: one prompt, one model, a finished video. Most work has a good picture and no story. What sets a creator apart is the meaning they build in. Before generating, check: "I can state the meaning of the video in one sentence."

00.02. Do not generate at random. "A cool picture, I will animate it" is not an idea. The result is a set of pretty frames with no meaning. Story and storyboard come first, generation after.

00.03. The first stage weighs about half. The next two stages (production, post) do not fix its mistakes, they enlarge them. A re-roll cures a prompt error. It does not cure a script error. A video can gain emotion later, but its meaning is set at the start. Approximate weights: 50% idea and preproduction, 25% generation, 25% post.

00.04. Do not start from the middle. The typical beginner failure: "I will sit down and make it!", a few unrelated clips, "this is junk", project dropped. The order that saves the project is preproduction, production, post. A creator who used to start from the middle and bail after two or three bad clips, then switched to this order, finished.

00.05. Most time goes into the story forming in your head, not into generations. In one large story project, preparation took about 14 days and clean generation about 4. Every detail found in preparation saved dozens of generations.

00.06. If you do not like a scene and cannot say why, show it to someone with a fresh eye (a director, a creator community). A fresh look saves credits.

00.07. Value moves to idea, script and taste. Many people will work with AI, few will work with quality. The agent can write the script and the prompts, but the idea must be the user's. Content made for the creator's ego (dragons, cartoons with no meaning) is not what a client buys.

00.08. The idea goes into a logline: who, what they want, what stops them. Everything else is built under it. One sentence.

00.09. Fix the limits at once: duration, frame format, number of shots. Ask the frame format before the first generation: a format change means all generations again.

00.10. Check the idea for generatability: what the model will carry and what it will break. Count the production at the same time: how many generations, is a recurring character needed, does it fit the duration. For a short punchy video, 3-6 generations and 15-30 s is the guideline. The agent counts for itself. The user hears the credit figure only before a paid step.

00.11. One idea per video, retellable in one sentence. Not "beautiful product shots" but a mechanic: "the whole world is black and white, only the product has color", "one continuous shot with no cuts". Idea check: you can retell it to a friend in one sentence.

### B. Idea method: assembly, volume, hard selection

00.12. A good idea is not a flash of insight. It is assembly from proven patterns, plus large volume, plus hard selection. A published study of advertising ideas (Goldenberg, Mazursky, Solomon, 1999) found that most of the best ads fit six templates, and satirical sites publish a few percent of the headlines they write. We did not verify those figures. Repeat the mechanic: many variants, blind selection, polish the best.

00.13. Start with the brief, not with ideas. Without a brief the ideas come out generic. Ask at most 3-4 questions at a time and never re-ask what is already known. Find out: product, audience (what they live with, fear, do not believe), the one action after the video, the main thought in one sentence, the "uncomfortable truth", where the brand sits in the finale, limits (duration, platform, tone, taboos, generation budget), references. If the client is in a hurry: minimum is product, audience, platform. List the rest as assumptions.

00.14. The "uncomfortable truth" of a product, or a pain everybody in the category knows, is the best fuel for humor and recognition. Example: "everyone is tired of fake gurus".

00.15. Before generating ideas, collect raw material: 15-30 pains and phrases of the audience; 20-40 idioms and verbs around the topic (so you can show them literally); 15-20 recognizable genres to parody. Ask the product questions: is there an idea in the name, the packaging, the product's story, what happens with the product and without it. An idea is a new combination of old elements. Add local memes and niche slang from the user.

00.16. People first, then the model. Ask the owner or team to write 10-20 one-line ideas in 15-30 minutes, then bring in the agent. Model ideas are uniform; people without an anchor give more spread (Doshi and Hauser, 2024). Put the human ideas into the common pool without author tags. If the person does not want to, go on.

00.17. Volume: 8-12 directions (template x genre), 5-10 premises each, 60-120 per pass. Premise format: one or two lines of setup, a final beat with the brand, the device in brackets. "Do not repeat a mechanic. If two ideas are about the same thing, keep the stronger." Row template is in `templates/idea-toolkit.md`.

00.18. The idea formula has four details: (1) a recognizable scene that reads in one second without sound; (2) one strange thing; (3) escalation, at least three beats; (4) the brand in the punchline. Control: "If you cut the brand, the joke breaks." A worked reference example is in `templates/idea-toolkit.md`.

00.19. One strange thing per video. Two ideas in one video cancel each other. The absurd grows out of a recognizable everyday situation: "ordinary against unexpected" is funnier than "ordinary against impossible".

00.20. The violation must be harmless: nobody suffers seriously, no audience trauma is touched. Parody genres, not specific people. Do not use real logos of other brands without the client's consent. Humor works when something is both a violation of a norm and safe. Two checks: "Where is the violation?" (none: the video is boring) and "What makes it harmless?" (nothing: the humor hurts the brand).

00.21. Selection is hard and blind. First kill 70-80% yourself: is it clear without sound, is the strange thing in the first 3 seconds, is the brand in the punch. Show the remaining 15-25 as a numbered list with no comments or labels, so you do not sell ideas with your tone. With a team: ideas are read without authors by one person in a monotone, everyone votes yes/no, an idea passes with more than half.

00.22. Polish 3-7 ideas as a "scene game": base, strange thing, at least three escalation beats (each stronger), a brand punch, 2-3 mutations with SCAMPER. Reread the next day.

00.23. Pass mark: 8 of 10 on the "funny and clear in 3 seconds" checklist. For a failed idea, make one fix, not a rewrite. The 10-point list is in `templates/idea-toolkit.md`.

00.24. Test on live people before production: show an animatic or storyboard to 5-10 people from the target audience with no explanation. Ask "retell what happened" and "where did you laugh". If they cannot retell it, the idea is unclear. The viewer is not stupid.

00.25. Keep several ideas, 1-3 finalists, and 2-3 hook variants for testing. After release, measure retention at second 3, completions, reposts and saves, and write down which templates worked.

00.26. Analyze somebody else's successful idea instead of inventing from zero. "Analyze a video" mode: split it into scene, strange thing, escalation, punch, name the template, then give 5 variants of the same mechanic for your product. To start: find an ad you like, build a moodboard, break it into a storyboard. Do not strain a concept out of your head: take what already worked and adapt it for your client.

00.27. A reference is structure, not someone else's brand. Take structure, pace and devices. Do not carry the original's logos, texts, characters or music into client work.

00.28. First find the format that resonates with the audience, then repeat it. Repeating 30 times something that catches nobody gives nothing. For a content factory, idea beats polish: no wow quality is needed, only an idea that grabs in a second. A "20 hooks" request using the formula "problem, unexpected solution, product at work, reaction" is in `templates/hooks.md`.

00.29. Look at real ads, do not invent in a vacuum. Use the Meta Ad Library and TikTok Creative Center for spec ads; make a spec ad for a real brand in 3 hook versions.

00.30. Every promise in the video rests on real data. Claims (income, results) must rely on the user's real cases, or the video becomes the thing it mocks. With no cases, use only symbols and honest facts (views, clients). Do not invent facts: numbers, reviews, clients, "ready in 2 minutes".

### C. Hook and the cold viewer

00.31. The viewer decides "watch or scroll" in half a second, one second at most. Give all the juice in that second: it must be clear at once what the video is about and why to watch to the end. Mistake example: the first 4 seconds show a title card, and the viewer thinks the phone froze. Starting at once with a child asking a question is stronger.

00.32. The hook is worded at the idea stage, not after editing. Prepare 2-3 variants of the first seconds for testing. The hook is the first hit after which the viewer thinks "what?? I have to watch to the end". Timing of the hook differs across sources (3 s, 1-2 s, 1.5 s, half a second). Rule: take the strictest and latest norm. The idea must be clear from the first frame without sound, and the details unfold by second 3.

00.33. The idea must read without sound. Subtitles are mandatory, many people watch muted. Idea check 1: without sound and text, one second shows where we are and what genre it is. The first 3 seconds must catch visually even without sound.

00.34. In the first 3 seconds there is already a strange thing, not a lead-in. Enter a recognizable scene (a birth, a wedding, a court, the news, a nature documentary, mom's kitchen) instead of explaining the world.

00.35. An idea that is not visible on screen does not work. "If the idea does not read from the screen, you lack frames that explain it." A caption does not replace a shot. A caption is for what you could not show. Example: a luxury watch with no explanatory text under the video is unclear.

00.36. In a good story the hero struggles and there is a turn at the end. If everything is told in the first seconds, there is nothing to worry about. Example: an ad in sports-brand style opened with a child shouting "mom", so the viewer knew everything. It is stronger to show the heroine fighting herself and reveal in the resolution that she is a mother. You advertise the struggle, not the product. Resolved conflict: do not reveal the turn in the first seconds, the hero struggles and the turn comes at the end. A first frame may hint at the situation as a riddle, but never gives the resolution.

00.37. Something must change in the video: "without glasses" becomes "with glasses". Story check: what changes from start to end.

00.38. Emotion must be close and concrete. We start to care only when we see a person's emotion. Far future and nuclear war are not felt, as a number like ten trillion is not felt. Loss is one of the strongest feelings. Landscapes with no human emotion are a mistake.

00.39. The viewer must recognize themselves: "this is about me", not "this is an ad". For a series, the topic must let the viewer recognize themselves within 3 seconds.

00.40. Hit the audience's pain, not the product. For a story cartoon: "The hook is about relationships, not about the product". The product appears only in the middle as the hero's path. The tag the offender gives equals the audience's pain and returns as a mirror in the finale. Skeleton and hook bank are in `templates/idea-toolkit.md`.

00.41. A concrete audience of a city, people or region takes the hook and has almost no competitors. Example: a real-estate video opens with a panorama of the city and its name. Narrow audience: content for a specific people or region has little competition and grows easier. The downside: a local story tied to a local date means nothing to a foreign viewer, so an English version needs a different idea.

00.42. Advertising: show, do not call. A coffee shop sells atmosphere, not beans. Phrases like "we are waiting for you, come in" work against you: they say there are no customers. People go where people already are (social proof). Exception: brand-awareness videos on transit screens need no plot, the person has 2 seconds.

00.43. The product follows from the story, it is not a separate inserted shot. Examples: a lemonade as a bonus for victory (like a coin in a platform game), the heroine is handed a drink and wins; a heroine calmly eats a sweet, thugs bother her, she deals with them and returns to the sweet.

00.44. The contrast of heroes must read in seconds, especially in vertical 60-90 s: "strong contrast between the heroines, so the viewer knows within seconds who is who". Example: a tidy schoolgirl with a headband against a heroine in a dark grunge look.

00.45. Short entry. A story project dropped the wide establishing shot of the school: "too long for social media". The idea must not require a long setup before the first event.

00.46. Plot and intrigue matter more than visual perfection. "The main thing is idea and plot, number one" (about micro-dramas). The visual is often average, but the viewer finishes for the hook. Do not delay release chasing photorealism.

00.47. The character's gaze is part of the idea, not a prompt detail. Models by default draw the character looking at the camera, and the video "gives itself away". Looking at the camera is justified only when the hero talks to the viewer, or as a single look in the finale. For expensive products the model looks down with a challenge. Continued in stage 01.

### D. Series or single video

00.48. The decision "series or single video" is made at the idea stage and written in `idea.md`. Theory from one creator guide, not verified by us: people subscribe to a series, not a single video. It needs recurring characters, a topic the viewer recognizes in 3 seconds, and a hook at the end of each episode. Method: 60-120 ideas from proven devices, blind selection, a season synopsis of 10 episodes. Counter-position: an author profile where every video is its own idea and one recognizable look and one emotional territory unite them (opening card with the name of a feeling in the first second, 40-60 s, a cut every 1-2 s, a repeat or twist in the last 3 s, caption with a question to the audience). This is a taste choice and it is the user's. Ask which they want and record it. Default for client work: propose a series (see 00.49). Default for the user's own profile: ask. (default; the user may change it)

00.49. Sell a series to a client, not one video. The client's goal is followers, one video will not get them, the client pays for a month, not for a clip, and a one-off video "for fun" costs about 5 times more. Choose the format for the client's single goal.

00.50. A micro-series as a test: a pilot of 3 episodes of 60 seconds in one genre, posted to Reels and Shorts, watch completion. For cartoons: invent a mascot and make 3 short videos with it. One style and one character across all videos.

00.51. A series stands on classical dramaturgy, not on tools: hero's path, obstacles, character arc, setup, climax, resolution. A series script can be in a plain text format with scenes, dialogue and character description.

00.52. A story cartoon of 40-120 s uses the skeleton "hit, bottom, mentor, path, caption, meeting, mirror and "How?", call to action". 60 seconds is 2-3 generations of 20-30 s, 3-4 recurring characters, 4-6 locations. "Shoot success like a series, not like an ad." This is a format people finish for the plot, and the product is the way the hero got out of the bottom.

00.53. If the project is first and big, take one scene or one format, not everything at once. Climb the whole ladder once, and the rest goes along the beaten path. For the idea this means: make a pilot first.

### E. What the human supplies (what the model cannot)

00.54. Meaning, story, emotion and logic come from the human. "The network draws frames, you supply story, emotion and logic." Taste too: an agent cannot replace eyes and taste, but it takes over all manual work.

00.55. For a client project, money and terms come before the idea. First discuss the idea and script, then a quote for the project. The client pays for generations. Prepayment is agreed in writing (sources range from 50% to 100%; ask the user, a decision for the first client). The contract sets the number of revisions and the stage. Extra revisions are paid separately. With a very small budget, say honestly that it buys a couple of generations and the author does not answer for the result. Replacing a hero from scratch is normal: "everyone redoes things".

00.56. Search costs money: put time and credits for search and redo into the quote. In one large story project, about 22 s of generated video went into each 1 s of the final cut (223 video runs, about 2000 s generated for 90 s of final). The opening scene was generated four times, no variant made it, and a different heroine had to be found.

00.57. Three whales: fast, good, cheap. Choose two. The human picks which two before starting.

00.58. A client and a brief reduce redoing but do not cancel it. A good brief reduces rework, and a hero change after approval is possible and must be covered in the contract.

00.59. A creator either knows how or knows where to ask. Understand the neighboring professions (camera, light, sound, editing direction) at least for the terms.

00.60. The human decides the mode of work. The "director" sets the task, looks at the result, corrects and says "ok". The agent does, checks and shows. An idea counts as accepted only after the user's "ok".

00.61. Idea, script and taste go into the studio's memory. Record rejected ideas and the reasons in `idea.md` so you do not return to them. Every "do not do that" remark goes into the project notes (see stage 09).

### F. Packaging the idea for the person and the market (where it is part of the idea)

00.62. Serve the idea "in your own sauce". From the start think of yourself not as a contractor but as an author who presents each unit of content in their own way. If imagination runs short, ask the agent for creative ideas. A carousel post with an unusual presentation stands out.

00.63. A profile that is only a catalog of work does not bring clients: it needs a face, services, a path, cases. Service quality should be at least 3 of 5 so clients come. For video ideas this means a portfolio idea should show the path, not only the result: "describe the path, not only the result".

00.64. One-line offer: "I make [product] for [niche], so that [result]." Good: "AI photo shoots for cosmetologists, so they can run a blog without filming". Bad: "I make neural networks, photo and video for everyone". A narrow niche pays: a niche does not limit, it focuses.

00.65. Start with what you already know. "Do not invent a new road. Strengthen the one you already walk." Take a field where you spent a year or two, list clients' common pain, close it with AI visuals.

00.66. Do not wait for an order: find a company that is about to launch, make a video in advance and send it. Worst case, one more portfolio piece. Best case, a first client. Videos for tiny projects with no money waste time, so choose the niche by research.

00.67. An idea can be an idea of publication: a challenge or a recurring rubric turns a series of spec videos into a story (for example, "making ads for brands in AI until I get my first order, day N"). It also works as a pitch to brands. The course does not claim this, it is observed in the field.

## Workflow

After each step, show the result and ask "go on?".

1. Brief. At most 3-4 questions at a time. Output: the brief card, which the user confirms or corrects. Template: `templates/idea-toolkit.md`. File: `brief.md`.
2. Frame format, platform and duration. Ask before any generation.
3. References and "what already works" (analyze-a-video mode; Meta Ad Library, TikTok Creative Center). Output: `refs/`.
4. Raw material: pains, idioms, genres, product questions.
5. Human pass: 10-20 one-line ideas in 15-30 minutes from the user. Ask for it, then continue.
6. Generate 60-120 premises on a "template x genre" matrix. Six templates, eleven filters, device cheat sheet, genre bank, SCAMPER: `templates/idea-toolkit.md`.
7. Pre-selection (kill 70-80%), then blind vote on 15-25 ideas. The user votes on the numbered list, with no labels from you.
8. Polish 3-7 ideas: base, strange thing, beats, punch, mutations.
9. Run the 10-point checklist, 8 or more to pass. For a story cartoon add the 9-point group (`templates/idea-toolkit.md`).
10. Decide: series or single. For a series write the season's episode list and the hook at the end of each.
11. Write the logline, the limits and the generatability check, and 2-3 hook variants. File: `idea.md`.
12. If there is time, test on 5-10 people from the audience (a storyboard or animatic comes from stage 01).
13. Show the user 1-3 finalists. The user says "ok". Then stage 01.

Modes: full; quick (mini-brief of 2-3 questions, 15-20 labeled ideas, top 3 with short storyboards); polish the user's own idea; story cartoon; analyze someone else's video. Choose the format first: for a short 15-30 s punch put the brand in the punchline, for a 40-120 s story cartoon the hook is about relationships and the product is not at the center.

## Formulas

Offer line:

```
I make [product] for [niche], so that [result].
```

Idea formula (4 details): 1) a recognizable scene (base reality); 2) one strange thing; 3) escalation, at least three beats of increasing strength ("if that is true, what else is true?"); 4) the brand in the punchline.

Logline: "who, what they want, what stops them", plus limits (duration, format, number of shots) and a generatability check.

Nine hook formulas for a scriptwriter prompt: experiment, life hack, insider, pain to solution, myth, from scratch, income, secret, counter-position. Eight video types: "wow result", "repeat after me", "before/after", "myth buster", "behind the scenes", "pain to solution", "trend plus topic", "provocation". Texts are in `templates/hooks.md` and `templates/script-and-storyboard.md`.

Long forms (brief card, premise row, checklist, six templates, eleven filters, genre bank, SCAMPER, story-cartoon skeleton, examples) are in `templates/idea-toolkit.md`.

## Check before "ok"

- [ ] The brief is filled. Assumptions the client did not confirm are listed.
- [ ] The idea retells in one sentence. A logline exists (who, what they want, what stops them).
- [ ] In the first second it is clear where we are and what the video is about. It reads without sound. Subtitles are planned wherever there is speech.
- [ ] In the first 3 seconds there is a strange thing or a hit, not a lead-in. There are 2-3 hook variants.
- [ ] The story has a struggle, a turn and a change from start to end. The turn is not revealed at the start.
- [ ] One strange thing. It is harmless. The brand or product follows from the story (the punch).
- [ ] The emotion is close and concrete. People's emotions are visible, not only landscapes.
- [ ] The idea checklist passed at 8 or more out of 10.
- [ ] All numbers, reviews and promises are real and have a source. No invented ones.
- [ ] No other brands' logos, characters or music (the reference was taken as structure).
- [ ] The decision series or single is made and written in `idea.md`.
- [ ] Production is counted: number of generations, recurring characters, duration.
- [ ] For a client project: who pays for generations, the prepayment and the number of revisions are agreed.
- [ ] 1-3 finalists were shown without "selling" comments.

The stage closes only on the user's "ok".

## Common mistakes

- A good picture and no story. Showing off the network, not the creator. An overused idea.
- No plot and no storyboard: a set of beautiful frames with no meaning.
- The product is not connected to the story.
- A weak hook: an ad for glasses that opens with a case opening is too little for Instagram.
- A weak start: everything told in the first two seconds, no struggle and no resolution; no subtitles; only landscapes; a far-off topic; frames out of style.
- Advertising a venue without showing it; "we are waiting for you, come in".
- Taking big ideas "from the middle"; quitting after 2-3 failed generations.
- Not budgeting search and redo; a tiny budget with no warning to the client; a contract with no revisions written in.
- Straining out a "unique" concept instead of adapting what worked.
- In a story cartoon: an idea about the product instead of the relationship; the hero gloating; success shown "like an ad" (slow motion, rain of banknotes).
- Two strange things in one video; pure fantasy with no everyday base; a violation with real victims; real logos without consent; invented income figures; comments and labels when showing the shortlist.
- Automatic praise of the user's idea. Say by the checklist why it is weak and how to strengthen it.
- Judging level by years or number of courses; "wow quality" instead of an idea; ten outreach messages with no reply is "not yet an attempt".
- A catalog profile "look what I can do", faceless; blaming low reach on the algorithm instead of the content.

## Tools

| Tool | Role in this stage |
|---|---|
| The agent (Claude Code or similar) | brief, raw material, premise pool, polish, checklist |
| Meta Ad Library, TikTok Creative Center | look at real ads for spec ideas (free) |
| Pinterest and film-frame libraries | references and moodboard (the main work is in stage 01) |
| A voice dictation app | optional: dictate scripts, prompts and notes |
| Higgsfield and any paid generator | not needed here: no paid generation before the user's "ok" on the idea |

Tools change, the roles stay: find what works, write many variants, select blind, check with the checklist.
