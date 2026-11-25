path = r"C:\Users\heman\Desktop\devatwal-crane-service\devatwal-crane\public\js\crane3d.js"
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines[60:160]):
    print(f"{i+61}: {line}", end="")
