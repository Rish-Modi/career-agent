# Career Guide

A Claude Code project for managing job search and career progression.

## Setup

1. Open this folder in Claude Code: `claude` from inside the directory.
2. Fill in the template files in `career/`:
   - `impact-doc.md` — your detailed work history (most important)
   - `goals.md` — what you're targeting
   - `brag-doc.md` — raw material for resumes and stories
3. Install scraper dependencies (one-time):
   ```bash
   pip install requests beautifulsoup4 --break-system-packages
   ```

## Skills

- **`job-analyzer`** — "Is this a good fit?" on a single posting
- **`job-scraper`** — Batch-analyze multiple postings, cluster them, generate tailored resumes per cluster
- **`resume-builder`** — Build/tailor resumes (Markdown + .docx + .pdf)
- **`interview-prep`** — Behavioral prep, STAR stories, mock interviews
- **`coding-prep`** — Coding interview practice with Socratic tutoring

## Usage patterns

### Quick fit check
> "Here's a JD: <paste>. Is this worth pursuing?"
Triggers `job-analyzer`.

### Batch analysis with tailored resumes
> "Here are 8 jobs I'm considering: <list of URLs>. Cluster them and build resumes."
Triggers `job-scraper` → confirms buckets with you → invokes `resume-builder` per bucket.

### Tailored resume for a specific role
> "Build me a resume for this Stripe staff role: <JD>."
Triggers `resume-builder` with the JD as target.

### Behavioral prep
> "I have an interview at Datadog next week. Build my story bank."
Triggers `interview-prep` story bank mode.
> "Mock interview me for a Stripe E5 behavioral round, strict mode."
Triggers `interview-prep` mock mode.

### Coding practice
> "Practice a medium sliding-window problem with me."
Triggers `coding-prep` in Socratic mode.
> "Mock interview me, 45 min, Google-style."
Triggers `coding-prep` mock mode.

## File layout

```
career/                          # Your background — edit these
  impact-doc.md
  goals.md
  brag-doc.md
  current-resume.md              # (create as needed)
  story-bank.json                # (created by interview-prep)
  coding-log.md                  # (created by coding-prep)
applications/                    # Per-application work
  <company>-<role>/
.claude/skills/                  # Skill definitions
  job-analyzer/
  job-scraper/
    scrape.py
    parse.py
    output/<date>/                # Scraper run outputs
  resume-builder/
  interview-prep/
  coding-prep/
CLAUDE.md                        # Project-level instructions
```

## Notes

- The scraper auto-fails on LinkedIn and Indeed (login/JS walls). When that happens, paste the JD text and the workflow continues.
- All skill outputs are files you can version with git. Consider `git init` so you can track resume iterations.
