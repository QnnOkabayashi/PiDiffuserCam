# PiDiffuserCam

Quinn Okabayashi and Josh Vandervelde
___
## Configure Software
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
    * Display VNC server address
    * Reboot, enabling the VNC server
    > Note: Sometimes this code doesn't do anything for reasons beyond me. If it doesn't work at first, wait a minute and try again.

3. On your local machine, install [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/).

4. Open VNC Viewer and enter the VNC Server address the setup process displayed in step 2. This will open a window where the camera feed will display when we enable it.

5. To start taking pictures, SSH into the Pi, navigate to `~/PiDiffuserCam/raspberrypi`, and enter:
    ```
    $ python3 main.py
    ```
___
## Copying captured images
The `scp` command can be used to transfer files over SSH. The following command transfers images from the Raspberry Pi to your desktop (executed from your local shell):
```
$ scp -rp pi@raspberrypi.local:/home/pi/PiDiffuserCam/raspberrypi/captures /Users/$(whoami)/Desktop
```
> Note: This command will fail if no images have been captured

___
## 2D Reconstruction
1. After transfering the images to your computer, convert them to `.tif` by renaming them.
2. Clone the [tutorial code](https://github.com/Waller-Lab/DiffuserCam-Tutorial) repository into a Jupyter Notebook.
2. Upload them to the Jupyter Notebook and edit the config block (shown below) by entering in the image file names:
    ```python
    psfname = "./psf_file_name_here.tif"
    imgname = "./image_file_name_here.tif"
    ```
3. You can also change the number of iterations for tweaking the clarity:
    ```python
    # Number of iterations
    iters = 5
    ```
4. Restart the kernel to execute script, and the reconstruction will display at the bottom.