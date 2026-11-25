from PIL import Image

im_arm = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\check_slant_arm.jpg")
print("im_arm size:", im_arm.size)

im_boom = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\check_upper_boom.jpg")
print("im_boom size:", im_boom.size)
