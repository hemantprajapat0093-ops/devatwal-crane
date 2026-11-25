import os
import urllib.request
import json

token = os.environ.get("GITHUB_TOKEN", "REDACTED_TOKEN")
headers = {
    "Authorization": f"Bearer {token}",
    "User-Agent": "AntigravityAgent",
    "Accept": "application/vnd.github.v3+json"
}

req = urllib.request.Request("https://api.github.com/user", headers=headers)
try:
    with urllib.request.urlopen(req) as resp:
        user_info = json.loads(resp.read().decode('utf-8'))
        print("Token belongs to user:", user_info.get("login"))
except Exception as e:
    print("Error verifying token:", e)
