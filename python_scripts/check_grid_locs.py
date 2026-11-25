from PIL import Image

im = Image.open(r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_1795622910081.jpg")

# 1. Look at (700 to 1100, 150 to 350) - Where "Your Trusted" is:
im.crop((700, 150, 1100, 350)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\loc_trusted.jpg")

# 2. Look at (550 to 750, 450 to 680) - Left tire / lower body:
im.crop((550, 450, 750, 680)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\loc_left_body.jpg")

# 3. Look at (750 to 1100, 350 to 680) - Right tire / lower arm:
im.crop((750, 350, 1100, 680)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\loc_arm.jpg")

# 4. Look at (1000 to 1400, 200 to 550) - Boom and slab:
im.crop((1000, 200, 1400, 550)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\loc_boom_slab.jpg")

print("Saved grid locations!")
