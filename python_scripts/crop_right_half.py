from PIL import Image

im = Image.open(r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_1795622910081.jpg")
# Crop right half:
right = im.crop((550, 100, im.width, im.height))
right.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\test_right_half.jpg")
print("Saved test_right_half.jpg:", right.size)
