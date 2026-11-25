from PIL import Image

beam = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\test_full_beam.png")
# If the beam slope is +0.8537 (angle ~ 40.5° clockwise downwards),
# rotating counter-clockwise by 40.5° (or -40.5°) makes it horizontal:
rotated = beam.rotate(40.5, expand=True, resample=Image.Resampling.BICUBIC)
rotated.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\beam_horizontal.png")

# Also try rotating by -40.5° just in case PIL rotate convention:
rotated_neg = beam.rotate(-40.5, expand=True, resample=Image.Resampling.BICUBIC)
rotated_neg.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\beam_horizontal_neg.png")

print("Saved both horizontal beam rotations!")
