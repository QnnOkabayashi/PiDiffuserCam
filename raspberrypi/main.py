import os
from picamera import PiCamera
from datetime import datetime

# Create '/captures' for storing raw images if it doesn't already exist
captures_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'captures')
if not os.path.isdir(captures_path):
    os.mkdir(captures_path)


with PiCamera() as camera:
    camera.start_preview()
    input("Press <enter> to stop")
    camera.stop_preview()
    # d = datetime.now()
    # label = f'{d.year}-{d.month}-{d.day} at {d.hour}.{d.minute}.{d.second}'

    # camera.capture(output=os.path.join(captures_path, f'{label}.png'))

