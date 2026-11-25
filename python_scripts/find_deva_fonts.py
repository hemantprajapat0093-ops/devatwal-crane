import glob, os

for f in sorted(glob.glob(r"C:\Windows\Fonts\*.*")):
    base = os.path.basename(f).lower()
    if any(k in base for k in ["nirm", "mangal", "apar", "utsa", "kokila", "segoe", "devan", "hindi"]):
        print(os.path.basename(f))
