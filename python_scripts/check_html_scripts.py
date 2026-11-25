import os
import re

html_path = r"C:\Users\heman\Desktop\devatwal-crane-service\devatwal-crane\public\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

scripts = re.findall(r'<script[\s\S]*?</script>', html)
print(f"Total <script> tags in index.html: {len(scripts)}")
for i, s in enumerate(scripts):
    first_line = s.split('\n')[0]
    length = len(s)
    has_three = "three" in s.lower()
    has_raf = "requestanimationframe" in s.lower()
    has_orbit = "orbitcontrols" in s.lower()
    print(f"Script #{i+1} ({length} chars): {first_line[:60]}... three={has_three}, raf={has_raf}, orbit={has_orbit}")
