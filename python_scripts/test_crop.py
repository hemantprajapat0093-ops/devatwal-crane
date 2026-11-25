from PIL import Image

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\exact_reference_hero.jpg")
w, h = im.size
print(f"Total size: {w}x{h}")

# Header area: y: 0 to 140
header = im.crop((0, 0, w, 140))
header.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\ref_header.jpg")

# Left text area: x: 0 to 650, y: 140 to 689
left_area = im.crop((0, 140, 650, h))
left_area.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\ref_left_text.jpg")

# Right crane area: x: 450 to w, y: 140 to h
right_crane = im.crop((450, 140, w, h))
right_crane.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\ref_crane_visual.jpg")

print("Cropped header, left, right successfully!")
