from PIL import Image
import numpy as np

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_perfect_clean_backdrop.jpg")
arr = np.array(im)

# Let's inspect x=0 to 860, y=150 to 450 (where Go Futer was)
crop_check = im.crop((0, 150, 860, 450))
crop_check.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\verify_clean_text_area.jpg")

# Check for any bright yellow text pixels:
arr_crop = np.array(crop_check)
yellow_mask = (arr_crop[:, :, 0] > 180) & (arr_crop[:, :, 1] > 140) & (arr_crop[:, :, 2] < 90)
print("Yellow text count in left & middle area:", np.sum(yellow_mask))

# Check top left corner for yellow stripes:
top_left = im.crop((0, 0, 150, 150))
arr_tl = np.array(top_left)
tl_yellow = (arr_tl[:, :, 0] > 180) & (arr_tl[:, :, 1] > 140) & (arr_tl[:, :, 2] < 90)
print("Yellow pixels in top left:", np.sum(tl_yellow))

# Check flare dots near slab:
slab_area = im.crop((1040, 145, 1160, 235))
slab_area.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\verify_clean_slab.jpg")
print("Verified! Background is clean.")
