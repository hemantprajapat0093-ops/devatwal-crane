import os

fonts = [
    r"C:\Windows\Fonts\nirmalab.ttf",
    r"C:\Windows\Fonts\mangalb.ttf",
    r"C:\Windows\Fonts\mangal.ttf",
    r"C:\Windows\Fonts\aparajb.ttf",
    r"C:\Windows\Fonts\nirmala.ttf"
]

for f in fonts:
    print(f, os.path.exists(f))
