from PIL import Image

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\user_crane_exact.jpg")
w, h = im.size
print(f"Size: {w}x{h}")

# Let's crop the left 120 pixels to see the letter snippets
crop_left = im.crop((0, 0, 120, h))
crop_left.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\test_user_crane_left.jpg")
print("Saved test_user_crane_left.jpg")
