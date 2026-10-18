#!/usr/bin/env python3
"""Ping IndexNow (Bing, Yandex, Seznam...) with changed URLs after a deploy.

Usage: python3 scripts/indexnow-ping.py <key> [sitemap_url]

- Fetches the live sitemap.
- Optionally diffs against a cached 'previous' sitemap file to submit only NEW URLs.
- Sends URLs in one POST to api.indexnow.org (collective endpoint: Bing, Yandex, Seznam).
- Never fails the build: exit 0 warnings on errors, exit 1 only if strictly asked (not used).
"""
import sys
import json
import urllib.request

HOST = "https://api.indexnow.org/indexnow"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "rm-indexnow/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", errors="replace")


def main():
    if len(sys.argv) < 2:
        print("usage: indexnow-ping.py <key> [sitemap_url] [--before <file>]")
        return 0
    key = sys.argv[1].strip()
    sitemap_url = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith("--") else "https://renaissancemasculine.com/sitemap.xml"

    before = None
    if "--before" in sys.argv:
        before_file = sys.argv[sys.argv.index("--before") + 1]
        before = set(l.strip() for l in open(before_file) if l.strip())

    sitemap = fetch(sitemap_url)
    import re
    urls = re.findall(r"<loc>([^<]+)</loc>", sitemap)
    # strip scheme-less normalization to compare sets cleanly
    present = set(u.rstrip("/") for u in urls)

    if before is not None:
        before_n = set(u.rstrip("/") for u in before)
        changed = sorted(present - before_n)
        if not changed:
            print("IndexNow: no new URLs to submit.")
            return 0
    else:
        changed = sorted(present)

    payload = {
        "host": "renaissancemasculine.com",
        "key": key,
        "keyLocation": f"https://renaissancemasculine.com/{key}.txt",
        "urlList": changed,
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
            print(f"IndexNow: HTTP {r.status} - submitted {len(changed)} URL(s). Response: {body[:200]}")
    except Exception as e:
        print(f"IndexNow ping failed (non-blocking): {e}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
