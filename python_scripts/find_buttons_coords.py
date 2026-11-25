from PIL import Image
import numpy as np

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_exact_master_banner.jpg")
w, h = im.size
arr = np.array(im)

# Button 1: "Book Crane Slot Online" is bright amber/yellow at the bottom left:
# Let's find rows around y: 480 to 580, x: 0 to 400
# Yellow button has high R, high G, low B: (R > 220, G > 160, B < 60)
mask_yellow = (arr[480:580, :400, 0] > 220) & (arr[480:580, :400, 1] > 160) & (arr[480:580, :400, 2] < 60)
y_indices, x_indices = np.where(mask_yellow)

if len(y_indices) > 0:
    min_y, max_y = 480 + y_indices.min(), 480 + y_indices.max()
    min_x, max_x = x_indices.min(), x_indices.max()
    print(f"Yellow button ('Book Crane Slot Online'): x={min_x}..{max_x} ({min_x/w*100:.1f}%..{max_x/w*100:.1f}%), y={min_y}..{max_y} ({min_y/h*100:.1f}%..{max_y/h*100:.1f}%)")

# Button 2: "Get a Quote" is to the right of the yellow button:
# It has a white/grey outline and dark center. Let's find where it is:
# Usually from max_x of yellow button to around x=500, between min_y and max_y
# Let's crop y from min_y - 10 to max_y + 10, x from min_x - 10 to 600
crop_btns = im.crop((min_x - 10, min_y - 10, 600, max_y + 10))
crop_btns.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\crop_buttons.png")
print("Saved crop_buttons.png")
