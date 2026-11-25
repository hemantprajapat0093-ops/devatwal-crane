from PIL import Image

im = Image.open(r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_1795622910081.jpg")
w, h = im.size
print(f"Size: {w}x{h}")

# In uploaded_media_1795622910081.jpg:
# Top left corner: x: 0 to 50, y: 0 to 50 - check if there's yellow
top_left = im.crop((0, 0, 100, 100))
top_left.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\debug_top_left.jpg")

# Near the lifted slab on the right: x: 1100 to 1419, y: 150 to 450 - check for green/blue circles or lens artifacts
slab_area = im.crop((1100, 150, 1419, 450))
slab_area.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\debug_slab.jpg")

print("Cropped debug areas.")
