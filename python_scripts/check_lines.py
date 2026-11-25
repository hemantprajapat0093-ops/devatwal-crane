with open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, l in enumerate(lines[800:1120], 801):
    if any(k in l for k in ["Satyapal", "Maman", "Vishnudat", "Dharminder", "9414", "9950", "8003", "9828"]):
        print(f"L{i}: {l.strip()}")
