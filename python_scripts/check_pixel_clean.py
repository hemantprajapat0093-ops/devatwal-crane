from PIL import Image
import numpy as np

src_top = np.array(Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\crop_src_top.png"))
clean_top = np.array(Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\crop_clean_top.png"))

# Where in src_top are high values (white text/border)?
# In src:
white_pixels_src = (src_top[:, :, 0] > 180) & (src_top[:, :, 1] > 180) & (src_top[:, :, 2] > 180)
print("Src top white text pixels:", np.sum(white_pixels_src))

white_pixels_clean = (clean_top[:, :, 0] > 180) & (clean_top[:, :, 1] > 180) & (clean_top[:, :, 2] > 180)
print("Clean top white pixels:", np.sum(white_pixels_clean))

src_mid = np.array(Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\crop_src_mid.png"))
clean_mid = np.array(Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\crop_clean_mid.png"))
yellow_src = (src_mid[:, :, 0] > 200) & (src_mid[:, :, 1] > 160) & (src_mid[:, :, 2] < 50)
print("Src mid yellow pixels (from '...r.'):", np.sum(yellow_src))
yellow_clean = (clean_mid[:, :, 0] > 200) & (clean_mid[:, :, 1] > 160) & (clean_mid[:, :, 2] < 50)
print("Clean mid yellow pixels:", np.sum(yellow_clean))

src_bot = np.array(Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\crop_src_bot.png"))
clean_bot = np.array(Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\crop_clean_bot.png"))
white_bot_src = (src_bot[:, :, 0] > 180) & (src_bot[:, :, 1] > 180) & (src_bot[:, :, 2] > 180)
print("Src bot white pixels (from '...le'):", np.sum(white_bot_src))
white_bot_clean = (clean_bot[:, :, 0] > 180) & (clean_bot[:, :, 1] > 180) & (clean_bot[:, :, 2] > 180)
print("Clean bot white pixels:", np.sum(white_bot_clean))
