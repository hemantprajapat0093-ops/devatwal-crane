from PIL import Image

im0 = Image.open(r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_0_1795620538745.jpg")
print("im0 size:", im0.size)
im0.crop((0, 0, 700, 400)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\test_im0_crop.jpg")
print("Saved test_im0_crop.jpg")
