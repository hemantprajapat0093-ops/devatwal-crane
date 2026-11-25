from PIL import Image

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\exact_reference_hero.jpg")
w, h = im.size

# Let's inspect columns from x=600 to 900
# Where does the crane outrigger/wheel or body start?
# Let's crop strips of 50px width from x=550 to 850
for x in range(550, 850, 50):
    im.crop((x, 300, x + 50, 680)).save(rf"C:\Users\heman\Desktop\devatwal-crane-service\public\images\crane_start_{x}.jpg")
print("Saved crane start crops!")
