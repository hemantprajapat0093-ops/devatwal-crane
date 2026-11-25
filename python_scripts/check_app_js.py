with open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\js\app.js", "r", encoding="utf-8") as f:
    text = f.read()

print("Length of app.js:", len(text))
print("Contains hero references?:", "hero" in text.lower())
