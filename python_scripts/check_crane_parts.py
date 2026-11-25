from PIL import Image

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\exact_reference_hero.jpg")
w, h = im.size

# Let's see:
# y=0 to 120 is the header in the reference mockup.
# y=120 to 689 is the hero section!
# In the hero section:
# Where is the crane?
# Let's crop x=500..800, y=350..689 (bottom half where crane cabin and tires are)
im.crop((500, 350, 800, 689)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\crane_lower_body.jpg")
# Where is the boom and lifted slab?
im.crop((800, 120, 1419, 500)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\crane_upper_boom.jpg")
print("Saved crane lower body and upper boom crops!")
