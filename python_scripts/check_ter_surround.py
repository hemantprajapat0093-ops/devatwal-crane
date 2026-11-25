from PIL import Image
import numpy as np

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\crop_ter.jpg")
arr = np.array(im)
# In crop_ter, y is 0..170 (250..420), x is 0..200 (650..850)
# What is around (x=150, y=50)? That's x=800, y=300
print("Color above yellow text (y=20, x=150):", arr[20, 150])
print("Color right of yellow text (y=80, x=195):", arr[80, 195])
print("Color below yellow text (y=165, x=150):", arr[165, 150])
