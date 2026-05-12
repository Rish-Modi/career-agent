---
name: job-analyzer
description: Analyze a single job posting for fit against my background. Use when the user shares one job description (pasted text or URL) and wants a fit assessment, not batch analysis. For multiple postings, use job-scraper instead.
---

# Job Analyzer

## When to use
The user shares a single job description — pasted text, a URL, or both — and wants to know if it's worth pursuing.

For 2+ postings at once, hand off to `job-scraper`.

## Workflow

### 1. Get the JD
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
For each significant requirement, rate against my background (from `career/impact-doc.md`):

| Requirement | Rating | Justification |
|---|---|---|
| 7+ years backend | Strong | 7 years across AWS + Bill |
| Kubernetes at scale | Moderate | Used at Bill, not deep operator-level |
| ML systems | Gap | No direct experience |

Use **Strong / Moderate / Gap** — three buckets, no fence-sitting. Each justification must cite something concrete from my career, not generic claims.

### 4. Red and green flags
Scan the JD's *language*, not just its requirements:
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
- Questions to ask the recruiter/hiring manager to clarify ambiguity in the JD

## Output format
Concise. Table for the requirements grid, prose for everything else. No filler. End with the verdict in bold so I can scan it.

## What not to do
- Don't soften the verdict to be encouraging. If it's a poor fit, say so.
- Don't pad with generic interview tips — that's `interview-prep`'s job.
- Don't generate a resume here — that's `resume-builder`'s job. You can note "this would benefit from a tailored resume emphasizing X" and stop.
