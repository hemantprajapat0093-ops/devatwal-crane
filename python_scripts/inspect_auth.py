from PIL import Image
import numpy as np

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\auth_left.jpg")
print("auth_left size:", im.size)
# Let's inspect what is on the left
arr = np.array(im)
# Is it the crane or text?
print("Top-left pixel:", arr[0,0])
print("Middle pixel:", arr[im.height//2, im.width//2])
