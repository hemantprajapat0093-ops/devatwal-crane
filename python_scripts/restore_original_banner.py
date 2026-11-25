from PIL import Image, ImageFilter
import os
import shutil

original_path = r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_1795628364577.jpg"
orig_im = Image.open(original_path)
w, h = orig_im.size
print(f"Original master image: {w}x{h}")

target_dirs = [
    r"C:\Users\heman\Desktop\devatwal-crane-service\public\images",
    r"C:\Users\heman\Desktop\devatwal-crane-service\devatwal-crane\public\images",
]

# Create 2x version for retina
im_2x = orig_im.resize((w * 2, h * 2), Image.Resampling.LANCZOS)
im_2x = im_2x.filter(ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=2))

for tdir in target_dirs:
    if os.path.exists(tdir):
        # 1x banner
        path_1x = os.path.join(tdir, "hero_exact_master_banner.jpg")
        orig_im.save(path_1x, quality=98)
        print("Restored:", path_1x)
        
        # 2x banner
        path_2x = os.path.join(tdir, "hero_exact_master_banner_2x.jpg")
        im_2x.save(path_2x, quality=98)
        print("Restored:", path_2x)
        
        # hero_crane_full_view.jpg
        path_full = os.path.join(tdir, "hero_crane_full_view.jpg")
        orig_im.save(path_full, quality=98)
        print("Restored:", path_full)

print("All banners reverted to exact original state!")
