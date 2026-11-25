from PIL import Image

im0 = Image.open(r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_0_1795620538745.jpg")
im_ref = Image.open(r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_1795622910081.jpg")

print("im0 crop at 0,0:", im0.getpixel((10, 10)))
print("im_ref crop at 0,0:", im_ref.getpixel((10, 10)))
