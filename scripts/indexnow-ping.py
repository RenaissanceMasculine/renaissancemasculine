#!/usr/bin/env python3
"""Ping IndexNow (Bing, Yandex, Seznam...) with the site's sitemap URLs.

Usage: python3 scripts/indexnow-ping.py <key> [sitemap_url]

- Fetches the live sitemap and submits ALL URLs in one POST to
  api.indexnow.org (collective endpoint: Bing, Yandex, Seznam).
- Small site: re-submitting unchanged URLs is tolerated by the API;
  no local state/cache needed.
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
        print("usage: indexnow-ping.py <key> [sitemap_url]")
        return 0
    key = sys.argv[1].strip()
    sitemap_url = sys.argv[2] if len(sys.argv) > 2 else "https://renaissancemasculine.com/sitemap.xml"

    sitemap = fetch(sitemap_url)
    import re
    urls = re.findall(r"<loc>([^<]+)</loc>", sitemap)

    payload = {
        "host": "renaissancemasculine.com",
        "key": key,
        "keyLocation": f"https://renaissancemasculine.com/{key}.txt",
        "urlList": urls,
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
            print(f"IndexNow: HTTP {r.status} - submitted {len(urls)} URL(s). Response: {body[:200]}")
    except Exception as e:
        print(f"IndexNow ping failed (non-blocking): {e}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
