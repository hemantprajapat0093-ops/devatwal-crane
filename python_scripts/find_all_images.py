import re

with open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\index.html", "r", encoding="utf-8") as f:
    html = f.read()

with open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\css\style.css", "r", encoding="utf-8") as f:
    css = f.read()

print("HTML image references:")
for m in re.finditer(r'<img[^>]+src=["\']([^"\']+)["\']', html):
    print(" -", m.group(1))

print("\nCSS url references:")
for m in re.finditer(r'url\(["\']?([^"\'\)]+)["\']?\)', css):
    print(" -", m.group(1))
