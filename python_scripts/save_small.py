from PIL import Image

im = Image.open(r'C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_1795622910081.jpg')
# Let's save a downscaled version to see what the image looks like
im_small = im.resize((im.width // 2, im.height // 2))
im_small.save(r'C:\Users\heman\Desktop\devatwal-crane-service\public\images\ref_small.jpg')
print("Saved ref_small.jpg")
