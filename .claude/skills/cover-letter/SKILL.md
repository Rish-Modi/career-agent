---
name: cover-letter
description: Generate a tailored cover letter for a specific job posting. Use when the user asks for a cover letter for a role. Produces Markdown and .docx outputs.
---

# Cover Letter Generator

## When to use
Any request to write or tailor a cover letter for a specific role. Requires a target JD or an existing `role.md` to ground the letter.

## Inputs
- **Source material** — read all that exist before drafting:
  - `career/impact-doc.md` — always. Primary source of truth for roles, projects, and metrics.
  - `career/brag-doc.md` — read if it exists. Contains quantified wins and recognition that may not appear in the impact doc. Cross-check metrics here; the brag doc often has stronger or more specific numbers.
  - `career/goals.md` — read if it exists. Use to understand what the user is optimizing for and how to frame the letter's angle.
  - `career/personal-info.md` — read if it exists. Use for the closing signature block: name, email, phone, LinkedIn. Omit GitHub unless specifically requested. If the file does not exist, use placeholders and note them.
- **Role context** (one of, in priority order):
  - Existing `applications/<company>/<role-slug>/role.md` — use the fit analysis and JD already on disk
  - A pasted JD or URL — fetch and parse it fresh
- **Optional user direction**: specific angle to lead with, a talking point to include, or a point to omit.
- **Length**: default 3-4 short paragraphs, ~250-350 words. Confirm if I want longer.

## Workflow

### 1. Get the JD and fit context
Check whether `applications/<company>/<role-slug>/role.md` exists. If it does, read it for the full JD and the fit analysis. If not, fetch or request the JD and run a quick mental fit pass before writing.

If neither exists and no JD was provided, ask for one before proceeding.

### 2. Identify 2-3 strongest fit signals
From `impact-doc.md`, find the 2-3 experiences that most directly address the role's core responsibilities. These become the backbone of the letter's body. Do not try to cover everything.

Prefer signals that:
- Are quantified
- Involve the same domain, scale, or problem type as the role
- Demonstrate scope beyond the individual contributor level (if the role is senior/staff)

### 3. Draft the letter

**Structure:**

**Opening (1 paragraph):** A direct, confident hook that names the company and connects my background to a specific thing they're building or solving. Not "I am writing to express my interest." The opening should make a concrete claim the rest of the letter supports.

**Body (2 paragraphs):** Each paragraph centers on one strong fit signal from step 2. Lead with the outcome, then explain what I did and why it's relevant to this role. No retelling of the resume chronologically. Every paragraph should end with a sentence that ties back to the role's challenge or the company's trajectory.

**Closing (1 paragraph):** One sentence expressing genuine interest in the specific role (not just the company generically), one sentence on what I bring to the table in summary, and a clean call to action.

### 4. Tailoring pass
- Match the JD's vocabulary where truthful (use their phrasing for team structure, product area, engineering challenge)
- Reorder or reframe the body paragraphs to lead with the strongest fit
- Strip any sentence that could appear in a letter for a different company without changing a word

### 5. Critique pass
Before finalizing, check every paragraph:
- Does the opening make a concrete claim? Or does it just state that I'm applying?
- Does each body paragraph have a number or a concrete scope signal?
- Does anything read like it was copied from the resume? If so, reframe it as narrative.
- Is there any filler ("I am passionate about," "I thrive in fast-paced environments")? Delete it.

### 6. Produce outputs
Save to `applications/<company>/<role-slug>/`:
- `cover-letter.md` — clean Markdown, source of truth
- `cover-letter.docx` — using the docx skill, matching the resume's formatting style (same font, margins)

If the application folder does not exist yet, create it. Tell the user the saved path.

**If `cover-letter.md` already exists**, prompt before overwriting:
- **Overwrite** — replace entirely.
- **Revise** — take the existing letter as a draft and apply targeted edits (good for second-pass refinements).
- **Cancel** — print to terminal only, write nothing.

### 7. Summarize
End with 2-3 sentences: what angle the letter leads with, what it deprioritizes, and anything from `impact-doc.md` that is underspecified and would strengthen a future draft (without fabricating).

## Anti-patterns
- Never open with "I am writing to apply for..." or any variant. Find a hook.
- Don't retell the resume chronologically. The letter explains *why* this role, not *what* I did.
- Don't list technologies or skills as a paragraph. That's the resume's job.
- Don't invent metrics. If the number isn't in my files, use scope or scale instead, or flag the gap.
- Don't pad to length. A tight 250-word letter beats a meandering 400-word one.
- Don't include the recipient's name or address block unless I provide it. Use a clean salutation: "Dear Hiring Manager," or the team name if known.
- Don't write a generic enthusiasm paragraph. Every sentence must earn its place by being specific to this role and company.
- **Never use em dashes or en dashes** (— or –) anywhere in the letter. Replace with a comma, colon, period, or parentheses. No exceptions.
