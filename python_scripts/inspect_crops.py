from PIL import Image
import numpy as np

src = Image.open(r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_0_1795627290194.jpg")
w, h = src.size
print("Source size:", w, h)

cleaned = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_crane_full_view.jpg")
print("Cleaned size:", cleaned.size)

# Save crops to check:
src.crop((0, 0, 100, 120)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\crop_src_top.png")
cleaned.crop((0, 0, int(100*1400/w), int(120*1400/w))).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\crop_clean_top.png")

src.crop((0, 360, 100, 500)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\crop_src_mid.png")
cleaned.crop((0, int(360*1400/w), int(100*1400/w), int(500*1400/w))).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\crop_clean_mid.png")

src.crop((0, 540, 100, 603)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\crop_src_bot.png")
cleaned.crop((0, int(540*1400/w), int(100*1400/w), int(603*1400/w))).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\crop_clean_bot.png")

print("Crops saved successfully!")
