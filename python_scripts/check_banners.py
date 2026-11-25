from PIL import Image

for name in ['devatwal_partner_crane.jpg', 'devatwal_heavy_lift_banner.jpg', 'hero_reference_design.jpg']:
    p = f"C:/Users/heman/Desktop/devatwal-crane-service/public/images/{name}"
    im = Image.open(p)
    print(name, im.size)
