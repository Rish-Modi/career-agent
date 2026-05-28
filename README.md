# Career Agent

A Claude Code project that turns job searching into a structured workflow. Your career history, goals, target companies, and active applications all live in one place so Claude can reason across them. No more juggling scattered docs and a dozen open Job Descriptions.

**New here? Run `/onboard` inside Claude Code to get started.** It bootstraps your personal data directory, checks prerequisites, and walks you through the four core docs the rest of the tool reads from. Already set up? Run `/help` any time to see what each skill does or learn how to chain them.

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

This repo handles the **deep work**: Job Description analysis, tailored resumes, interview prep, per-role artifacts. Lightweight tracking fields (stage, outcome, date applied, referral, match level) are supported optionally on each `role.md` and only written when you mention them inline. The repo isn't an application tracker; manage your pipeline however you prefer.

## The toolbox

| Skill | What it does | Trigger phrase |
|---|---|---|
| `onboard` | First-run setup. Bootstraps `$PERSONAL`, checks prereqs, and interviews you for the four core docs. | *"/onboard"* / *"I just cloned the repo"* |
| `help` | Lists every skill, explains one on request, and walks through common workflows. | *"/help"* / *"what can you do"* |
| `job-analyzer` | Paste a Job Description, get a grounded fit analysis. Persists Job Description + analysis to `$PERSONAL/applications/<company>/<role>/role.md`. | *"Here's a Job Description: [paste]. Worth pursuing?"* |
| `resume-builder` | Reshape your impact doc into a posting-specific resume in Markdown, `.docx`, and `.pdf`. | *"Build a resume for this Stripe staff role"* |
| `cover-letter-builder` | Tailored cover letter grounded in your impact doc and the role's requirements. Outputs `.md` and `.docx`. | *"Write a cover letter for the Stripe staff role"* |
| `coding-prep` | Coding interview practice in your preferred language. Shared problem bank, private attempt log, tutoring or evaluation mode, timed mocks. | *"Let's practice two-sum"* / *"Mock me on a medium array problem"* |
| `star-stories` | Convert your projects into STAR-format Markdown files (one per project, multiple angles per file). Raw material for behavioral interviews. | *"STARify my resume"* / *"STARify [project name]"* |
| `interview-prep` | Behavioral coverage audit, mock interviews, company briefs, and round-specific cheat-sheets. Pulls from your STAR files. | *"Build a cheat-sheet for the Pinecone HM call"* / *"Mock me on a behavioral round"* |
| `daily-summary` | EOD log of artifacts touched, open loops, patterns, and next steps. | *"Wrap up the day"* / *"EOD summary"* |
| `morning` | AM briefing: yesterday's open items + stale roles (>7 days untouched) + one suggested first move. | *"/morning"* / *"What's on my plate today?"* |

Every skill is grounded in your personal files under `$PERSONAL/career/`. Fill those in once and the advice stops being generic.

## Quick start

```bash
# 1. Clone and enter the repo
git clone <repo-url> career-agent && cd career-agent

# 2. Bootstrap your private data directory (sibling of the repo)
PERSONAL="$(dirname "$(pwd)")/career-agent-personal-docs"
mkdir -p "$PERSONAL/career" "$PERSONAL/applications"
cp career/impact-doc.template.md    "$PERSONAL/career/impact-doc.md"
cp career/goals.template.md         "$PERSONAL/career/goals.md"
cp career/brag-doc.template.md      "$PERSONAL/career/brag-doc.md"
cp career/personal-info.template.md "$PERSONAL/career/personal-info.md"

# 3. Install the Python deps
pip install python-docx reportlab requests

# 4. Open in Claude Code
claude
```

Then run `/onboard` inside Claude Code. It bootstraps `$PERSONAL` for you, checks prerequisites, and walks you through filling in `impact-doc.md` (most important), `goals.md`, `brag-doc.md`, and `personal-info.md`. Steps 2 and 3 above can be skipped if you let `/onboard` do them, but they're listed in case you want to do it manually.

