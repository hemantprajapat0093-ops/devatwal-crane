import os
import shutil

src_root = r"C:\Users\heman\Desktop\devatwal-crane-service"
dst_root = r"C:\Users\heman\Desktop\devatwal-crane-service\devatwal-crane"

# Sync files
files_to_copy = [
    "server.js",
    "package.json",
    "package-lock.json",
    "docker-compose.yml",
    "Dockerfile",
    ".dockerignore",
    "README.md",
]

for f in files_to_copy:
    src_f = os.path.join(src_root, f)
    dst_f = os.path.join(dst_root, f)
    if os.path.exists(src_f):
        shutil.copy2(src_f, dst_f)
        print("Copied", f)

# Sync public/
src_pub = os.path.join(src_root, "public")
dst_pub = os.path.join(dst_root, "public")
shutil.copytree(src_pub, dst_pub, dirs_exist_ok=True)
print("Synced public/ directory")

# Sync data/
src_data = os.path.join(src_root, "data")
dst_data = os.path.join(dst_root, "data")
if os.path.exists(src_data):
    shutil.copytree(src_data, dst_data, dirs_exist_ok=True)
    print("Synced data/ directory")

print("All files synchronized into devatwal-crane!")
