from PIL import Image
import numpy as np

# Let's inspect crop_clean_top, crop_clean_mid, crop_clean_bot
top = np.array(Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\crop_clean_top.png"))
mid = np.array(Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\crop_clean_mid.png"))
bot = np.array(Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\crop_clean_bot.png"))

print("Top shape:", top.shape)
print("Mid shape:", mid.shape)
print("Bot shape:", bot.shape)

# Let's check variance across x=0..80 to make sure no sudden lines or boundaries exist
# We want the sky and ground to transition smoothly
print("Top left corner mean:", np.mean(top[:40, :40, :], axis=(0,1)))
print("Mid left corner mean:", np.mean(mid[:40, :40, :], axis=(0,1)))
print("Bot left corner mean:", np.mean(bot[:40, :40, :], axis=(0,1)))
