---
name: resume-builder
description: Build, tailor, or revise a resume. Use when the user asks for a resume — either a general version or one tailored to a specific job posting or archetype profile. Produces Markdown, .docx, and .pdf outputs.
---

# Resume Builder

## When to use
Any request to build, tailor, revise, or critique a resume. Also invoked by `job-scraper` to produce per-cluster resume variants.

## Inputs
- **Source material**: `career/impact-doc.md` (always), `career/brag-doc.md` if it exists, `career/current-resume.md` as a baseline if it exists.
- **Target** (one of):
  - A specific job description → tailor to it
  - An archetype profile from `job-scraper` → tailor to the cluster
  - "General" → produce a strong default version
- **Length preference**: default 1 page. Confirm if I want longer.

## Workflow

### 1. Confirm target
If the target isn't obvious from context, ask:
- Specific JD, archetype profile, or general?
- Length preference?
- Any role/company I'm asking you to *deprioritize* (e.g., I don't want my AWS work to dominate)?

### 2. Pull and rewrite bullets
For each role in my career, draft bullets using **XYZ format**:
> Accomplished **X** by doing **Y**, measured by **Z**.

Every bullet must:
- Start with a strong action verb (built, led, shipped, reduced, architected — not "responsible for," "helped with," "worked on")
- Include scope (team size, system scale, dollar impact, user count, request volume — whatever applies)
- Include a quantified outcome where possible

If `impact-doc.md` is missing the numbers, surface that and ask me to fill them in rather than fabricating.

### 3. Tailor
When a target JD or archetype is provided:
- Match the JD's keyword vocabulary where it's truthful (e.g., if they say "distributed systems," use that phrase if it applies to my work — don't keyword-stuff with terms I haven't used)
- Reorder bullets so the most relevant come first within each role
- Cut bullets that don't reinforce the target — even strong ones
- Adjust the summary/header to mirror the role's framing

### 4. Critique pass
Before finalizing, evaluate every bullet:
- Does it have a number? If not, can I add one?
- Does it lead with action and outcome, or with the situation?
- Could a less impressive engineer write the same bullet? If yes, sharpen it.
- Is the scope clear?

Flag weak bullets explicitly with proposed alternatives.

### 5. Produce outputs
Create three formats in `applications/<company>-<role>/` (or `career/resumes/<variant>/` for general versions):
- `resume.md` — clean Markdown, the source of truth
- `resume.docx` — using the docx skill
- `resume.pdf` — using the pdf skill

For the .docx and .pdf, use a clean professional template — single column, sans-serif, no graphics, no skill bars, no photo. ATS-friendly.

### 6. Summarize the changes
End with a short summary of:
- What you emphasized and why
- What you cut and why
- Anything you flagged as weak that I should improve at the source (in `impact-doc.md` or `brag-doc.md`)

## Anti-patterns
- Don't invent metrics. If the number isn't in my files, ask.
- Don't keyword-stuff. ATS optimization is real, but obvious stuffing reads worse than honest framing.
- Don't include an "Objective" section. Use a one-line professional summary instead, only if it adds signal.
- Don't list every technology I've ever touched. Curate to what matters for the target.
- One page unless explicitly asked otherwise. Senior-level resumes can justify two pages; if I'm targeting staff+, ask.
