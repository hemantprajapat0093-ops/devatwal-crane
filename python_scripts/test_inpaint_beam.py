from PIL import Image
import numpy as np

banner = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_exact_master_banner.jpg").copy()
arr = np.array(banner)

# In banner, blue text is roughly in box x: 805..945, y: 360..485
# Let's crop this patch and check:
patch = arr[355:490, 800:950].copy()

# On the yellow beam:
# The yellow beam has high R, high G, low B: e.g. R ~ 220-255, G ~ 140-190, B ~ 10-60
# The blue text has: B > 100, and B > R - 10
# The white outline has: R > 190, G > 190, B > 190
# Let's detect the blue text + its outline:
is_blue = (patch[:, :, 2] > 100) & (patch[:, :, 2] > patch[:, :, 0] - 10) & (patch[:, :, 1] < 160)
is_white_outline = (patch[:, :, 0] > 180) & (patch[:, :, 1] > 180) & (patch[:, :, 2] > 160) & (patch[:, :, 0] < 255)

# Also any dark blue/black edge of the text:
is_text_dark = (patch[:, :, 0] < 80) & (patch[:, :, 1] < 80) & (patch[:, :, 2] < 120)

print("Detected blue text pixels:", np.sum(is_blue))
print("Detected white outline pixels:", np.sum(is_white_outline))

# Save patch before cleaning
Image.fromarray(patch).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\test_patch_before.png")
