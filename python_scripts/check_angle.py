from PIL import Image
import numpy as np

user_img = Image.open(r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_1795628801899.png")
print("User uploaded image size:", user_img.size)

# Let's inspect the arm crop
arm = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\arm_devatwal_area.png")

# In arm, where is the yellow arm slanting?
# The arm slants downwards to the right (or from top-left to bottom-right):
# Let's measure the angle of the beam!
# Let's inspect a slice of the beam in arm
