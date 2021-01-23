import os
from picamera import PiCamera
from datetime import datetime

# Create '/captures' for storing raw images if it doesn't already exist
captures_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'captures')
if not os.path.isdir(captures_path):
    os.mkdir(captures_path)


with PiCamera() as camera:
    camera.start_preview()
    while True:
        user_input = input('Press <enter> to take a picture, or q+<enter> to quit: ')
        if user_input == '':
            label = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            camera.capture(os.path.join(captures_path, f'{label}.png'))
        elif user_input == 'q':
            break
    camera.stop_preview()

