with open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\css\style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Add corner-dock-btn-maps if not present
if ".corner-dock-btn-maps" not in css:
    maps_btn_css = """
.corner-dock-btn-maps {
  background: linear-gradient(135deg, #2563eb, #1d4ed8);
  box-shadow: 0 0 25px rgba(37, 99, 235, 0.75), 0 8px 30px rgba(0, 0, 0, 0.7);
  border: 2px solid #60a5fa;
  color: #fff;
}
.corner-dock-btn-maps:hover {
  box-shadow: 0 0 40px rgba(37, 99, 235, 0.95), 0 12px 35px rgba(0, 0, 0, 0.85);
}
"""
    css = css.replace(".corner-dock-btn-wa:hover {", maps_btn_css + "\n.corner-dock-btn-wa:hover {")

# Update .hero-exact-banner to ensure pure midnight navy blend on left
old_hero_banner = """.hero-exact-banner {
  position: relative;
  min-height: 640px;
  background-color: #070d18;
  background-image: 
    linear-gradient(to right, rgba(7, 13, 24, 0.98) 0%, rgba(7, 13, 24, 0.88) 40%, rgba(7, 13, 24, 0.3) 65%, transparent 100%),
    url('/images/hero_perfect_clean_backdrop.jpg');
  background-position: right center;
  background-size: cover;
  background-repeat: no-repeat;
}"""

new_hero_banner = """.hero-exact-banner {
  position: relative;
  min-height: 660px;
  background-color: #070d18;
  background-image: 
    linear-gradient(to right, #070d18 0%, #070d18 40%, rgba(7, 13, 24, 0.85) 58%, transparent 80%),
    url('/images/hero_perfect_clean_backdrop.jpg');
  background-position: right center;
  background-size: cover;
  background-repeat: no-repeat;
}"""

if old_hero_banner in css:
    css = css.replace(old_hero_banner, new_hero_banner)
    print("Replaced .hero-exact-banner in style.css")
else:
    print(".hero-exact-banner exact block not matched, searching regex")

with open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\css\style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Updated style.css successfully!")
