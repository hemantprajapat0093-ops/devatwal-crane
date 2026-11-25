from PIL import Image

im = Image.open(r'C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_1795622910081.jpg')
w, h = im.size
print(f"Total size: {w}x{h}")

# Let's inspect where the text ends and crane starts
# The crane cabin starts around x=570 to 650.
# The ground starts around y=480.
# Let's see slices at x = 500, 550, 600, 650
for x_test in [500, 550, 600, 650, 700]:
    slice_img = im.crop((x_test, 0, x_test + 100, h))
    slice_img.save(rf'C:\Users\heman\Desktop\devatwal-crane-service\public\images\slice_{x_test}.jpg')
print("Slices saved")
