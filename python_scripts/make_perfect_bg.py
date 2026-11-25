from PIL import Image

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\exact_reference_hero.jpg")
# In exact_reference_hero.jpg:
# The front left tire of the crane starts at x ~ 530, y ~ 500
# The cabin starts at x ~ 560
# The boom starts at x ~ 550
# On the left side from x=0 to x=520 is purely the text, badges, and dark blue gradient!
# Let's write a script that makes x=0 to 520 100% clean solid gradient with zero ghost text,
# and blends smoothly into the crane from x=490 to 540!
bg = im.copy()
w, h = bg.size

# Let's build a smooth navy-blue gradient for x from 0 to 520
# At x=0: #060b14 to #081122
# At y=0: #070d18
import numpy as np

arr = np.array(bg)
for x in range(540):
    # fade factor
    factor = min(1.0, max(0.0, (540 - x) / 50.0))
    if x < 490:
        factor = 1.0
    for y in range(h):
        y_ratio = y / h
        # target color: deep rich midnight navy #070e1e at top, #040812 at bottom
        r = int(7 * (1 - y_ratio) + 3 * y_ratio)
        g = int(14 * (1 - y_ratio) + 7 * y_ratio)
        b = int(30 * (1 - y_ratio) + 16 * y_ratio)
        
        orig_r, orig_g, orig_b = arr[y, x, :3]
        arr[y, x, 0] = int(r * factor + orig_r * (1 - factor))
        arr[y, x, 1] = int(g * factor + orig_g * (1 - factor))
        arr[y, x, 2] = int(b * factor + orig_b * (1 - factor))

res = Image.fromarray(arr)
res.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_perfect_clean_backdrop.jpg", quality=98)
print("Saved hero_perfect_clean_backdrop.jpg!")
