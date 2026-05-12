---
name: job-scraper
description: Scrape multiple job posting URLs, cluster them by role archetype, and generate a tailored resume per cluster. Use when the user provides 2+ job posting URLs and wants batch analysis plus per-cluster resumes. For a single posting, use job-analyzer instead.
---

# Job Requirement Scraper

## When to use
The user provides 2+ job posting URLs (or pastes Job Description text for multiple roles) and wants to:
- Compare requirements across postings
- Group similar roles together
- Generate a tailored resume per group

For a single posting, use `job-analyzer`.

## Workflow

### 1. Collect inputs
Accept URLs as a list, a file, or pasted text. Confirm the full list back to the user before scraping — typos or wrong tabs are common.

### 2. Set up the run directory
```bash
mkdir -p .claude/skills/job-scraper/output/<YYYY-MM-DD>/{raw,resumes}
```
Use today's date. If a directory for today already exists, append `-2`, `-3`, etc.

### 3. Scrape
Run:
```bash
python .claude/skills/job-scraper/scrape.py <run_dir> <url1> <url2> ...
```

The script writes one file per URL to `<run_dir>/raw/`. For each URL it either:
- Succeeds → writes `<n>-<slug>.txt` with extracted Job Description text
- Fails → writes `<n>-<slug>.FAILED.txt` with the URL and reason

For every failed URL, **stop and ask the user to paste the Job Description text**. Save their pasted text to `<run_dir>/raw/<n>-<slug>.txt` (replacing the .FAILED file). Don't proceed to parsing until every posting has content.

### 4. Parse and normalize
Run:
```bash
python .claude/skills/job-scraper/parse.py <run_dir>
```

This reads every `.txt` file in `raw/` and writes `<run_dir>/parsed.json` — but the parsing itself is done by *you*, not the script. The script just orchestrates: it prints each raw file and expects you to fill in a structured record per posting:

```json
{
  "id": "1",
  "source_file": "1-stripe-staff-eng.txt",
  "url": "...",
  "company": "...",
  "title": "...",
  "level": "Senior | Staff | Principal | ...",
  "required_skills": ["..."],
  "nice_to_have": ["..."],
  "responsibilities": ["..."],
  "scope_signals": ["..."],
  "comp_range": "...",
  "location": "...",
  "remote_policy": "...",
  "red_flags": ["..."],
  "green_flags": ["..."]
}
```

Be specific in `scope_signals` — capture concrete things like "owns payments platform serving 100M req/day" rather than "large scale."

### 5. Cluster
Read all parsed records. Propose buckets based on:
- **Role archetype** (backend, full-stack, platform/infra, ML/AI, developer tools, etc.)
- **Level and scope** (senior IC, staff IC, tech lead, EM, etc.)
- **Company stage** (early startup, scaleup, public/big tech)
- **Tech stack overlap**
- **Domain** (payments, infra, devtools, data, etc.)

Write `<run_dir>/buckets.md` with:
- Each bucket: name, postings in it (by id + company), common requirements, archetype description
- Short rationale for grouping
- Singletons (postings that don't cluster) — list separately

**Stop and confirm buckets with the user.** They will have opinions. Ask:
- Any buckets to merge or split?
- Any singletons to absorb into a bucket?
- Any to drop entirely?

### 6. Analyze each confirmed bucket
For each bucket, append to `buckets.md`:
- Top 10 most common keywords/skills across the bucket's postings (count + which postings)
- Common scope and impact signals
- Map to my background (from `career/impact-doc.md`):
  - **Strengths** for this archetype
  - **Gaps**
  - **Stretch areas** (have adjacent experience but not direct)
- Recommended resume emphasis: what to lead with, what to cut, what to reframe

### 7. Generate tailored resumes
For each bucket, invoke the `resume-builder` skill with the bucket's analysis as the target profile. Output to:
```
<run_dir>/resumes/<bucket-slug>/
  resume.md
  resume.docx
  resume.pdf
```

### 8. Final summary
End the run with:
- N postings scraped, M buckets created, K singletons
- Best-fit bucket and why (most strengths, fewest gaps)
- Stretch buckets and what's missing
- All files produced (list paths)

## Anti-patterns
- Don't silently skip failed scrapes — always surface them and get the text.
- Don't over-cluster. 5 similar postings = 1 bucket, not 3.
- Don't keyword-stuff the resumes. Each variant should be honestly tailored, not stuffed with the bucket's vocabulary.
- Don't cite a posting as supporting a keyword without checking — be specific about which postings drove which conclusions.
