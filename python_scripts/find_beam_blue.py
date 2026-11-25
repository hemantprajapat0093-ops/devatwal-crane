from PIL import Image
import numpy as np

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\beam_horizontal.png")
arr = np.array(im)

# Look at y around the red text (yr is 95..164)
# In Indian truck/crane art, "देवतवाल" is line 1, and "क्रेन सर्विस" is line 2 (just above or below it),
# or "देवतवाल" is the first half, and "क्रेन सर्विस" is the second half!
# Let's inspect rows y from 100 to 220:
# Where are the blue pixels on the yellow beam (around yr)?
mask = (arr[:, :, 2] > 120) & (arr[:, :, 2] > arr[:, :, 0] + 30) & (arr[:, :, 1] < 160)
# Filter only y between 70 and 220:
mask[:70, :] = False
mask[220:, :] = False

yb, xb = np.where(mask)
if len(xb) > 0:
    print(f"Blue text on beam: x={xb.min()}..{xb.max()}, y={yb.min()}..{yb.max()}")
    # Let's crop x: 50..270, y: 70..210
    im.crop((50, 70, 270, 210)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\clean_beam_text_area.png")
    print("Saved clean_beam_text_area.png!")
