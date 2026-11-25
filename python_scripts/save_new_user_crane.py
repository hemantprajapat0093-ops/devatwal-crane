from PIL import Image

im_new = Image.open(r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_1795627120219.jpg")
print("im_new size:", im_new.size)

# Save a clean copy into public/images
im_new.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\user_crane_reference.jpg", quality=98)
print("Saved user_crane_reference.jpg!")
