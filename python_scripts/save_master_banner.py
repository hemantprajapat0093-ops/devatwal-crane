from PIL import Image

path = r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_1795628364577.jpg"
im = Image.open(path)
w, h = im.size
print(f"Dimensions: {w} x {h}")

# Save to public/images/hero_exact_master_banner.jpg
dest_path = r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_exact_master_banner.jpg"
im.save(dest_path, quality=98)
print("Saved to public/images/hero_exact_master_banner.jpg")

# Let's check where the buttons are located in pixels (x, y, w, h)
# Button 1: "Book Crane Slot Online ->"
# Button 2: "Get a Quote"
# We can find their coordinates in the image:
