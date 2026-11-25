with open(r"C:\Users\heman\Desktop\devatwal-crane-service\devatwal-crane\public\css\style.css", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, l in enumerate(lines[:60]):
    print(f"{i+1}: {l}", end="")
