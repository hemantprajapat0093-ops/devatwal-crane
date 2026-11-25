import os, re

files = [
    r"C:\Users\heman\Desktop\devatwal-crane-service\public\index.html",
    r"C:\Users\heman\Desktop\devatwal-crane-service\public\js\app.js",
    r"C:\Users\heman\Desktop\devatwal-crane-service\server.js"
]

patterns = ["Satyapal", "Maman", "Vishnudat", "9414333328", "9950233073", "800372", "982842", "corner-dock-btn-maps", "riico", "Ghiloth"]

for path in files:
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        print(f"=== {os.path.basename(path)} ({len(lines)} lines) ===")
        for i, line in enumerate(lines, 1):
            for pat in ["Satyapal", "Maman", "Vishnudat", "9950233073", "corner-dock-btn-maps"]:
                if pat.lower() in line.lower():
                    print(f"L{i}: {line.strip()[:100]}")
                    break
