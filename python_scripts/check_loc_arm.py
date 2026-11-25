from PIL import Image

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\loc_arm.jpg")
# let's save a clear visual inspect
print("loc_arm size:", im.size)
# What is the text on the boom in exact_reference_hero.jpg?
im_boom = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\check_upper_boom.jpg")
print("im_boom size:", im_boom.size)
