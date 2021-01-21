# PiDiffuserCam

Quinn Okabayashi and Josh Vandervelde

___
## Installing Raspberry Pi OS and enabling SSH
1. Install the [Raspberry Pi Imager](https://www.raspberrypi.org/documentation/installation/installing-images/)

2. Connect an unused microSD card to your computer

3. Follow the instructions in the Raspberry Pi Imager software

    * OS: Select Raspberry Pi OS (other) > Raspberry Pi OS Lite (32-bit)
    * SD Card: Selected the microSD card you plugged in

4. Click "Write" and wait for the imager to finish flashing the OS

5. Enable SSH on boot by creating an empty file called `ssh` with the following
```
touch /Volumes/boot/ssh
```

6. The first step to enabling WiFi connection is to create a `wpa_supplicant.conf` file
```
touch /Volumes/boot/wpa_supplicant.conf
```

7. Then, open that text file and paste the following, substituting your network credentials

    This step won't work if your network has a confirmation page.
```
country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    scan_ssid=1
    ssid="your_wifi_ssid"
    psk="your_wifi_password"
}
```

8. Once these files have been created, you can eject the microSD and insert it into the Raspberry Pi, and plug it into power

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

## Installing project dependencies
Since Git and PiCamera do not come installed in Raspberry Pi OS Lite, you must manually install them.

1. Once connected via SSH, install Git and PiCamera with the following commands
```
$ sudo apt-get update
$ sudo apt-get install git python3-picamera
```

2. Verify that Git was installed with the following command, which should display the version
```
$ git --version
```

3. Verify that PiCamera was installed with the following command, which should produce no output
```
$ python3 -c "import picamera"
```

## Cloning the project repo and setup
1. Once connected via SSH, clone the project repo with the following command from the home directory
```
$ git clone https://github.com/QnnOkabayashi/PiDiffuserCam.git
```

2. Run the following, which should output "`Success!`" (This is basically useless right now)
```
$ python3 PiDiffuserCam/raspberrypi/main.py
```

## Copying captured images to local machine via SSH
Enter the following command from the terminal of the machine you want to copy images to, substituting your local destination file path
```
$ scp -rp pi@raspberrypi.local:/home/pi/PiDiffuserCam/raspberrypi/captures /local/destination/path/
```