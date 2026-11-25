from PIL import Image
import numpy as np

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\final_crane_arm_inspection.png")
arr = np.array(im)

# Let's crop just around the beam text area:
# x: 100 to 450, y: 50 to 350
beam_text_crop = im.crop((100, 50, 450, 350))
beam_text_crop.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\beam_text_tight_crop.png")
print("Saved beam_text_tight_crop.png!")
