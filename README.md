# PiDiffuserCam

Quinn Okabayashi and Josh Vandervelde
___
## Configure your Raspberry Pi
1. Follow the instructions [here](https://github.com/QnnOkabayashi/scripts/blob/master/HeadlessPi/README.md) for configuring your Raspberry Pi for headless mode and connecting via SSH.

2. Once connected via SSH, setup the project with the following command:
    ```
    $ source <(curl -s https://raw.githubusercontent.com/QnnOkabayashi/scripts/master/PiDiffuserCam/setup.sh)
    ```
    > Warning: You should always verify that scripts from URLs are safe before running! Check out the source code below yourself.

    [Source code](https://github.com/QnnOkabayashi/scripts/blob/master/PiDiffuserCam/setup.sh)

    This will:
    * Update the package manager
    * Install the required dependencies
    * Clone the project repo code to the home directory
    * Enable the PiCamera and RealVNC modules
    * Display VNC server address for [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/)
    * Reboot, enabling the VNC server
    > Note: Sometimes this code doesn't do anything for reasons beyond me. If it doesn't work at first, wait a minute and try again.

___
## Copying captured images to local machine via SSH
Enter the following command from the terminal of the machine you want to copy images to, substituting your local destination path:
```
$ scp -rp pi@raspberrypi.local:/home/pi/PiDiffuserCam/raspberrypi/captures /local/destination/path/
```
> Note: This command will fail if no images have been captured
