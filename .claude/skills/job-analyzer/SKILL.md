---
name: job-analyzer
description: Analyze a single job posting for fit against my background. Use when the user shares one job description (pasted text or URL) and wants a fit assessment, not batch analysis. For multiple postings, use job-scraper instead.
---

# Job Analyzer

## When to use
The user shares a single job description — pasted text, a URL, or both — and wants to know if it's worth pursuing.

For 2+ postings at once, hand off to `job-scraper`.

## Workflow

### 1. Get the Job Description
If a URL is provided, fetch it. If fetching fails or the page is JS-heavy (LinkedIn etc.), ask the user to paste the text.

### 2. Extract structure
Identify:
- Role title and level signals
- Required skills/experience
- Nice-to-have skills
- Core responsibilities and scope
- Comp range (if listed)
- Location and remote policy
- Team/org context if mentioned

### 3. Fit assessment
For each significant requirement, rate against my background (from `$PERSONAL/career/impact-doc.md`). `$PERSONAL` is the personal-docs sibling directory defined in `CLAUDE.md`. Resolve it once at the start of the session and reuse.

| Requirement | Rating | Justification |
|---|---|---|
| 7+ years backend | Strong | 7 years across AWS + Bill |
| Kubernetes at scale | Moderate | Used at Bill, not deep operator-level |
| ML systems | Gap | No direct experience |

Use **Strong / Moderate / Gap** — three buckets, no fence-sitting. Each justification must cite something concrete from my career, not generic claims.

### 4. Red and green flags
Scan the Job Description's *language*, not just its requirements:
- **Red flags**: vague scope, kitchen-sink requirements, "rockstar/ninja," unrealistic stack breadth, no mention of team, comp far below market, urgency cues that suggest churn
- **Green flags**: clear scope, specific problems to solve, named team/org, reasonable level expectations, signals of engineering maturity (e.g., mentions of design review, on-call rotation structure, mentorship)

### 5. Verdict
One of:
- **Great fit** — apply, lead with these strengths: [...]
- **Stretch** — worth applying if [condition]; will need to address [gap] in conversation
- **Poor fit** — skip, unless [specific reason to reconsider]

### 6. If applying, recommend
- Top 3 strengths to lead with (cite specific work from my impact doc)
- Gaps to preempt and how to frame them
- Questions to ask the recruiter/hiring manager to clarify ambiguity in the Job Description

### 7. Save the role workspace
After producing the analysis, persist it to disk so downstream skills (`resume-builder`, `interview-prep`) and future sessions can reference it.

**Folder convention:** `$PERSONAL/applications/<company-slug>/<role-slug>/role.md`

Slug rules:
- Lowercase, kebab-case, ASCII-only.
- **Company slug**: short, canonical form. `Apple Inc.` → `apple`. `Stripe, Inc.` → `stripe`. `Meta Platforms` → `meta`.
- **Role slug**: title + the *distinguishing* qualifier, not the full posting title. `Staff Software Engineer, Payments Infrastructure` → `staff-payments-infra`. Keep it short enough to skim in the folder tree (≤ 5 words).
- If a slug is ambiguous (e.g., two open Stripe staff roles), ask the user to disambiguate before writing.

**If the target file already exists**, prompt the user:
- **Overwrite** — replace the entire file with the new analysis. Use when the prior analysis is outdated or wrong.
- **Append** — add a new `## Fit analysis (re-run on YYYY-MM-DD)` section below the existing one. Default for re-runs after updating `impact-doc.md` or `goals.md`. Preserves history.
- **Cancel** — print the analysis to the terminal only, write nothing.

Tracking state (stage, outcome, dates applied, referral, match level) is **not** stored here — that lives in the user's external tracker. `role.md` is a working artifact for the role's content and analysis only.

**Schema (single file, YAML frontmatter + body):**

```markdown
---
position: Staff Software Engineer, Payments Infrastructure
company: Stripe
location: San Francisco, CA
work_mode: hybrid                    # remote | hybrid | onsite | unknown
job_id: 6173829                      # if available, else null
link: https://stripe.com/jobs/...    # canonical posting URL
date_added: 2026-05-11               # today's date when first created
comp_range: $280k–$380k TC           # if stated in Job Description, else null
tech_stack: [Ruby, Go, Kafka, Postgres]
---

## Fit analysis
(the Strong/Moderate/Gap table + red/green flags + verdict + recommendations from steps 3–6)

## Job Description
(full pasted Job Description text, verbatim, so we don't lose it if the URL rots)

## Notes
(empty placeholder for the user's ongoing free-form notes — questions, recruiter context, follow-ups)
```

After writing, tell the user the absolute path it landed at (resolved from `$PERSONAL`), e.g. `Saved to <absolute>/career-agent-personal-docs/applications/stripe/staff-payments-infra/role.md`.

## Output format
Concise. Table for the requirements grid, prose for everything else. No filler. End with the verdict in bold so I can scan it. Mention the saved path on the last line.

## What not to do
- Don't soften the verdict to be encouraging. If it's a poor fit, say so.
- Don't pad with generic interview tips — that's `interview-prep`'s job.
- Don't generate a resume here — that's `resume-builder`'s job. You can note "this would benefit from a tailored resume emphasizing X" and stop.
- Don't write status fields (stage, outcome, match level, referral, date_applied) into the frontmatter — those live in the user's external tracker, not here.
- Don't auto-overwrite an existing `role.md` without prompting.
