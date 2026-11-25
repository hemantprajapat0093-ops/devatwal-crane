from PIL import Image
import numpy as np

crop = Image.open(r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_1795628801899.png").convert("RGB")
banner = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_exact_master_banner.jpg")

crop_arr = np.array(crop).astype(np.float32)
banner_arr = np.array(banner).astype(np.float32)

cw, ch = crop.size
bw, bh = banner.size

# The yellow arm is somewhere around x: 600..950, y: 250..550
# Let's search with SSD (sum of squared differences) or normalized cross-correlation
best_ssd = float("inf")
best_pos = (0, 0)

# To speed up, search in a reasonable region:
for y in range(250, bh - ch, 2):
    for x in range(600, 1000, 2):
        patch = banner_arr[y:y+ch, x:x+cw]
        ssd = np.mean(np.abs(patch - crop_arr))
        if ssd < best_ssd:
            best_ssd = ssd
            best_pos = (x, y)

print(f"Best match position in banner: x={best_pos[0]}, y={best_pos[1]}, SSD={best_ssd}")

# Let's crop around that position in the banner to verify
x, y = best_pos
banner.crop((x - 20, y - 20, x + cw + 20, y + ch + 20)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\test_matched_arm.png")
print("Saved test_matched_arm.png!")
