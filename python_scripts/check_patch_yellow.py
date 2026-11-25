from PIL import Image
import numpy as np

# Let's inspect test_patch_before.png
patch = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\test_patch_before.png")
print("Patch size:", patch.size)

# If we inpaint in the patch directly:
# What does the yellow beam look like around the blue text in the patch?
arr = np.array(patch)

# Let's find the yellow color of the beam around the blue text:
# The yellow beam has R ~ 240, G ~ 160, B ~ 35 (warm industrial yellow!)
yellow_mask = (arr[:, :, 0] > 200) & (arr[:, :, 1] > 130) & (arr[:, :, 2] < 70)
mean_yellow = np.mean(arr[yellow_mask], axis=0)
print("Mean yellow of the crane arm:", mean_yellow)
