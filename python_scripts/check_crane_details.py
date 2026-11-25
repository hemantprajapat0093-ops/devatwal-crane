from PIL import Image

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\exact_reference_hero.jpg")
w, h = im.size
print(f"Size: {w}x{h}")

# Let's crop:
# 1. Under "Your Trusted" (x: 700 to 1000, y: 150 to 350)
im.crop((700, 150, 1000, 350)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\debug_your_trusted.jpg")

# 2. Lower boom / tire side where "देवतवाल क्रेन सर्विस" is written (x: 800 to 1100, y: 350 to 650)
im.crop((800, 350, 1100, 650)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\debug_lower_arm.jpg")

# 3. Main boom where "ACE 12XW प्रजापति" is written (x: 950 to 1350, y: 250 to 450)
im.crop((950, 250, 1350, 450)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\debug_main_boom.jpg")

# 4. Bottom right corner of image (where call/email dock sits) (x: 1100 to 1419, y: 500 to 689)
im.crop((1100, 500, w, h)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\debug_bottom_right.jpg")

print("Saved all debug crops!")
