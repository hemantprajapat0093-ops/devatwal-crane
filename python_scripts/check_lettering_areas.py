from PIL import Image

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\exact_reference_hero.jpg")
w, h = im.size

# Let's crop the exact area of the lower arm and upper boom:
# Lower slant arm (between the front tire and the engine):
# Front tire is around x: 800 to 1050, y: 500 to 680
# Slant arm goes from (x: 820, y: 580) up to (x: 950, y: 450)
im.crop((780, 400, 1080, 680)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\check_slant_arm.jpg")

# Upper boom (where ACE 12XW is):
# Boom is around x: 1000 to 1350, y: 280 to 450
im.crop((950, 260, 1350, 480)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\check_upper_boom.jpg")

print("Saved check_slant_arm.jpg and check_upper_boom.jpg")
