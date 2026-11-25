with open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\index.html", "r", encoding="utf-8") as f:
    html = f.read()

print("Original HTML length:", len(html))

# Let's verify key markers in HTML
markers = [
    'class="fixed-floating-corner-dock"',
    '<header class="sticky top-0 z-40',
    '<section id="hero"',
    '<section id="booking-section"',
    '<iframe',
    '<footer>'
]

for m in markers:
    print(f"Marker '{m}': {'FOUND' if m in html else 'NOT FOUND'}")
