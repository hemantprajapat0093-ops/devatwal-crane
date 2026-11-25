from PIL import Image

im0 = Image.open(r"C:/Users/heman/.gemini/antigravity-cli/brain/4864e298-07a5-436c-ad5f-3371b3bb3f27/.user_uploaded/uploaded_media_0_1795620538745.jpg")
im1 = Image.open(r"C:/Users/heman/.gemini/antigravity-cli/brain/4864e298-07a5-436c-ad5f-3371b3bb3f27/.user_uploaded/uploaded_media_1_1795620538745.jpg")

# Let's save im1 as hero_crane_authentic.jpg
im1.save(r"C:/Users/heman/Desktop/devatwal-crane-service/public/images/hero_crane_authentic.jpg", quality=95)

# Also let's extract the header logo from im0 if possible, or see how it looks
# In im0, the logo is around x: 40 to 110, y: 15 to 80
logo_crop = im0.crop((35, 12, 115, 80))
logo_crop.save(r"C:/Users/heman/Desktop/devatwal-crane-service/public/images/header_logo_from_pic.png")

# Let's save im0 for reference
im0.save(r"C:/Users/heman/Desktop/devatwal-crane-service/public/images/hero_reference_design.jpg", quality=95)

print("Saved files successfully!")
