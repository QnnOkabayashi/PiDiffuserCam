# PiDiffuserCam

Quinn Okabayashi and Josh Vandervelde

___
## Installing Raspberry Pi OS and enabling SSH via WiFi
1. Install the [Raspberry Pi Imager](https://www.raspberrypi.org/documentation/installation/installing-images/)

2. Connect an unused micro SD card to your computer

3. Follow the instructions in the Raspberry Pi Imager software to flash the OS

    * OS: Select Raspberry Pi OS (other) > Raspberry Pi OS Lite (32-bit)
    * SD Card: Select the micro SD card you plugged in

4. This software ejects the drive, so you have to physically eject and insert the SD card again

5. To enable SSH over WiFi, run the following command and follow the instructions
```
$ bash -c "$(curl -s https://raw.githubusercontent.com/QnnOkabayashi/scripts/master/PiDiffuserCam/headless.sh)"
```
This will:
* Prompt you to select the boot drive (Select the same drive as in the previous step)
* Prompt you to enter WiFi credentials
* Write necessary files to enable SSH via WiFi

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

## Project setup
Once connected via SSH, setup the project with the following command:
```
$ curl -s https://raw.githubusercontent.com/QnnOkabayashi/scripts/master/PiDiffuserCam/setup.sh | bash
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
