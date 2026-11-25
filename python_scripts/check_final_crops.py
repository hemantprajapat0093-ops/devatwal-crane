from PIL import Image

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_perfect_clean_backdrop.jpg")

# 1. Under "Your Trusted"
im.crop((700, 180, 1050, 420)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\verify_sharp_trusted.jpg")

# 2. Slant arm
im.crop((750, 420, 1050, 650)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\verify_sharp_arm.jpg")

# 3. Upper boom
im.crop((1000, 260, 1350, 420)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\verify_sharp_boom.jpg")

# 4. Bottom right corner
im.crop((1100, 480, im.width, im.height)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\verify_clean_br.jpg")

print("Saved verification crops!")
