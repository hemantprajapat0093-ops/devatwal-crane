import os
import re

root = r"C:\Users\heman\Desktop\devatwal-crane-service\devatwal-crane"
app_js_path = os.path.join(root, "public", "js", "app.js")
css_path = os.path.join(root, "public", "css", "style.css")
html_path = os.path.join(root, "public", "index.html")

with open(app_js_path, "r", encoding="utf-8") as f:
    js_text = f.read()

with open(css_path, "r", encoding="utf-8") as f:
    css_text = f.read()

with open(html_path, "r", encoding="utf-8") as f:
    html_text = f.read()

print("=== JS INSPECTION ===")
scroll_matches = [line for line in js_text.splitlines() if "scroll" in line.lower() and "addeventlistener" in line.lower()]
print("Scroll event listeners:", scroll_matches)

raf_matches = [line for line in js_text.splitlines() if "requestanimationframe" in line.lower()]
print("RAF matches count:", len(raf_matches))
for r in raf_matches:
    print("  RAF:", r.strip())

# Check touch event listeners
touch_matches = [line for line in js_text.splitlines() if "touch" in line.lower()]
print("Touch mentions:", len(touch_matches))

# Check Three.js initialization and controls
print("Three.js references in JS:", "three" in js_text.lower(), "OrbitControls:", "orbitcontrols" in js_text.lower())

print("\n=== CSS INSPECTION ===")
backdrop_matches = [line for line in css_text.splitlines() if "backdrop-filter" in line]
print(f"backdrop-filter count: {len(backdrop_matches)}")

blur_matches = [line for line in css_text.splitlines() if "filter:" in line and "blur" in line]
print(f"filter: blur count: {len(blur_matches)}")

will_change = [line for line in css_text.splitlines() if "will-change" in line]
print(f"will-change count: {len(will_change)}")
