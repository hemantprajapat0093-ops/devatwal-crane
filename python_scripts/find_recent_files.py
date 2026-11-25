import os
import time

now = time.time()
cutoff = now - 3600 # Last 1 hour

found = []
search_dirs = [
    r"C:\Users\heman\Desktop",
    r"C:\Users\heman\Downloads",
    r"C:\Users\heman\Documents",
    r"C:\Users\heman",
]

for sdir in search_dirs:
    for root, dirs, files in os.walk(sdir):
        # Skip node_modules and .git
        if "node_modules" in root or ".git" in root or "AppData" in root:
            continue
        for f in files:
            p = os.path.join(root, f)
            try:
                mtime = os.path.getmtime(p)
                if mtime > cutoff:
                    found.append((mtime, p))
            except Exception:
                pass

found.sort(reverse=True)
print(f"Files modified/created in the last hour ({len(found)} total):")
for t, p in found[:30]:
    print(f" - {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t))}: {p}")
