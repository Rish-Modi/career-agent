# Career Agent

A Claude Code project that turns job searching into a structured workflow. Your career history, goals, target companies, and active applications all live in one repo so Claude can reason across them. No more juggling Google Docs, Notion, and a dozen open JDs.

## What it helps you do

| Skill | What it does | Trigger phrase |
|---|---|---|
| `job-analyzer` | Paste a JD, get a grounded fit analysis (skills match, level alignment, gaps, comp signal). Persists JD + analysis to `applications/<company>/<role>/role.md`. | *"Here's a JD: [paste]. Worth pursuing?"* |
| `job-scraper` | Drop 10+ URLs, get them clustered by role archetype with a tailored resume per cluster. | *"Here are 8 jobs: [URLs]. Cluster and build resumes."* |
| `resume-builder` | Reshape your impact doc into a posting-specific resume in Markdown, `.docx`, and `.pdf`, versioned in git so you can diff drafts. | *"Build a resume for this Stripe staff role: [JD]"* |
| `interview-prep` | STAR-formatted story bank from your real work history; mock behavioral rounds with hire / no-hire feedback. | *"Build my story bank for the Datadog interview"* / *"Mock interview me, Stripe E5 behavioral"* |
| `coding-prep` | Socratic tutoring that won't hand you the solution; mock technical rounds with time-boxing; log of where you stumbled. | *"Practice a medium sliding-window problem"* / *"Mock interview me, 45 min, Google-style"* |
| `daily-summary` | EOD log of artifacts touched, open loops, patterns across the day, and concrete next steps. Writes to `career/daily-log/YYYY-MM-DD.md`. | *"Wrap up the day"* / *"EOD summary"* |
| `morning` | AM briefing: yesterday's open items + stale roles (>7 days untouched) + one suggested first move. Read-only. | *"/morning"* / *"What's on my plate today?"* |

Every skill is grounded in the files under `career/`: your impact doc, goals, and brag doc. Fill those in once and the advice stops being generic.

## Setup

1. Clone the repo and `cd` into it.
2. Copy the templates into your own (gitignored) working files:
   ```bash
   cp career/impact-doc.template.md career/impact-doc.md
   cp career/goals.template.md      career/goals.md
   cp career/brag-doc.template.md   career/brag-doc.md
   ```
3. Open the folder in Claude Code: `claude` from inside the directory.
4. Fill in your real content in:
   - `career/impact-doc.md`: your detailed work history (most important)
   - `career/goals.md`: what you're targeting
   - `career/brag-doc.md`: raw material for resumes and stories
5. Install scraper dependencies (one-time):
   ```bash
   pip install requests beautifulsoup4 --break-system-packages
   ```

The `career/*.md` working files, `career/daily-log/`, and everything under `applications/` are gitignored, so your personal data stays local. Only the `.template.md` skeletons are shared.

## A typical day

```
Morning   →   /morning                                  briefing on open items + suggested first move
   ↓
Daytime   →   paste a JD, build a resume, run a         per-role artifacts appear under
              mock interview, practice coding           applications/<company>/<role>/
   ↓
Evening   →   "wrap up the day"                         log written to career/daily-log/YYYY-MM-DD.md
```

This repo handles the **deep work**: JD analysis, tailored resumes, interview prep, per-role artifacts. Application *status* (stage, dates applied, outcomes, match level) is intentionally **not** stored here. Keep that in Notion or your tracker of choice. The two systems don't need to sync because they don't overlap.

## File layout

```
career/                              # Your background. Edit these
  impact-doc.template.md             # template (committed)
  impact-doc.md                      # your version (gitignored)
  goals.template.md
  goals.md                           # gitignored
  brag-doc.template.md
  brag-doc.md                        # gitignored
  current-resume.md                  # gitignored (create as needed)
  story-bank.json                    # gitignored (created by interview-prep)
  coding-log.md                      # gitignored (created by coding-prep)
  daily-log/                         # gitignored (created by daily-summary)
    2026-05-11.md
applications/                        # Per-application work (gitignored)
  <company>/
    <role-slug>/
      role.md                        # JD + fit analysis + notes (from job-analyzer)
      resume.md / .pdf               # tailored resume (from resume-builder)
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
    interview-prep/
    coding-prep/
    daily-summary/
    morning/
  settings.local.json                # personal permissions (gitignored)
CLAUDE.md                            # project-level instructions to Claude
```

## Notes

- The scraper auto-fails on LinkedIn and Indeed (login/JS walls). When that happens, paste the JD text and the workflow continues.
- `role.md` files store the JD, fit analysis, and free-form notes only. No status fields. Stage, outcome, dates applied, referral, match level all live in your external tracker (e.g., Notion).
- All skill outputs are plain markdown files you can edit by hand at any time.
