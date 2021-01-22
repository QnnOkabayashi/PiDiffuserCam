# PiDiffuserCam

Quinn Okabayashi and Josh Vandervelde
___
## Configure your Raspberry Pi
Follow the instructions [here](https://github.com/QnnOkabayashi/scripts/blob/master/HeadlessPi/README.md) for configuring your Raspberry Pi for headless mode.
___
## Initialize project code
Once connected via SSH, setup the project with the following command:
```
$ source <(curl -s https://raw.githubusercontent.com/QnnOkabayashi/scripts/master/PiDiffuserCam/setup.sh)
```
> Warning: You should always verify that scripts from URLs are safe before running! Check out the source code below yourself.

[Source code](https://github.com/QnnOkabayashi/scripts/blob/master/PiDiffuserCam/setup.sh)

This will:
* Update the package manager
* Install Git and PiCamera, required dependencies
* Clone the project repo code to the home directory
* Enable the camera module
* Reboot
> Note: Sometimes this code doesn't do anything for reasons beyond me. If it doesn't work at first, wait a few minutes and try again.
___
## Copying captured images to local machine via SSH
Enter the following command from the terminal of the machine you want to copy images to, substituting your local destination file path:
```
$ scp -rp pi@raspberrypi.local:/home/pi/PiDiffuserCam/raspberrypi/captures /local/destination/path/
```
> Note: this command will fail if no images have been captured
