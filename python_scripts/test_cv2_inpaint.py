import cv2
import numpy as np
from PIL import Image

banner = cv2.imread(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_exact_master_banner.jpg")
h, w, _ = banner.shape

# Blue text is in region: y: 350..495, x: 800..950
# Let's create an inpainting mask for the blue text:
# Notice banner in cv2 is BGR!
# Blue text in BGR: B > 100, R < 120 (since R is channel 2 in BGR!)
b = banner[:, :, 0]
g = banner[:, :, 1]
r = banner[:, :, 2]

# Let's restrict the mask strictly to the yellow beam around the blue text:
# x from 800 to 950, y from 355 to 490
mask = np.zeros((h, w), dtype=np.uint8)

# In the beam area:
# The yellow beam is along line y ~ 0.8537 * x - 325
# For each x in 805..945, the blue text line is around y0 = int(0.8537 * x - 325)
# Text width is ~ 25 pixels around y0
for x in range(805, 945):
    y_center = int(0.8537 * x - 325)
    for y in range(y_center - 18, y_center + 20):
        if 0 <= y < h:
            # Check if this pixel is blue text or white outline or dark border:
            # Blue text in BGR: b > 110, r < 140, or b > r + 30
            # White outline in BGR: b > 180, g > 180, r > 180
            # Dark text edge: b < 80, g < 80, r < 80
            is_blue = (b[y, x] > 110) & (b[y, x] > int(r[y, x]) + 20)
            is_white = (b[y, x] > 175) & (g[y, x] > 175) & (r[y, x] > 175)
            is_dark = (r[y, x] < 70) & (g[y, x] < 70) & (b[y, x] < 90)
            if is_blue or is_white or is_dark:
                mask[y, x] = 255

# Dilate mask slightly by 2 pixels to cover edges
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
mask_dilated = cv2.dilate(mask, kernel, iterations=1)

# Inpaint using Telea
inpainted = cv2.inpaint(banner, mask_dilated, 3, cv2.INPAINT_TELEA)

# Save result patch to inspect
x1, y1, x2, y2 = 780, 340, 960, 500
cv2.imwrite(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\test_beam_inpainted.png", inpainted[y1:y2, x1:x2])
cv2.imwrite(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\test_inpaint_mask.png", mask_dilated[y1:y2, x1:x2])
print("Inpainted patch saved!")
