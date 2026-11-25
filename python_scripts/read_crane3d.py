path = r"C:\Users\heman\Desktop\devatwal-crane-service\devatwal-crane\public\js\crane3d.js"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

print("crane3d.js length:", len(text))
for i, line in enumerate(text.splitlines()[:60]):
    print(f"{i+1}: {line}")
