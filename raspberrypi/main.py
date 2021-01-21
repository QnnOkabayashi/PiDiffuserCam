import os, picamera

# Create '/captures' for storing raw images if it doesn't already exist
captures_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "captures")
if not os.path.isdir(captures_path):
    os.mkdir(captures_path)

# Do image capturing stuff here


