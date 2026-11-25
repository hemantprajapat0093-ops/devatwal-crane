from PIL import Image

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\exact_reference_hero.jpg")
# Let's crop from x=450 to 750, y=100 to 500
crop1 = im.crop((450, 100, 750, 500))
crop1.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\test_text_overlap.jpg")
print("Saved test_text_overlap.jpg")
