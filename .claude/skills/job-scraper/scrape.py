#!/usr/bin/env python3
"""
Scrape job postings from a list of URLs.

Usage:
    python scrape.py <run_dir> <url1> <url2> ...

For each URL:
  - Success → writes <run_dir>/raw/<n>-<slug>.txt with extracted JD text
  - Failure → writes <run_dir>/raw/<n>-<slug>.FAILED.txt with reason

Failures are expected for LinkedIn and other JS-heavy / login-walled sites.
The skill workflow handles failures by asking the user to paste text manually.
"""

import sys
import re
import os
from pathlib import Path
from urllib.parse import urlparse

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Missing dependencies. Install with: pip install requests beautifulsoup4 --break-system-packages")
    sys.exit(1)


USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)

# Sites known to block or require JS — fail fast so user pastes text
KNOWN_HARD_SITES = {"linkedin.com", "www.linkedin.com", "indeed.com", "www.indeed.com"}

# Tags whose text is almost certainly not JD content
NOISE_TAGS = {"script", "style", "nav", "header", "footer", "aside", "noscript"}


def slugify(text: str, max_len: int = 40) -> str:
    text = re.sub(r"[^a-z0-9]+", "-", text.lower())
    text = text.strip("-")
    return text[:max_len] or "posting"


def url_slug(url: str) -> str:
    parsed = urlparse(url)
    host = parsed.netloc.replace("www.", "")
    path = parsed.path.strip("/").replace("/", "-")
    return slugify(f"{host}-{path}")


def fetch(url: str, timeout: int = 15) -> tuple[bool, str]:
    """Return (success, text_or_error)."""
    host = urlparse(url).netloc.lower()
    if host in KNOWN_HARD_SITES:
        return False, f"Known hard site ({host}). Paste JD text manually."

    try:
        resp = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=timeout)
    except requests.RequestException as e:
        return False, f"Request failed: {e}"

    if resp.status_code != 200:
        return False, f"HTTP {resp.status_code}"

    if len(resp.text) < 500:
        return False, "Response too short — likely a redirect or login wall."

    return True, resp.text


def extract_text(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup.find_all(NOISE_TAGS):
        tag.decompose()

    # Prefer <main> or <article> if present
    container = soup.find("main") or soup.find("article") or soup.body or soup
    text = container.get_text(separator="\n")

    # Collapse whitespace
    lines = [line.strip() for line in text.splitlines()]
    lines = [line for line in lines if line]
    return "\n".join(lines)


def looks_like_jd(text: str) -> bool:
    """Sanity check: does this look like a job posting?"""
    if len(text) < 300:
        return False
    keywords = ["responsibilities", "qualifications", "requirements", "experience",
                "you will", "we are looking", "about the role", "about the team",
                "what you'll do", "what you'll bring", "skills"]
    text_lower = text.lower()
    return sum(1 for kw in keywords if kw in text_lower) >= 2


def write_file(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    run_dir = Path(sys.argv[1])
    urls = sys.argv[2:]
    raw_dir = run_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    print(f"Scraping {len(urls)} URLs → {raw_dir}\n")

    results = []
    for i, url in enumerate(urls, 1):
        slug = url_slug(url)
        ok, payload = fetch(url)

        if ok:
            text = extract_text(payload)
            if looks_like_jd(text):
                path = raw_dir / f"{i}-{slug}.txt"
                content = f"URL: {url}\n\n---\n\n{text}"
                write_file(path, content)
                print(f"  [{i}] OK    {url}")
                results.append(("ok", url, path))
            else:
                path = raw_dir / f"{i}-{slug}.FAILED.txt"
                content = (
                    f"URL: {url}\n\n"
                    f"REASON: Scraped successfully but content doesn't look like a JD. "
                    f"Paste the JD text into this file (replace this content) and rename to remove .FAILED.\n\n"
                    f"---\nExtracted text (first 2000 chars):\n\n{text[:2000]}"
                )
                write_file(path, content)
                print(f"  [{i}] WEAK  {url} — content doesn't look like a JD")
                results.append(("weak", url, path))
        else:
            path = raw_dir / f"{i}-{slug}.FAILED.txt"
            content = (
                f"URL: {url}\n\n"
                f"REASON: {payload}\n\n"
                f"Paste the JD text below (replace this content) and rename to remove .FAILED.\n"
            )
            write_file(path, content)
            print(f"  [{i}] FAIL  {url} — {payload}")
            results.append(("fail", url, path))

    failures = [r for r in results if r[0] != "ok"]
    print(f"\n{len(results) - len(failures)} succeeded, {len(failures)} failed/weak.\n")

    if failures:
        print("Failures need manual paste. Files created:")
        for status, url, path in failures:
            print(f"  {path}")
        sys.exit(2)  # Non-zero so the skill workflow knows to handle paste step


if __name__ == "__main__":
    main()
