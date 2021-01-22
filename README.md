# PiDiffuserCam

Quinn Okabayashi and Josh Vandervelde

___
## Setting up your Raspberry Pi for [headless](https://en.wikipedia.org/wiki/Headless_computer) operation (OSX only)
Insert an unused micro SD card into your machine, and enter the following command:

```
$ python3 -c "import urllib.request; exec(urllib.request.urlopen('https://raw.githubusercontent.com/QnnOkabayashi/scripts/master/RaspberryPi/setup_headless.py').read())"
```

> Warning: You should always verify that scripts from URLs are safe before running! Check out the source code below yourself.

[Source code](https://github.com/QnnOkabayashi/scripts/blob/master/RaspberryPi/setup_headless.py)

This will:
* Prompt you to select a drive to format
* Flash Raspberry Pi OS Lite (32-bit) to it
* Prompt you for WiFi credentials
* Enable SSH via WiFi for the Pi
* Safely eject the drive

You may now remove the micro SD card and insert it into your Raspberry Pi.

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
$ source <(curl -s https://raw.githubusercontent.com/QnnOkabayashi/scripts/master/PiDiffuserCam/setup.sh)
```
[Source code](https://github.com/QnnOkabayashi/scripts/blob/master/PiDiffuserCam/setup.sh)

This will:
* Update the package manager
* Install Git and PiCamera, required dependencies
* Clone the project repo code to the home directory
* Enable the camera module
* Reboot
> Note: Sometimes this code doesn't do anything for reasons beyond me. If it doesn't work at first, wait a few minutes and try again.

## Copying captured images to local machine via SSH
Enter the following command from the terminal of the machine you want to copy images to, substituting your local destination file path:
```
$ scp -rp pi@raspberrypi.local:/home/pi/PiDiffuserCam/raspberrypi/captures /local/destination/path/
```
> Note: this command will fail if no images have been captured
