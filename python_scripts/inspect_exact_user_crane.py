from PIL import Image

im = Image.open(r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_0_1795627290194.jpg")
print("Size:", im.size, im.mode)

# Save high-quality copy in public/images
im.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\user_crane_exact.jpg", quality=98)
print("Saved user_crane_exact.jpg!")
