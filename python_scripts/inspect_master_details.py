from PIL import Image

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_exact_master_banner.jpg")
print("Size:", im.size)

# Let's crop a few areas to inspect their crispness:
# 1. Headline: "Lift Higher, Go Further."
im.crop((40, 140, 600, 320)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\test_crop_headline.png")

# 2. Crane Hindi text: "देवतवाल क्रेन सर्विस" and "ACE 12XW प्रजापति"
im.crop((650, 180, 1250, 480)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\test_crop_crane.png")

# 3. Slab and hook:
im.crop((1100, 80, 1391, 450)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\test_crop_slab.png")

print("Inspection crops saved!")
