from PIL import Image

crop_path = r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_1795628801899.png"
crop = Image.open(crop_path)
print(f"Crop size: {crop.size}, mode: {crop.mode}")

banner_path = r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_exact_master_banner.jpg"
banner = Image.open(banner_path)
print(f"Banner size: {banner.size}")
