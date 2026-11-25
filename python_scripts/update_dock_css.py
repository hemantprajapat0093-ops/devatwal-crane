with open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\css\style.css", "r", encoding="utf-8") as f:
    css = f.read()

target = """.corner-dock-btn-phone {
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

.corner-dock-btn-maps {
  background: linear-gradient(135deg, #2563eb, #1d4ed8);
  box-shadow: 0 0 25px rgba(37, 99, 235, 0.75), 0 8px 30px rgba(0, 0, 0, 0.7);
  border: 2px solid #60a5fa;
  color: #fff;
}
.corner-dock-btn-maps:hover {
  box-shadow: 0 0 40px rgba(37, 99, 235, 0.95), 0 12px 35px rgba(0, 0, 0, 0.85);
}

.corner-dock-btn-wa:hover {
  box-shadow: 0 0 40px rgba(22, 163, 74, 0.95), 0 12px 35px rgba(0, 0, 0, 0.85);
}"""

replacement = """.corner-dock-btn-phone {
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

if target in css:
    css = css.replace(target, replacement)
    print("Replaced corner dock CSS cleanly!")
else:
    print("Exact target not found, skipping replace.")

with open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\css\style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Saved public/css/style.css!")
