from PIL import Image
import numpy as np

im = Image.open(r'C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_1795622910081.jpg')
arr = np.array(im)

# What is the color of the dark blue / sky on the top and left?
print("Top left (0,0):", arr[0,0])
print("Middle left (300, 0):", arr[300, 0])
print("Bottom left (680, 0):", arr[680, 0])
print("Sky at x=700, y=50:", arr[50, 700])
print("Sky at x=800, y=50:", arr[50, 800])
