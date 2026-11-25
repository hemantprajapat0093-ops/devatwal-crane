from PIL import Image

im1 = Image.open(r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_1_1795616151709.jpg")
print("im1 size:", im1.size)
w, h = im1.size
# lower slant arm:
im1.crop((300, 150, 700, 380)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\arm_real_im1.jpg")
# upper boom:
im1.crop((500, 20, 1000, 180)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\boom_real_im1.jpg")
print("Saved im1 crops!")
