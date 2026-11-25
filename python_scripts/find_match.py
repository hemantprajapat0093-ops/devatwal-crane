from PIL import Image
import numpy as np

im_new = Image.open(r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_1795627120219.jpg")
im_mock = Image.open(r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_1795622910081.jpg")

print("im_new:", im_new.size)
print("im_mock:", im_mock.size)

# Let's find template match
arr_new = np.array(im_new)
arr_mock = np.array(im_mock)

# Take a 100x100 patch from im_new at center
patch = arr_new[200:300, 300:400, :3]
# Find where patch matches in arr_mock
best_diff = float('inf')
best_loc = (0, 0)

for y in range(0, arr_mock.shape[0] - 100, 10):
    for x in range(0, arr_mock.shape[1] - 100, 10):
        diff = np.mean(np.abs(arr_mock[y:y+100, x:x+100, :3] - patch))
        if diff < best_diff:
            best_diff = diff
            best_loc = (x, y)

print(f"Best coarse match: diff={best_diff}, loc={best_loc}")
# Refine coarse match
bx, by = best_loc
best_refined = float('inf')
best_refined_loc = best_loc
for y in range(max(0, by - 15), min(arr_mock.shape[0] - 100, by + 15)):
    for x in range(max(0, bx - 15), min(arr_mock.shape[1] - 100, bx + 15)):
        diff = np.mean(np.abs(arr_mock[y:y+100, x:x+100, :3] - patch))
        if diff < best_refined:
            best_refined = diff
            best_refined_loc = (x, y)

print(f"Best refined match: diff={best_refined}, loc={best_refined_loc}")
# Since patch was at (300, 200) in im_new:
offset_x = best_refined_loc[0] - 300
offset_y = best_refined_loc[1] - 200
print(f"im_new is cropped at: x={offset_x}, y={offset_y} to x={offset_x+im_new.width}, y={offset_y+im_new.height}")
