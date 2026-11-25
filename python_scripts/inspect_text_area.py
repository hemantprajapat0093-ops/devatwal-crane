from PIL import Image
import numpy as np

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\debug_text_gofuter.jpg")
arr = np.array(im)
h, w, _ = arr.shape

# Let's inspect what is in debug_text_gofuter.jpg (which is x=400 to 850 in original)
# Original y=200 to 400
# Is the crane boom or sky behind the text?
print("Shape of crop:", h, w)
# Let's check color of sky around x=700..850 in original (which is 300..450 in this crop)
for rel_x in range(0, w, 50):
    orig_x = 400 + rel_x
    print(f"Orig x={orig_x}: y=220 color={arr[20, rel_x][:3]}, y=350 color={arr[150, rel_x][:3]}")
