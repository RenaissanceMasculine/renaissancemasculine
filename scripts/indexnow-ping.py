#!/usr/bin/env python3
"""Ping IndexNow (Bing, Yandex, Seznam...) with ONLY new/changed post URLs.

Usage (in the deploy workflow):
    python3 scripts/indexnow-ping.py <key> [sitemap_url] [--git-diff <range>]

How it determines what to submit (no local state, nothing to keep in sync):
1. `git diff --name-only <range>` lists changed files since the previous push.
2. Only _posts/*.md filenames (slug = filename minus YYYY-MM-DD-) are kept.
3. The LIVE sitemap is fetched and filtered by slug suffix match — URLs are
   never reconstructed from front matter (percent-encoding + category order
   make guessing unreliable); only sitemap-extracted URLs are ever submitted.
4. Changed posts absent from the sitemap (deleted posts) are ignored.
5. No posts changed (CSS, assets, workflow edits...) -> no ping at all.

With no --git-diff argument (local manual run) the whole sitemap is submitted.
"""
import os
import re
import sys
import json
import subprocess
import urllib.request

HOST = "https://api.indexnow.org/indexnow"
SITEMAP_DEFAULT = "https://renaissancemasculine.com/sitemap.xml"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "rm-indexnow/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", errors="replace")


def slug_of(fname):
    base = os.path.basename(fname)
    if not base.endswith(".md"):
        return None
    parts = base.split("-", 3)
    if len(parts) < 4 or not re.match(r"^\d{4}-\d{2}-\d{2}$", "-".join(parts[:3])):
        return None  # not a Jekyll dated post
    return parts[3][:-3].replace(" ", "-").casefold()


def changed_slugs(git_range):
    out = subprocess.run(
        ["git", "diff", "--name-only", git_range, "--", "_posts/"],
        capture_output=True, text=True, check=True,
    ).stdout
    return {s for s in (slug_of(f) for f in out.splitlines()) if s}


def main():
    args = sys.argv[1:]
    if not args:
        print("usage: indexnow-ping.py <key> [sitemap_url] [--git-diff <range>]")
        return 1
    key = args.pop(0).strip()
    sitemap_url = SITEMAP_DEFAULT
    git_range = None
    if args and not args[0].startswith("--"):
        sitemap_url = args.pop(0)
    if "--git-diff" in args:
        git_range = args[args.index("--git-diff") + 1]

    sitemap = fetch(sitemap_url)
    urls = re.findall(r"<loc>([^<]+)</loc>", sitemap)

    if git_range:
        slugs = changed_slugs(git_range)
        if not slugs:
            print("IndexNow: no posts changed - skipping ping.")
            return 0
        to_submit = [u for u in urls if u.rstrip("/").rpartition("/")[2].casefold() in slugs]
        missing = slugs - {u.rstrip("/").rpartition("/")[2].casefold() for u in to_submit}
        if missing:
            print(f"IndexNow: note - changed slugs not in sitemap (ignored): {sorted(missing)}")
    else:
        to_submit = urls  # manual mode: submit everything

    if not to_submit:
        print("IndexNow: nothing to submit.")
        return 0

    payload = {
        "host": "renaissancemasculine.com",
        "key": key,
        "keyLocation": f"https://renaissancemasculine.com/{key}.txt",
        "urlList": to_submit,
    }
    req = urllib.request.Request(
        HOST,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            body = r.read().decode("utf-8", errors="replace")
            print(f"IndexNow: HTTP {r.status} - submitted {len(to_submit)} URL(s): {to_submit}")
    except Exception as e:
        print(f"IndexNow ping failed (non-blocking): {e}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
