from PIL import Image
import numpy as np

mock = Image.open(r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_1795622910081.jpg")
w, h = mock.size
print("Mock size:", w, h)

# In mock, at y=300 (around middle of hero), what is the RGB across x from 0 to 1419?
# Let's inspect x=0, 200, 400, 500, 600, 700, 800, 1000, 1200, 1400:
for x in [0, 100, 200, 300, 400, 500, 550, 600, 700, 800, 1000, 1200]:
    print(f"x={x}: RGB at y=200 is {mock.getpixel((x, 200))}, at y=350 is {mock.getpixel((x, 350))}")
