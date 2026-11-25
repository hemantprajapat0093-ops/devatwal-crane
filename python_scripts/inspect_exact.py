from PIL import Image

im = Image.open(r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_1795622910081.jpg")
print("Image size:", im.size)

# Let's save a pristine copy in public/images
im.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\exact_reference_hero.jpg", quality=98)

# Let's also crop the navbar logo
# Logo is on the top left: roughly x: 90 to 180, y: 35 to 135
logo_crop = im.crop((95, 45, 175, 125))
logo_crop.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\exact_logo.png")

# Let's check the right side crane image:
# x: ~500 to 1419, y: 150 to 689
crane_crop = im.crop((520, 150, 1419, 689))
crane_crop.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\exact_crane_crop.jpg", quality=98)

# Let's also extract the full background without the left text if needed, or see how it looks
print("Saved exact_reference_hero.jpg, exact_logo.png, exact_crane_crop.jpg")
