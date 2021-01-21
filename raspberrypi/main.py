import os, picamera.PiCamera
from datetime import datetime

# Create '/captures' for storing raw images if it doesn't already exist
captures_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "captures")
if not os.path.isdir(captures_path):
    os.mkdir(captures_path)

# Do image capturing stuff here

with PiCamera() as camera:
    d = datetime.now()
    label = f"{d.year}-{d.month}-{d.day} at {d.hour}.{d.minute}.{d.second}"

    camera.capture(output=f"captures/{label}.png")

