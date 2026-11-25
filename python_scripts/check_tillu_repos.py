import urllib.request
import json

url = "https://api.github.com/users/baba-tillu0093/repos?per_page=100&sort=updated"
headers = {"User-Agent": "AntigravityAgent"}

req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req) as resp:
        repos = json.loads(resp.read().decode('utf-8'))
        print(f"Found {len(repos)} public repos for baba-tillu0093:")
        for r in repos:
            print(" -", r.get("name"), "url:", r.get("html_url"), "branch:", r.get("default_branch"))
except Exception as e:
    print("Error querying baba-tillu0093:", e)
