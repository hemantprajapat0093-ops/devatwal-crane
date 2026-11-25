from PIL import Image

im = Image.open(r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_1_1795616151709.jpg")
print("im1 size:", im.size)
# In im1, what is the resolution and sharpness?
# Let's crop the crane from im1:
# On the left is the cabin (x: 50 to 250), then outrigger/engine (x: 250 to 500), then arm (x: 450 to 700), then boom (x: 500 to 1100), then right side has the yellow parallelogram "Devatwal Crane Service"
# Let's crop the text on the arm in im1:
im.crop((440, 160, 680, 360)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\arm_text_im1_crop.jpg")
# Let's crop the text on the boom in im1:
im.crop((600, 40, 950, 160)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\boom_text_im1_crop.jpg")
print("Saved arm_text_im1_crop.jpg and boom_text_im1_crop.jpg!")
