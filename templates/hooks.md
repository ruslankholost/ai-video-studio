# Hooks and offer

Short fill-in prompts for producing many hooks for a "content factory" (one template, many videos for one product), and a one-line offer formula. A hook is the first 3 seconds of a video: what is seen, the first phrase or caption, and the emotion the video ends on.

Used at stage 00 (`docs/stages/00-idea.md`) when the user needs a batch of ideas for one product, and at stage 11 (`docs/stages/11-business-and-clients.md`) when the user sells video work. Script-level hook formulas are in `templates/script-and-storyboard.md`. Humor templates and the relationship-hook bank for story cartoons are in `templates/idea-toolkit.md`.

## Offer formula

```
I make [product] for [niche], so that [result].
```

Good: "AI photo shoots for beauty therapists, so that they can run a blog with no filming."
Bad: "I make neural networks, photos and videos for everyone."

The test: a stranger can say who it is for and what they get after one reading. A second example: "Short product videos for ceramics shops, so that each new piece gets a video the day it is made."

## Viral video formula for a content factory

Every video follows four beats. One formula gives hundreds of videos for different products.

1. Problem: a familiar situation from the first second, the viewer recognizes themselves.
2. Idea: an unexpected solution.
3. Product in action: the product solves the problem on screen.
4. Reaction: an emotion worth sharing.

## Prompt: 20 hooks for a content factory

Paste into a chat model after filling the brackets. The video must be makeable by generation from a single template, so ask for no complex shooting.

```
You write short vertical videos for a content factory.

Product: [name, what it does, price range]
Who buys: [audience, their main pain]
Where we publish: Reels, Shorts, TikTok

Write 20 hooks for videos using the formula: problem, unexpected solution, product in action, reaction.
For each hook give:
1. What is seen in the first 3 seconds.
2. The first phrase or the on-screen caption.
3. How the video ends (the viewer's emotion).

The hooks must not repeat each other. No complex shooting: everything must be makeable by
generation from one template.
```

Example of one output row, for a ceramic mug shop:

1. Seen: a hand drops a mug on a tile floor, the camera is low and the mug does not break. Caption: "I dropped it on purpose." Ending: relief and a smile, the mug rolls to a stop, close-up of the glaze.

## Choosing and testing hooks

1. Throw out hooks that need a spoken explanation to be understood. A hook must read with no sound.
2. Keep the 3-5 most different hooks, not the 3-5 best-worded ones.
3. Test each hook against the first two points of the 10-point check in `templates/idea-toolkit.md`: it is clear where we are in one second, and a strange or recognizable thing is on screen within 3 seconds.
4. For one chosen idea, write 3 first-3-seconds variants (A, B, C) and run only the cheapest draft of each. Do not render full videos for all variants.
5. A hook must not promise something the video does not deliver. If the video cannot deliver, change the hook, not the claim.

## Prompt: offer and first message

See `templates/client-docs.md` for the version used when approaching a client.
