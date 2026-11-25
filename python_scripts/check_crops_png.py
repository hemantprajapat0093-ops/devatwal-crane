from PIL import Image, ImageFilter
import numpy as np

# Let's inspect test_clean_top, test_clean_mid, test_clean_bot
top = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\test_clean_top.png")
mid = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\test_clean_mid.png")
bot = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\test_clean_bot.png")

print("Top size:", top.size)
print("Mid size:", mid.size)
print("Bot size:", bot.size)
