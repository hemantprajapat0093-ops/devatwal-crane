from PIL import Image, ImageFilter

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_exact_master_banner.jpg")
w, h = im.size

# Upscale to 2x for Retina / 4K displays
target_w = w * 2
target_h = h * 2

im_2x = im.resize((target_w, target_h), Image.Resampling.LANCZOS)
im_2x = im_2x.filter(ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=2))
im_2x.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_exact_master_banner_2x.jpg", quality=98)

print(f"Generated 2x master banner: {target_w}x{target_h}")
