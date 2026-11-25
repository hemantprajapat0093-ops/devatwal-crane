from PIL import Image, ImageDraw

banner = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_exact_master_banner.jpg").copy()
draw = ImageDraw.Draw(banner)

# Let's crop from (760, 300, 980, 520)
beam_crop = banner.crop((750, 300, 980, 520))
beam_crop.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\test_full_beam.png")
print("Saved test_full_beam.png, size:", beam_crop.size)
