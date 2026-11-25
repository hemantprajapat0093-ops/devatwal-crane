with open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\index.html", "r", encoding="utf-8") as f:
    html = f.read()

print("Vishnudat count:", html.count("Vishnudat"))
print("Dharminder count:", html.count("Dharminder"))
print("Maman count:", html.count("Maman"))
print("Satyapal count:", html.count("Satyapal"))
print("8003721244 count:", html.count("8003721244"))
print("9982842357 count:", html.count("9982842357"))
print("9414333328 count:", html.count("9414333328"))
print("9950233073 count:", html.count("9950233073"))
print("corner-dock-btn-maps count:", html.count("corner-dock-btn-maps"))
print("Yard link to Google Maps present:", "https://www.google.com/maps/place/Devatwal+Crane+Service/@28.0604817,76.4195232" in html)
