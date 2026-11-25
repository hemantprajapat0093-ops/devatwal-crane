from PIL import Image

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\beam_text_tight_crop.png")
# Let's save a clean JPEG and PNG for verification
im.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\verify_hindi_crane_service.jpg", quality=98)
print("Saved verify_hindi_crane_service.jpg successfully!")
