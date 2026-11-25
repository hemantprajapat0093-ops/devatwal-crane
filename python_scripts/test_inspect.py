from PIL import Image

im = Image.open(r'C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_1795622910081.jpg')
print("Size:", im.size)
# Let's crop top navbar, left text, and crane
nav = im.crop((0, 0, im.width, 100))
nav.save(r'C:\Users\heman\Desktop\devatwal-crane-service\public\images\test_nav.jpg')

left = im.crop((0, 100, 700, im.height))
left.save(r'C:\Users\heman\Desktop\devatwal-crane-service\public\images\test_left.jpg')

right = im.crop((700, 100, im.width, im.height))
right.save(r'C:\Users\heman\Desktop\devatwal-crane-service\public\images\test_right.jpg')

print("Saved test crops")
