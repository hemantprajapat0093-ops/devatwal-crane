from PIL import Image
import numpy as np

im = Image.open(r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_0_1795627290194.jpg")
w, h = im.size
print(f"Image width: {w}, height: {h}")

# Let's find exactly where the rear tire and engine box start in x
# The rear tire is on the lower left. Let's find its leftmost pixel:
arr = np.array(im)

# Look at y from 400 to 580: where does the tire / yellow engine frame actually start?
for x in range(0, 150, 5):
    col = arr[400:580, x]
    # Check if there is machinery (dark tire or yellow frame)
    # The yellow engine frame has high R, high G, low B (R>180, G>100, B<50)
    # The tire has low values (R<80, G<80, B<80)
    yellows = np.sum((col[:, 0] > 180) & (col[:, 1] > 100) & (col[:, 2] < 60))
    tire = np.sum((col[:, 0] < 70) & (col[:, 1] < 70) & (col[:, 2] < 70))
    print(f"x={x:3d} (x/w={x/w*100:.1f}%): yellows={yellows:3d}, tire_dark={tire:3d}")
