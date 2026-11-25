import subprocess
import urllib.request
import json

# Get credential from git credential fill
p = subprocess.Popen(['git', 'credential', 'fill'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
out, err = p.communicate(input='protocol=https\nhost=github.com\n\n')

username = None
token = None
for line in out.splitlines():
    if line.startswith('username='):
        username = line.split('=', 1)[1]
    elif line.startswith('password='):
        token = line.split('=', 1)[1]

print("Authenticated User:", username)

if token:
    headers = {
        "Authorization": f"Bearer {token}",
        "User-Agent": "AntigravityAgent",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # 1. Query user's repos
    try:
        req = urllib.request.Request("https://api.github.com/user/repos?per_page=100&sort=updated", headers=headers)
        with urllib.request.urlopen(req) as resp:
            repos = json.loads(resp.read().decode('utf-8'))
            print(f"Found {len(repos)} repositories for authenticated user:")
            for r in repos:
                name = r.get('name')
                full_name = r.get('full_name')
                clone_url = r.get('clone_url')
                default_branch = r.get('default_branch')
                print(f" - {full_name} (branch: {default_branch}, url: {clone_url})")
    except Exception as e:
        print("Error fetching authenticated repos:", e)
