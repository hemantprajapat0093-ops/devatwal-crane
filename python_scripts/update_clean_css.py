with open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\css\style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Update dock button glows to avoid color bleeding in the corner
old_dock_css = """.corner-dock-btn-phone {
  background: linear-gradient(135deg, #10b981, #059669);
  box-shadow: 0 0 25px rgba(16, 185, 129, 0.75), 0 8px 30px rgba(0, 0, 0, 0.7);
  border: 2px solid #34d399;
}
.corner-dock-btn-phone:hover {
  box-shadow: 0 0 40px rgba(16, 185, 129, 0.95), 0 12px 35px rgba(0, 0, 0, 0.85);
}

.corner-dock-btn-email {
  background: linear-gradient(135deg, #fbbf24, #f59e0b);
  box-shadow: 0 0 28px rgba(245, 158, 11, 0.85), 0 8px 30px rgba(0, 0, 0, 0.7);
  border: 2px solid #fef08a;
  color: #000;
}
.corner-dock-btn-email:hover {
  box-shadow: 0 0 45px rgba(245, 158, 11, 1), 0 12px 35px rgba(0, 0, 0, 0.85);
}

.corner-dock-btn-wa {
  background: linear-gradient(135deg, #16a34a, #15803d);
  box-shadow: 0 0 25px rgba(22, 163, 74, 0.75), 0 8px 30px rgba(0, 0, 0, 0.7);
  border: 2px solid #4ade80;
}
.corner-dock-btn-wa:hover {
  box-shadow: 0 0 40px rgba(22, 163, 74, 0.95), 0 12px 35px rgba(0, 0, 0, 0.85);
}"""

new_dock_css = """.corner-dock-btn-phone {
  background: linear-gradient(135deg, #10b981, #059669);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.7);
  border: 2px solid #34d399;
}
.corner-dock-btn-phone:hover {
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.85);
  transform: scale(1.1);
}

.corner-dock-btn-email {
  background: linear-gradient(135deg, #fbbf24, #f59e0b);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.7);
  border: 2px solid #fef08a;
  color: #000;
}
.corner-dock-btn-email:hover {
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.85);
  transform: scale(1.1);
}

.corner-dock-btn-wa {
  background: linear-gradient(135deg, #16a34a, #15803d);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.7);
  border: 2px solid #4ade80;
}
.corner-dock-btn-wa:hover {
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.85);
  transform: scale(1.1);
}"""

if old_dock_css in css:
    css = css.replace(old_dock_css, new_dock_css)
    print("Replaced dock CSS to eliminate green halos!")
else:
    print("Dock CSS exact block not matched, searching...")

# Update .hero-exact-banner
old_hero = """.hero-exact-banner {
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

new_hero = """.hero-exact-banner {
  position: relative;
  min-height: 660px;
  background-color: #070d18;
  background-image: 
    linear-gradient(to right, #070d18 0%, #070d18 36%, rgba(7, 13, 24, 0.8) 54%, transparent 74%),
    url('/images/hero_perfect_clean_backdrop.jpg');
  background-position: right center;
  background-size: cover;
  background-repeat: no-repeat;
}"""

if old_hero in css:
    css = css.replace(old_hero, new_hero)
    print("Replaced .hero-exact-banner in style.css")

with open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\css\style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Saved updated style.css!")