If you already know your way around, run `/help` any time to see the full toolbox or learn how a specific skill works.

You also need [Claude Code](https://claude.ai/code) installed and authenticated.

## Where your personal data lives

Your private career data is stored **outside this repo** in a sibling directory called `career-agent-personal-docs/`. The repo carries only code, templates, and instructions, never personal content.

```
Coding/
  career-agent/                       # this repo (committed to git)
  career-agent-personal-docs/         # your private data (NOT in git, sibling of repo)
```

Throughout the skills and `CLAUDE.md`, `$PERSONAL` refers to the absolute path of that sibling directory. Skills resolve it dynamically from the git root, so it works from the main checkout and from any worktree without hard-coding.

## How to use job-analyzer

Use this when you want a grounded read on whether a single posting is worth pursuing.

1. Paste the Job Description text (or a URL, if it's a site Claude can fetch). One posting per request.
2. Ask: *"Worth pursuing?"* or *"How do I fit?"*
3. Claude returns: skills match, level alignment, gaps, comp signal, and a recommendation.
4. The Job Description, analysis, and any free-form notes get persisted to `$PERSONAL/applications/<company>/<role-slug>/role.md`.

Feeds directly into `resume-builder` and `cover-letter-builder`.

## How to use coding-prep

Coding interview practice in your preferred language. Shared problem bank in `coding-bank/problems/`; private attempts in `$PERSONAL/career/coding-log/`.

On first use, Claude asks which language you want to practice in (TypeScript, Python, Go, Java, C++, Rust, etc.) and stores it in `$PERSONAL/career/coding-log/preferences.md`. Change it any time with *"switch my coding language to Python"*.

1. **Add a problem.** Paste the problem details. Claude saves to `coding-bank/problems/<slug>.md`.
2. **Practice.** *"Let's practice two-sum"* or *"surprise me from weak spots"*. Choose **tutoring** (hint ladder) or **evaluation only** (you solve, Claude grades).
3. **Mock me.** Timed 45 min, no hints, follow-up variant, hire/no-hire grade at the end.
4. **Query weak spots.** *"What should I redo today?"* — Claude reads your attempt log and surfaces failed or stale problems.

Attempts append to `$PERSONAL/career/coding-log/attempts.jsonl`, with per-problem notes in `by-problem/<slug>.md`.

## How to use interview-prep

Behavioral interview workflow. Pairs with `star-stories`: STAR files in `$PERSONAL/career/star/` are the source material, interview-prep is the consumer.

**Prerequisite:** at least a few STAR files in `$PERSONAL/career/star/`. Build them with *"STARify my resume"* (full portfolio) or *"STARify [project name]"* (single project).

Four modes, triggered by what you say:

1. **Coverage audit.** *"Where are my story gaps?"* — Read-only. Reports which behavioral competencies (leadership, ambiguity, failure, conflict, etc.) have strong / thin / no coverage. Suggests which projects to STARify next.
2. **Mock interview.** *"Mock me on a Pinecone behavioral round"* — Strict or coaching mode, one question at a time, evaluates structure/specificity/ownership/outcome, ends with a "stories to rehearse" list pointing at specific STAR files and angles. Transcript saved to `$PERSONAL/applications/<company>/<role>/interview-prep/`.
3. **Company brief.** *"Research Pinecone before tomorrow's call"* — Synthesized one-page brief on the company plus recommended stories mapped to the round structure. Saved to `$PERSONAL/applications/<company>/<role>/brief.md`.
4. **Cheat-sheet.** *"Build a cheat-sheet for the Pinecone HM call"* — Round-specific prep doc (opening pitch, lead stories with file links, predicted question table, gap framing, questions to ask, listen-fors). Templates differ for recruiter / HM / tech-screen / system-design / onsite-behavioral / cross-team-collab. Saved to `$PERSONAL/applications/<company>/<role>/<round>-cheat-sheet.md`.

interview-prep does *not* create new STAR files. If it needs a story you don't have, it tells you to run `/star-stories <project>` and resume.

## File layout

```
career-agent/                              # this repo
  career/                                  # personal-doc templates
  coding-bank/problems/                    # shared coding library
  .claude/skills/                          # skill definitions
  CLAUDE.md                                # full project instructions
  README.md

career-agent-personal-docs/                # sibling of repo, NOT in git
  career/                                  # impact doc, goals, brag doc, STAR files, daily logs, coding log
  applications/<company>/<role-slug>/      # per-role artifacts: role.md, resume, cover letter, cheat-sheets, briefs, interview notes
```

Full file layout, including which skill writes what, is in [CLAUDE.md](CLAUDE.md).

## Tips and tricks

A few things I've picked up running this workflow myself. Your mileage may vary.

1. **Open `career-agent-personal-docs/` in VS Code with a markdown preview extension** (e.g. [Markdown Preview Enhanced](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced)). You don't want to be squinting at raw markdown that Claude generated. Cleanly rendered docs are easier to study and handy to keep open during interview calls for quick reference.

2. **Don't pre-create application folders for every posting you look at.** I only ask Claude to create the `applications/<company>/<role>/` folder once I have a recruiter call scheduled. Otherwise you end up with hundreds of stale folders and lose signal.

3. **Use LeetCode as your coding environment, not Claude.** Solve the problem on LeetCode first, then paste both the problem and your solution into `coding-prep`. Treat Claude as the analysis and review layer, not the IDE.

4. **Dump interview notes immediately after the call, while it's fresh.** Take notes during the interview, then paste them into Claude for that role as soon as it ends. Claude updates the role's artifacts so your next round's prep automatically pulls in context from every previous round.

5. **Update `impact-doc.md` as wins happen, not when you're job searching.** Two-line entries when you ship something, get a comp adjustment, or run a project. By the time you actually need a tailored resume, the material is already there and quantified, instead of you trying to reconstruct numbers from six months ago.

6. **Run `/morning` daily even when you're not actively applying.** It surfaces stale roles and open loops in under a minute. Cheap to run, and the alternative is rediscovering you ghosted a recruiter two weeks ago.

7. **Don't trust LinkedIn or Indeed URL fetches.** They block behind login walls, and `job-analyzer` will fail or hallucinate. Paste the Job Description text directly.

8. **STARify projects right after they wrap, not the week before an onsite.** Details, peer names, and metrics decay fast. A 15-minute `/star-stories` session at project close pays back the first time you need it.

9. **Keep one master resume per career level, then tailor.** Build a single "staff-level engineer" resume once, then let `resume-builder` cut and rewrite from it per posting. Starting from scratch every time is wasted reps.

10. **This is my workflow, not the workflow.** If something here doesn't fit how you operate, fork the repo and refactor. The skills are deliberately small so they're easy to bend.

## Notes

- `job-analyzer` will try to fetch a Job Description from a URL, but LinkedIn and Indeed block automated fetches behind login/JS walls. When that happens, paste the Job Description text and the workflow continues.
- `role.md` files store the Job Description, fit analysis, and free-form notes. Tracking fields (stage, outcome, date_applied, referral, match_level) are optional: Claude mirrors them in the frontmatter if you mention them inline ("I applied today", "Alice referred me"), but won't prompt or invent.
- All skill outputs are plain markdown files you can edit by hand at any time.
- Because personal data lives in a sibling directory, it stays accessible from the main checkout and from any worktree with no symlink setup.

---

If you found the tool (or our collaboration) helpful, I'd appreciate a quick LinkedIn recommendation on my profile: [Link](https://www.linkedin.com/in/rishabh-modi-736a33149/). No pressure at all, but it would be a huge help.
