with open(r"C:\Users\heman\Desktop\devatwal-crane-service\devatwal-crane\public\js\crane3d.js", "r", encoding="utf-8") as f:
    text = f.read()

# Let's inspect init3DCrane and animate
lines = text.splitlines()
print("Total lines in crane3d.js:", len(lines))
for i in range(18, 55):
    print(f"{i+1}: {lines[i]}")
print("---")
for i in range(395, 420):
    print(f"{i+1}: {lines[i]}")
