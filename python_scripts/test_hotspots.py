from PIL import Image, ImageDraw

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_exact_master_banner.jpg").copy()
draw = ImageDraw.Draw(im)

w, h = im.size

# Box 1: Book Crane Slot Online
x1 = int(w * 0.03666)
y1 = int(h * 0.8581)
w1 = int(w * 0.1984)
h1 = int(h * 0.0811)
draw.rectangle([x1, y1, x1 + w1, y1 + h1], outline="red", width=3)

# Box 2: Get a Quote
x2 = int(w * 0.2495)
y2 = int(h * 0.8547)
w2 = int(w * 0.1416)
h2 = int(h * 0.0845)
draw.rectangle([x2, y2, x2 + w2, y2 + h2], outline="cyan", width=3)

im.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\test_button_overlay.jpg")
print(f"Button 1: [{x1}, {y1}, {x1+w1}, {y1+h1}]")
print(f"Button 2: [{x2}, {y2}, {x2+w2}, {y2+h2}]")
print("Saved test_button_overlay.jpg!")
