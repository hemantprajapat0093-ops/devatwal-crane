import os

history_paths = [
    os.path.expanduser(r"~\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt"),
    os.path.expanduser(r"~/.bash_history"),
]

for p in history_paths:
    if os.path.exists(p):
        print(f"Reading {p}:")
        with open(p, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
        for line in lines[-100:]:
            if any(k in line.lower() for k in ["git", "github", "devatwal", "baba", "crane", "push", "remote"]):
                print("  ", line.strip())
