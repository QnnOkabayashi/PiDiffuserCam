# PiDiffuserCam

Quinn Okabayashi and Josh Vandervelde
___
## Configure your Raspberry Pi
Follow the instructions [here](https://github.com/QnnOkabayashi/scripts/blob/master/PiDiffuserCam/README.md) for configuring your Raspberry Pi to run our code.
___
## Copying captured images to local machine via SSH
Enter the following command from the terminal of the machine you want to copy images to, substituting your local destination path:
```
$ scp -rp pi@raspberrypi.local:/home/pi/PiDiffuserCam/raspberrypi/captures /local/destination/path/
```
> Note: This command will fail if no images have been captured
