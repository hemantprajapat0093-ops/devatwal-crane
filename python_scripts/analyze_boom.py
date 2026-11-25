from PIL import Image
import numpy as np

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\check_crane_boom_area.jpg")
print("Size:", im.size)
# The crop is x=600..1000, y=100..500
# Let's see what features are in this crop:
# Where is the crane hydraulic cylinder or boom?
arr = np.array(im)
# The crane boom is yellow/orange metal. ACE 12XW.
# Where is ACE 12XW?
# ACE 12XW is on the boom!
# Where does the boom start?
