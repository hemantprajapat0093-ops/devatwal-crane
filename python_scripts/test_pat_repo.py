import os
import urllib.request
import json

token = os.environ.get("GITHUB_TOKEN", "REDACTED_TOKEN")
headers = {
    "Authorization": f"Bearer {token}",
    "User-Agent": "AntigravityAgent",
    "Accept": "application/vnd.github.v3+json"
}

req = urllib.request.Request("https://api.github.com/repos/hemantprajapat0093-ops/devatwal-crane", headers=headers)
try:
    with urllib.request.urlopen(req) as resp:
        repo_info = json.loads(resp.read().decode('utf-8'))
        print("Repo found!", repo_info.get("full_name"), "private:", repo_info.get("private"))
except Exception as e:
    print("Error querying repo with token:", e)
