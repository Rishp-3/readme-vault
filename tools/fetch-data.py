#!/usr/bin/env python3
"""Fetch live GitHub data for user Rishp-3 and save a snapshot to tools/data/rishp-3.json.

Stdlib only. Optional GITHUB_TOKEN env var raises the rate limit.
Falls back to the manual dataset (marked "source": "manual-fallback") when the
network is unavailable or the API errors out.
"""
import json
import os
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "rishp-3.json")

MANUAL = {
    "source": "manual-fallback",
    "login": "Rishp-3",
    "name": "Rishabh",
    "bio": "Frontend Developer | React | JavaScript | Node.js | Learning Full Stack Development",
    "avatar_url": "https://avatars.githubusercontent.com/u/174471886?v=4",
    "public_repos": None,
    "followers": None,
    "following": None,
    "tagline": "Building clean and responsive UIs with React",
    "role": "Frontend Developer",
    "status": "Online & Operational",
    "hireable": True,
    "open_to": "collaborations and open source",
    "journey_since": 2023,
    "goal": "Full stack development",
    "os": "Arch Linux",
    "stack": ["HTML5", "CSS3", "JavaScript", "React", "Tailwind CSS", "Bootstrap",
              "Node.js", "Express.js", "Git", "GitHub", "Netlify", "C", "Java"],
    "repos": [
        {"name": "21-Frontend-Peroject", "description": "21 vanilla HTML/CSS/JS frontend projects", "language": "JavaScript", "stars": None},
        {"name": "Java-Project", "description": "Java learning - 27 modules", "language": "Java", "stars": None},
        {"name": "readme-vault", "description": "Profile README collection", "language": None, "stars": None},
        {"name": "Rishp-3", "description": "Profile README", "language": None, "stars": None},
    ],
    "top_languages": ["JavaScript", "Java", "HTML", "CSS", "React"],
    "links": {
        "linkedin": "https://linkedin.com/in/rishp3",
        "x": "https://x.com/rishp_3",
        "instagram": "https://instagram.com/rishp_3",
        "youtube": "https://youtube.com/@rishp3",
        "codepen": "https://codepen.io/Rishp-3",
        "medium": "https://medium.com/@rishp-3",
        "leetcode": "https://leetcode.com/u/rishp_3",
        "gfg": "https://geeksforgeeks.org/profile/rishp_3",
        "stackoverflow": "https://stackoverflow.com/users/32493179",
        "github": "https://github.com/Rishp-3",
    },
}


def get(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": "rishp-fetch-data",
        "Accept": "application/vnd.github+json",
    })
    tok = os.environ.get("GITHUB_TOKEN")
    if tok:
        req.add_header("Authorization", "Bearer " + tok)
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read().decode("utf-8"))


def main():
    try:
        user = get("https://api.github.com/users/Rishp-3")
        repos = get("https://api.github.com/users/Rishp-3/repos?per_page=100&sort=updated")
        lang_count = {}
        repo_list = []
        for r in repos:
            if r.get("language"):
                lang_count[r["language"]] = lang_count.get(r["language"], 0) + 1
            repo_list.append({
                "name": r["name"],
                "description": r.get("description"),
                "language": r.get("language"),
                "stars": r.get("stargazers_count"),
                "forks": r.get("forks_count"),
                "url": r.get("html_url"),
            })
        top5 = [k for k, _ in sorted(lang_count.items(), key=lambda kv: (-kv[1], kv[0]))[:5]]
        data = dict(MANUAL)
        data.update({
            "source": "live-api",
            "login": user["login"],
            "name": user.get("name") or "Rishabh",
            "bio": user.get("bio") or MANUAL["bio"],
            "avatar_url": user["avatar_url"],
            "public_repos": user.get("public_repos"),
            "followers": user.get("followers"),
            "following": user.get("following"),
            "hireable": bool(user.get("hireable")),
            "repos": repo_list,
            "featured_repos": ["21-Frontend-Peroject", "Java-Project", "readme-vault", "Rishp-3"],
            "top_languages": top5 or MANUAL["top_languages"],
        })
    except Exception as e:
        print(f"[fetch-data] network/API unavailable ({e}); using manual fallback", file=sys.stderr)
        data = dict(MANUAL)
        data["featured_repos"] = [r["name"] for r in MANUAL["repos"]]

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"[fetch-data] wrote {OUT} (source={data['source']})")


if __name__ == "__main__":
    main()
