from PIL import Image
import numpy as np

full_mock = Image.open(r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_1795622910081.jpg")
user_crop = Image.open(r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_0_1795627290194.jpg")

# In full_mock, where is the crane located?
# Let's save full_mock crop from (400, 86, 1419, 689)
full_mock.crop((400, 86, 1419, 689)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\mock_crane_area.jpg")
user_crop.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\user_crop_clean.jpg")
print("Saved both to compare!")
