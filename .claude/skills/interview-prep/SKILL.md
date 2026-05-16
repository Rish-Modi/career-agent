---
name: interview-prep
description: Behavioral interview preparation, STAR story development, mock interviews, and company research. Use for any non-coding interview prep — behavioral, leadership, system design framing, recruiter screens, hiring manager conversations.
---

# Interview Prep

## When to use
- I'm preparing for a behavioral, leadership, or hiring manager round
- I want to build or refine STAR stories from my career
- I want to run a mock interview
- I need to research a company before an interview

For coding interviews, use `coding-prep`.

## Modes

### Mode 1: Story bank development

**Goal:** turn my career experiences into a flexible library of STAR stories.

Workflow:
1. Read `$PERSONAL/career/impact-doc.md` and `$PERSONAL/career/story-bank.json` if it exists. `$PERSONAL` is the personal-docs sibling directory defined in `CLAUDE.md`; resolve it once at the start of the session.
2. Propose 8–12 story candidates covering these competencies:
   - Leadership / influence without authority
   - Conflict (peer, manager, cross-team)
   - Ambiguity / undefined problems
   - Failure and recovery
   - Highest-impact project
   - Technical disagreement
   - Mentorship
   - Difficult tradeoff (scope, quality, time)
   - Cross-functional partnership
   - Driving change in a large org
3. For each, draft in STAR format:
   - **Situation** (2–3 sentences, concrete context)
   - **Task** (what specifically was on me)
   - **Action** (what I did — first person, specific, decision-driven)
   - **Result** (quantified outcome + what I learned)
4. Tag each story with the competencies it maps to. Good stories cover 3+ competencies.
5. Save to `$PERSONAL/career/story-bank.json` as a structured file so we can extend it over time.

Push back when a story is weak: "Action" too vague, "Result" missing numbers, or the story is really about the team rather than me.

### Mode 2: Mock interview

**Setup:**
- Confirm company, role, interview type, interviewer (IC peer / hiring manager / bar raiser / etc.), and time budget
- Confirm: do I want strict mode (you stay in character, feedback only at the end) or coaching mode (feedback after each answer)?

**During:**
- Ask one question at a time. Don't telegraph what's coming.
- For each answer, evaluate on:
  - **Structure**: did I use STAR? Was it easy to follow?
  - **Specificity**: real details, named systems, real numbers — or vague generalities?
  - **Ownership**: "I" vs. "we" — did my contribution come through?
  - **Outcome**: quantified impact?
  - **Length**: 2–4 minutes ideal; flag if I rambled or under-delivered
- In coaching mode, give pointed feedback (2–3 specific notes) then move on. Don't lecture.

**End:**
- Overall assessment
- Top 2 strengths and top 2 things to fix before the real interview
- Specific stories that landed and which ones to rework

### Mode 3: Company / role research

When I name a company and an upcoming interview:
- Search for: recent news (last 6 months), product launches, financial signals, leadership changes, engineering blog posts, glassdoor patterns
- Surface: known interview format, leadership principles or values they evaluate on, likely interviewers if I share names
- Generate likely questions based on the role + company patterns
- Propose which of my stories map best to their likely competencies

Don't dump search results — synthesize. End with a one-page brief.

## Output discipline
- Story bank goes in `$PERSONAL/career/story-bank.json`, structured.
- Mock interview transcripts and feedback go in `$PERSONAL/applications/<company>/<role>/interview-prep/`.
- Company research goes in `$PERSONAL/applications/<company>/<role>/brief.md`.

## Anti-patterns
- Don't write stories *for* me in first person without confirming the details. Draft, mark assumptions, ask me to verify.
- Don't grade everything generously. If an answer was weak, say it was weak and why.
- Don't recycle the same 2 stories across every question — the point of the bank is range.
