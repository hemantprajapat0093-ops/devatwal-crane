from PIL import Image
import numpy as np

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\left_of_tire.png")
arr = np.array(im)
print("left_of_tire shape:", arr.shape)
# Notice in full image, x=587 corresponds to x=137 in left_of_tire (587 - 450 = 137)
# What is between x=0 and 137 in left_of_tire?
# In left_of_tire, x=0..137 corresponds to x=450..587 of the full image
for x in range(0, 150, 20):
    print(f"x_rel={x} (full_x={450+x}): RGB at y=100 is {arr[100, x]}, at y=200 is {arr[200, x]}")
