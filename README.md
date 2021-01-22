# PiDiffuserCam

Quinn Okabayashi and Josh Vandervelde

___
## Setting up your Raspberry Pi for SSH
1. Connect an unused micro SD card to your Mac

2. Enter the following
    ```
    $ python3 -c "import urllib.request; exec(urllib.request.urlopen('https://raw.githubusercontent.com/QnnOkabayashi/scripts/master/PiDiffuserCam/headless.py').read())"
    ```
    This will:
    * Prompt you to select a drive to format
    * Flash Raspberry Pi OS Lite (32-bit) to it
    * Prompt you for WiFi credentials
    * Enable SSH via WiFi for the Pi
    * Safely eject the drive

    > WARNING: You should always verify that scripts from URLs are safe before running! You can view the source code [here](https://github.com/QnnOkabayashi/scripts/blob/master/PiDiffuserCam/headless.py).

3. Insert your SD card in the Raspberry Pi and connect to power

## Connecting via SSH
1. When your Pi is powered on, open your terminal and enter the following
```
$ ssh pi@raspberrypi.local
```

2. If this is the first time connecting, you will see a message like the following, which you need to allow
```
The authenticity of host 'raspberrypi.local (xxxx:xxx:xxxx:xxxx::xxxx)' can't be established.
ECDSA key fingerprint is SHA256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

3. It will then prompt you for the password, which is `raspberry` by default

4. To disconnect from the SSH, use the `exit` command

## Initialize project code
Once connected via SSH, setup the project with the following command:
```
$ bash < <(curl -s https://raw.githubusercontent.com/QnnOkabayashi/scripts/master/PiDiffuserCam/setup.sh)
```
This will:
1. Update the package manager
2. Install Git and PiCamera, required dependencies
3. Clone the project repo code to the home directory

> If it doesn't clone the repo, run the command again

## Copying captured images to local machine via SSH
Enter the following command from the terminal of the machine you want to copy images to, substituting your local destination file path
```
$ scp -rp pi@raspberrypi.local:/home/pi/PiDiffuserCam/raspberrypi/captures /local/destination/path/
```
Note that this command will fail if no images have been captured
