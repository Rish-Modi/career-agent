# Career Agent

A Claude Code project that turns job searching into a structured workflow. Your career history, goals, target companies, and active applications all live in one place so Claude can reason across them. No more juggling Google Docs, Notion, and a dozen open Job Descriptions.

## A typical day

```
Morning   →   /morning                                  briefing on open items + suggested first move
   ↓
Daytime   →   paste a Job Description, build a          per-role artifacts appear under
              resume, run a mock interview,             $PERSONAL/applications/<company>/<role>/
              practice coding
   ↓
Evening   →   "wrap up the day"                         log written to $PERSONAL/career/daily-log/YYYY-MM-DD.md
```

This repo handles the **deep work**: Job Description analysis, tailored resumes, interview prep, per-role artifacts. Application *status* (stage, dates applied, outcomes, match level) is intentionally **not** stored here. Keep that in Notion or your tracker of choice. The two systems don't need to sync because they don't overlap.

## How to use job-analyzer

Use this when you want a grounded read on whether a single posting is worth pursuing. It compares the role against your impact doc and saves the Job Description plus the analysis to your private applications folder.

1. Open the repo in Claude Code.
2. Paste the Job Description text (or a URL, if it's a site Claude can fetch). One posting per request.
3. Ask: *"Worth pursuing?"* or *"How do I fit?"*
4. Claude returns: skills match, level alignment, gaps, comp signal, and a recommendation.
5. The Job Description, the analysis, and any free-form notes get persisted to `$PERSONAL/applications/<company>/<role-slug>/role.md` so you can revisit later or feed it into `resume-builder` and `cover-letter-builder`.

## How to use coding-prep

TypeScript-first coding interview practice. The shared problem bank lives in this repo at `coding-bank/problems/`; your attempts and notes stay private in `$PERSONAL/career/coding-log/`.

There are four entry points:

1. **Add a problem to the bank.** Paste the problem name, description, difficulty, examples, constraints, and hints. Claude saves it to `coding-bank/problems/<slug>.md` so you (or anyone using the repo) can practice it later.
2. **Practice an existing problem.** Say *"let's practice two-sum"* or *"surprise me from weak spots"*. Claude asks upfront whether you want **tutoring** (hint ladder + pattern teaching) or **evaluation only** (you solve on LeetCode, paste your code, Claude grades it). Each attempt is logged.
3. **Run a mock interview.** Say *"mock me"*. Timed 45 minutes, no hints, follow-up variant after you solve, structured rubric grade at the end (hire / lean hire / lean no-hire / no-hire).
4. **Ask what to redo.** Say *"what should I redo today?"* or *"what are my weak spots?"*. Claude reads your attempt log and surfaces failed or stale problems.

All attempts append to `$PERSONAL/career/coding-log/attempts.jsonl` (queryable), with rolling per-problem notes in `$PERSONAL/career/coding-log/by-problem/<slug>.md`.

## What's ready to use

| Skill | What it does | Trigger phrase |
|---|---|---|
| `job-analyzer` | Paste a Job Description, get a grounded fit analysis (skills match, level alignment, gaps, comp signal). Persists Job Description + analysis to `$PERSONAL/applications/<company>/<role>/role.md`. | *"Here's a Job Description: [paste]. Worth pursuing?"* |
| `resume-builder` | Reshape your impact doc into a posting-specific resume in Markdown and `.docx`. | *"Build a resume for this Stripe staff role: [Job Description]"* |
| `cover-letter-builder` | Write a tailored cover letter grounded in your impact doc and the role's specific requirements. Saves `.md` and `.docx` alongside the resume. | *"Write a cover letter for the Stripe staff role"* |
| `coding-prep` | TypeScript coding interview practice. Add problems to the shared bank, then practice (tutoring or evaluation), run a timed mock, or query weak spots from your attempt log. | *"Let's practice two-sum"* / *"Mock me on a medium array problem"* |
| `daily-summary` | EOD log of artifacts touched, open loops, patterns across the day, and concrete next steps. Writes to `$PERSONAL/career/daily-log/YYYY-MM-DD.md`. | *"Wrap up the day"* / *"EOD summary"* |
| `morning` | AM briefing: yesterday's open items + stale roles (>7 days untouched) + one suggested first move. Read-only. | *"/morning"* / *"What's on my plate today?"* |

## In progress

| Skill | Status |
|---|---|
| `interview-prep` | STAR story bank and mock behavioral rounds. Coming soon. |

Every skill is grounded in your personal files under `$PERSONAL/career/`: your impact doc, goals, and brag doc. Fill those in once and the advice stops being generic.

## Where your personal data lives

Your private career data is stored **outside this repo** in a sibling directory called `career-agent-personal-docs/`. The repo itself only carries code, templates, and instructions, never personal content.

```
Coding/
  career-agent/                       # this repo (committed to git)
  career-agent-personal-docs/         # your private data (NOT in git, sibling of repo)
```

Throughout the skills and `CLAUDE.md`, `$PERSONAL` refers to the absolute path of that sibling directory. Skills resolve it dynamically from the git root, so it works from the main checkout and from any worktree without hard-coding.

## Dependencies

All dependencies are Python packages. Install them once before first use.

| Package | Used by | Install |
|---|---|---|
| `python-docx` | `resume-builder`, `cover-letter-builder` (generates `.docx` output) | `pip install python-docx` |
| `reportlab` | `resume-builder` (generates `.pdf` output) | `pip install reportlab` |
| `requests` | `job-analyzer` (fetches URLs) | `pip install requests` |

Install all at once:

```bash
pip install python-docx reportlab requests
```

You also need [Claude Code](https://claude.ai/code) installed and authenticated.

## Setup

1. Clone the repo and `cd` into it.
2. Create the sibling directory for personal data and bootstrap it from the templates:
   ```bash
   PERSONAL="$(dirname "$(pwd)")/career-agent-personal-docs"
   mkdir -p "$PERSONAL/career" "$PERSONAL/applications"
   cp career/impact-doc.template.md    "$PERSONAL/career/impact-doc.md"
   cp career/goals.template.md         "$PERSONAL/career/goals.md"
   cp career/brag-doc.template.md      "$PERSONAL/career/brag-doc.md"
   cp career/personal-info.template.md "$PERSONAL/career/personal-info.md"
   ```
3. Install dependencies (see above).
4. Open the repo in Claude Code: `claude` from inside the directory.
5. Fill in your real content in:
   - `$PERSONAL/career/personal-info.md`: name, email, phone, location, LinkedIn (used in every resume and cover letter header)
   - `$PERSONAL/career/impact-doc.md`: your detailed work history (most important)
   - `$PERSONAL/career/goals.md`: what you're targeting
   - `$PERSONAL/career/brag-doc.md`: raw material for resumes and stories

Because `career-agent-personal-docs/` sits outside the repo, your personal data is never tracked by git. The repo only ships the `.template.md` skeletons.

## File layout

```
career-agent/                              # this repo
  career/                                  # templates only (committed)
    impact-doc.template.md
    goals.template.md
    brag-doc.template.md
    personal-info.template.md
  coding-bank/                             # shared coding problem library (committed)
    README.md
    problems/
      <slug>.md                            # one file per problem, problem text only
  .claude/
    skills/                                # skill definitions
      job-analyzer/
      resume-builder/
      cover-letter-builder/
      interview-prep/
      coding-prep/
      daily-summary/
      morning/
    settings.local.json                    # personal permissions (gitignored)
  CLAUDE.md                                # project-level instructions to Claude
  README.md

career-agent-personal-docs/                # sibling of repo, NOT in git
  career/
    impact-doc.md                          # your version (created from template)
    goals.md
    brag-doc.md
    personal-info.md                       # your contact info
    current-resume.md                      # optional, create as needed
    story-bank.json                        # created by interview-prep
    coding-log/                            # created by coding-prep
      attempts.jsonl                       # append-only log, one line per attempt
      by-problem/
        <slug>.md                          # rolling notes per problem, linked to coding-bank by slug
    daily-log/                             # created by daily-summary
      2026-05-11.md
  applications/                            # per-application work
    <company>/
      <role-slug>/
        role.md                            # Job Description + fit analysis + notes (from job-analyzer)
        resume.md / .docx                  # tailored resume (from resume-builder)
        cover-letter.md / .docx            # tailored cover letter (from cover-letter-builder)
        story-bank.json                    # tailored stories (from interview-prep)
        interviews/                        # per-round notes
```

## Notes

- `job-analyzer` will try to fetch a Job Description from a URL, but LinkedIn and Indeed block automated fetches behind login/JS walls. When that happens, paste the Job Description text and the workflow continues.
- `role.md` files store the Job Description, fit analysis, and free-form notes only. No status fields. Stage, outcome, dates applied, referral, match level all live in your external tracker (e.g., Notion).
- All skill outputs are plain markdown files you can edit by hand at any time.
- Because personal data lives in a sibling directory (`../career-agent-personal-docs/`), it stays accessible from the main checkout and from any worktree without any symlink trickery. No per-worktree setup needed.
- If you found the tool (or our collaboration) helpful, I'd appreciate a quick LinkedIn recommendation on my profile: [Link](https://www.linkedin.com/in/rishabh-modi-736a33149/). No pressure at all, but it would be a huge help!
