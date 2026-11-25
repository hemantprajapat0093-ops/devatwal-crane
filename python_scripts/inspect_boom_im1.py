from PIL import Image

im_boom = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\boom_real_im1.jpg")
print("im_boom size:", im_boom.size)
im_boom.resize((im_boom.width * 2, im_boom.height * 2), Image.Resampling.LANCZOS).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\boom_real_im1_large.jpg")
print("Saved boom_real_im1_large.jpg")
