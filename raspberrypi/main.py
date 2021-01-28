import os
from picamera import PiCamera

# Create '/captures' for storing raw images if it doesn't already exist
captures_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'captures')
if not os.path.isdir(captures_path):
    os.mkdir(captures_path)

with PiCamera() as camera:
    camera.start_preview()
    print('Type a file name and press <enter> to capture, or leave blank to quit')
    while True:
        user_input = input('> ').strip()
        if user_input == '':
            break
        else:
            camera.capture(os.path.join(captures_path, f'{user_input}.png'))
    camera.stop_preview()

