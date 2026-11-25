from PIL import Image

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\arm_real_im1.jpg")
print("arm_real_im1 size:", im.size)
# In arm_real_im1, where is the text?
# Let's save a double-size version so we can inspect it clearly
im.resize((im.width * 2, im.height * 2), Image.Resampling.LANCZOS).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\arm_real_im1_large.jpg")
print("Saved arm_real_im1_large.jpg")
