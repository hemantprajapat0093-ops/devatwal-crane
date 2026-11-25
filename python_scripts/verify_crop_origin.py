from PIL import Image

full_mock = Image.open(r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_1795622910081.jpg")
user_crop = Image.open(r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_0_1795627290194.jpg")

print("full_mock size:", full_mock.size) # (1419, 689)
print("user_crop size:", user_crop.size) # (832, 603)

# If full_mock is (1419, 689), then (1419 - 832) = 587, and (689 - 603) = 86!
# Let's crop full_mock from (587, 86, 1419, 689):
cropped_from_mock = full_mock.crop((587, 86, 1419, 689))
print("cropped_from_mock size:", cropped_from_mock.size)

# Compare cropped_from_mock with user_crop
import numpy as np
diff = np.abs(np.array(cropped_from_mock, dtype=np.int32) - np.array(user_crop, dtype=np.int32))
print("Mean absolute difference:", np.mean(diff))
print("Max absolute difference:", np.max(diff))
