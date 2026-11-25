from PIL import Image
import numpy as np

base = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\test_cleaned_base.jpg")
base.crop((0, 0, 100, 120)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\test_clean_top.png")
base.crop((0, 360, 100, 500)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\test_clean_mid.png")
base.crop((0, 540, 100, 603)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\test_clean_bot.png")

arr = np.array(base)

# Check top:
white_top = np.sum((arr[20:120, :60, 0] > 190) & (arr[20:120, :60, 1] > 190) & (arr[20:120, :60, 2] > 190))
print("White pixels in top [20:120, :60]:", white_top)

# Check mid:
# In mid, was there text? The text "...r." was bright yellow.
# Yellow text is typically R > 220, G > 180, B < 60
yellow_mid = np.sum((arr[365:435, :45, 0] > 220) & (arr[365:435, :45, 1] > 180) & (arr[365:435, :45, 2] < 60))
print("Yellow text pixels in mid [365:435, :45]:", yellow_mid)

# Check bot:
white_bot = np.sum((arr[560:, :35, 0] > 180) & (arr[560:, :35, 1] > 180) & (arr[560:, :35, 2] > 180))
print("White pixels in bot [560:, :35]:", white_bot)
