# Client documents

Fill-in prompts for selling AI video work: an offer, a first message, a brief, a one-page proposal, deal terms, a list of niches that pay, and a brand brief for a fashion shoot. All are text prompts for a chat model. The agent fills the brackets from what the user tells it and never invents numbers, reviews or names.

Used at stage 11 (`docs/stages/11-business-and-clients.md`). The offer formula and a batch-of-hooks prompt are also in `templates/hooks.md`. Project folder layout for client work is in `templates/project-folder.md`.

## Rules

- Write simple language, no legal fog. Leave bracket fields wherever the client's own data goes.
- Numbers from a model with no source are not used. Ask the model for a source next to every figure, and open them.
- No fake case studies, no made-up client names, no fake reviews. If the user has no results yet, say that in the proposal and offer a small paid test.
- The user approves every document before it is sent to anyone.

## Offer formula

```
I make [product] for [niche], so that [result].
```

Good: "AI photo shoots for beauty therapists, so that they can run a blog with no filming." Bad: "I make neural networks, photos and videos for everyone."

Another example: "Product videos for small bakeries, so that every new item gets a video on the day it is baked."

## Prompt: offer and first message to a client

```
Help me write the offer of an AI video creator using the formula:
"I make [product] for [niche], so that [result]."

My direction: [for example, AI ads for products]
Niche: [for example, skin-care brands]
What I can already do: [image generation, video, editing, etc.]

Give 5 offer variants. For each:
1. Which main client pain it closes.
2. What result the client gets in numbers (reach, leads, savings on shooting). Mark every
   number as an assumption unless a source is given.
3. A first message to such a client in 3-4 sentences. No "Hello, I am an AI creator".
   A concrete idea for their business instead.
```

## Cold message rule

There is no template text. Do this instead: open the business's account, see their weak spot and their reach, think how a video could help, generate one frame or a short video in the brand's look, and send it with the idea so the person sees the benefit at once.

Bad: "Hello, I am Anna, an AI creator, here are my works." Good: a message that names something specific in their account, shows one frame, and asks one question.

## Message to people you know

Write personally, by name, never copy-paste to a list. A shape that works when starting out and building a portfolio:

```
Hi [name], how are you? Remember we talked [when]? I am learning to make [photos / short
videos] with AI and need practice. It takes 5 minutes of your time. Here are 3 examples.
Want the same, but with you / your product?
```

## Prompt: brief, proposal and deal terms

```
I am an AI video creator. Direction: [for example, a content factory for cafes].
My packages: [names, what is included, price].

Make three templates:
1. A brief: 10-15 questions to ask the client before starting: goal, audience, what may and
   may not be shown, examples, deadlines.
2. A one-page proposal: offer, what each package includes, deadlines, the result for the client.
3. Deal terms for a contract: estimate, [prepayment %], number of revisions, deadlines,
   content rights.

Write in plain language. Leave fields in square brackets wherever client data goes.
```

The user sets the prepayment share, revision count and rights. The agent suggests clear defaults and flags that the user should have a contract checked by a local professional before signing a real deal.

## Prompt: niches that pay

```
Analyze which tech and SaaS niches spend the most on motion advertising, using current spend
data and 5-year forecasts (for example fitness apps, AI automation). Market: [region].
Give a top 7 as a table: niche, who orders, typical budget per video, where to look for
clients, 2-3 companies that are launching soon. A source link for every number.
```

Use only numbers that come with a source you opened. Before contacting a company found this way, check that the facts about its launch are real.

## Prompt: find companies before a launch

```
Find 10 products in the niche [niche] that launch in the next 2-4 weeks: name, site, launch date,
founder and their public contacts. As a table. Mark the 3 that need a launch video most and
explain why.
```

## Brand brief for a fashion shoot

Use when a brand asks for a creative fashion shoot of a product (images or video).

Task statement: develop and carry out a creative fashion shoot that:

- shows the product's unique features and quality;
- creates an emotional link with the target audience;
- stands out visually and is memorable;
- matches the brand positioning ([premium / luxury / other]).

Steps:

1. Analyze the product: features, strengths, target audience, brand positioning.
2. Develop the concept: a unique idea, unusual models, locations or stories.
3. Choose visual elements: shoot style, location, model or character, accessories, color palette.
4. Technical plan: frame composition, angles, light, camera approach (see `templates/film-language.md`).
5. Build a series: main shots (full look, details, lifestyle).

Expected result: a series of professional fashion images for ad campaigns, social media and the brand's site.

Example fill, for a small leather-goods brand: positioning "quiet luxury, craftsmanship", concept "the bag as an heirloom passed across three generations", palette "oxblood, cream, brass", series "full look on the street, stitching close-up, the bag on a workshop bench".
