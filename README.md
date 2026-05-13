# Career Agent

A Claude Code project that turns job searching into a structured workflow. Your career history, goals, target companies, and active applications all live in one repo so Claude can reason across them. No more juggling Google Docs, Notion, and a dozen open Job Descriptions.

## A typical day

```
Morning   →   /morning                                  briefing on open items + suggested first move
   ↓
Daytime   →   paste a Job Description, build a          per-role artifacts appear under
              resume, run a mock interview,             applications/<company>/<role>/
              practice coding
   ↓
Evening   →   "wrap up the day"                         log written to career/daily-log/YYYY-MM-DD.md
```

This repo handles the **deep work**: Job Description analysis, tailored resumes, interview prep, per-role artifacts. Application *status* (stage, dates applied, outcomes, match level) is intentionally **not** stored here. Keep that in Notion or your tracker of choice. The two systems don't need to sync because they don't overlap.

## What's ready to use

| Skill | What it does | Trigger phrase |
|---|---|---|
| `job-analyzer` | Paste a Job Description, get a grounded fit analysis (skills match, level alignment, gaps, comp signal). Persists Job Description + analysis to `applications/<company>/<role>/role.md`. | *"Here's a Job Description: [paste]. Worth pursuing?"* |
| `resume-builder` | Reshape your impact doc into a posting-specific resume in Markdown and `.docx`. | *"Build a resume for this Stripe staff role: [Job Description]"* |
| `cover-letter` | Write a tailored cover letter grounded in your impact doc and the role's specific requirements. Saves `.md` and `.docx` alongside the resume. | *"Write a cover letter for the Stripe staff role"* |
| `daily-summary` | EOD log of artifacts touched, open loops, patterns across the day, and concrete next steps. Writes to `career/daily-log/YYYY-MM-DD.md`. | *"Wrap up the day"* / *"EOD summary"* |
| `morning` | AM briefing: yesterday's open items + stale roles (>7 days untouched) + one suggested first move. Read-only. | *"/morning"* / *"What's on my plate today?"* |

## In progress

| Skill | Status |
|---|---|
| `interview-prep` | STAR story bank and mock behavioral rounds. Coming soon. |
| `coding-prep` | Socratic tutoring and mock technical rounds. Coming soon. |
| `job-scraper` | Batch URL scraping, role clustering, and per-cluster resumes. Coming soon. |

Every skill is grounded in the files under `career/`: your impact doc, goals, and brag doc. Fill those in once and the advice stops being generic.

## Dependencies

All dependencies are Python packages. Install them once before first use.

| Package | Used by | Install |
|---|---|---|
| `python-docx` | `resume-builder`, `cover-letter` (generates `.docx` output) | `pip install python-docx` |
| `reportlab` | `resume-builder` (generates `.pdf` output) | `pip install reportlab` |
| `requests` | `job-scraper`, `job-analyzer` (fetches URLs) | `pip install requests` |
| `beautifulsoup4` | `job-scraper` (parses scraped HTML) | `pip install beautifulsoup4` |

Install all at once:

```bash
pip install python-docx reportlab requests beautifulsoup4
```

You also need [Claude Code](https://claude.ai/code) installed and authenticated.

## Setup

1. Clone the repo and `cd` into it.
2. Copy the templates into your own (gitignored) working files:
   ```bash
   cp career/impact-doc.template.md    career/impact-doc.md
   cp career/goals.template.md         career/goals.md
   cp career/brag-doc.template.md      career/brag-doc.md
   cp career/personal-info.template.md career/personal-info.md
   ```
3. Install dependencies (see above).
4. Open the folder in Claude Code: `claude` from inside the directory.
5. Fill in your real content in:
   - `career/personal-info.md`: name, email, phone, location, LinkedIn (used in every resume and cover letter header)
   - `career/impact-doc.md`: your detailed work history (most important)
   - `career/goals.md`: what you're targeting
   - `career/brag-doc.md`: raw material for resumes and stories

The `career/*.md` working files, `career/daily-log/`, and everything under `applications/` are gitignored, so your personal data stays local. Only the `.template.md` skeletons are shared.

## File layout

```
career/                              # Your background. Edit these
  impact-doc.template.md             # template (committed)
  impact-doc.md                      # your version (gitignored)
  goals.template.md
  goals.md                           # gitignored
  brag-doc.template.md
  brag-doc.md                        # gitignored
  personal-info.template.md          # template (committed)
  personal-info.md                   # your contact info (gitignored)
  current-resume.md                  # gitignored (create as needed)
  story-bank.json                    # gitignored (created by interview-prep)
  coding-log.md                      # gitignored (created by coding-prep)
  daily-log/                         # gitignored (created by daily-summary)
    2026-05-11.md
applications/                        # Per-application work (gitignored)
  <company>/
    <role-slug>/
      role.md                        # Job Description + fit analysis + notes (from job-analyzer)
      resume.md / .docx              # tailored resume (from resume-builder)
      cover-letter.md / .docx        # tailored cover letter (from cover-letter)
      story-bank.json                # tailored stories (from interview-prep)
      interviews/                    # per-round notes
.claude/
  skills/                            # Skill definitions
    job-analyzer/
    job-scraper/
      scrape.py
      parse.py
      output/<date>/                 # scraper run outputs
    resume-builder/
    cover-letter/
    interview-prep/
    coding-prep/
    daily-summary/
    morning/
  settings.local.json                # personal permissions (gitignored)
CLAUDE.md                            # project-level instructions to Claude
```

## Notes

- The scraper auto-fails on LinkedIn and Indeed (login/JS walls). When that happens, paste the Job Description text and the workflow continues.
- `role.md` files store the Job Description, fit analysis, and free-form notes only. No status fields. Stage, outcome, dates applied, referral, match level all live in your external tracker (e.g., Notion).
- All skill outputs are plain markdown files you can edit by hand at any time.
- If you found the tool (or our collaboration) helpful, I'd appreciate a quick LinkedIn recommendation on my profile: [Link](https://www.linkedin.com/in/rishabh-modi-736a33149/). No pressure at all, but it would be a huge help!
