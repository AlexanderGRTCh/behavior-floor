# docs.md — Authored Documents
_Guides, reports, briefs, any file written for a human reader. CORE invariants apply; condensed first draft is non-negotiable (a "make it shorter" follow-up means the first pass failed)._

## Plain guide ("for anyone" overview), validated skeleton
1. The simple goal (one paragraph, no jargon).
2. The obvious question (the naive "why not just use one LLM call" framing).
3. Three concrete failures of the naive approach, with a single running worked example introduced here.
4. N short layer paragraphs, two sentences each: what the layer does, why it had to exist. Same micro-template so the reader can skim.
5. "Why this took real work" closing: restate the naive baseline, enumerate the gaps each layer closes, concede no layer is novel alone, argue they stack.
6. "What you get" as a short bullet list of concrete artefacts.

Voice: 700 to 900 words for a 1.5 to 2 page doc; sentences 12 to 18 words; active voice; concrete examples over abstract claims; every technical term defined on first use or removed; no marketing language; zero dashes.

## System-work explainer (trigger: "system-brief style")
For explaining a shipped system change OR a whole system ("full map") to the primary user in plain register. Fixed section order (for a full-map doc, swap steps 3 to 6 for: The goal / What happens when you start / The parts in plain words / Why this beats the naive approach, keeping the same voice):
1. Title = the outcome in plain words, not the component ("Making the Writing Rules Stick"); subtitle = what + date + why in one line.
2. "What this is about" — anchor to the lived event that motivated the work (the thing the reader saw or felt).
3. "The problem" — the mechanism in plain words, no jargon.
4. "What we checked before changing anything" — evidence first: audits run, verdict line, then finding bullets.
5. "What we built" — one bullet per change; each opens with its name and carries the proving number (token cost, count).
6. "How we made sure it was safe" — the verification story (red teams, what they caught).
7. "What changes for you" — action required (usually none), deferred follow-ups, closing pointer to the technical record (work-log / decisions paths).

Plain register throughout; the technical record stays in the ledger files, the doc only points to it.

## Other document shapes
- Specific audience named (sharp VC, due diligence, engineering note): the skeleton is the floor; adjust depth, keep the voice rules.
- Status or work ledgers: dated entries, newest on top, self-contained per entry.

## Rendering pipeline
- Write `.md` first (source of truth). Markdown is the v1 default and needs no conversion step.
- Optional user-facing docx: build via python-docx with explicit Calibri, heading, bullet, and HR styling. Do not use a generic one-shot exporter; author the builder so styling is explicit and repeatable.
- Quick converts: a markdown-to-docx converter handles headings, bullets, bold, and italics but typically does NOT preserve tables; convert pipe tables in a second pass or avoid tables in docx targets.
- "Adjust, don't recreate": surgical edits on an existing docx (clone paragraph XML, wipe runs); never regenerate a reviewed document from scratch.
