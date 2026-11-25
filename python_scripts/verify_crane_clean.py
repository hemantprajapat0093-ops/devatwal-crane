from PIL import Image
import os

path = r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_crane_full_view.jpg"
im = Image.open(path)
print(f"hero_crane_full_view.jpg size: {im.size}")

# Check left edge (0 to 100 pixels in x) across various y ranges
# Crop and check the left edge to ensure the text snippets ('...t Rating', '...r.', '...le') are completely gone
crop1 = im.crop((0, 0, 150, im.height))
crop1.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\test_left_edge.jpg")
print("Saved test_left_edge.jpg")
