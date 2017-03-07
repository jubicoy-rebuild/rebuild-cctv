# RE:BUILD: Video-Surveillance system

## Goal

Goal is to have a video surveillance system with motion triggered snapshot and video saving and alerts via mail or SMS.
Surveillance system should have user interface for monitoring and for controls. You can also develope API for surveillance systems controls.
User interface for monitoring and controlling can be for any platform and done with any technology the group wants.

Focus on:
- Good documentation on how to setup the environment. Make the setup for users as easy as possible
- Keeping the UI easy to use and easy to understand
- Choosing well suiting technologies and maintaining clear architecture


## Requirements 
- C.H.I.P: 	https://getchip.com/
- PIR Sensor
- A camera 
- Python3 


## Descriptions 
While the program is running: 
	+ The camera takes snapshot and shows the picture continuously at C.H.I.P IP address opening with browser. 
	+ The motion sensor, if triggered, will save the screenshots in  /images folder with suitable name (image + timeformat) and send a message to a defined email.  


## Installations 
- Connect camera with USB port. 
- PIR sensor data PIN connect to XIO-P0 PIN of C.H.I.P. More info of other PINs (https://docs.getchip.com/chip.html#gpio)
- Copy index.html file to  /var/www/html/
- Replace your email and password in config.py (gmail)
- Run command 
```
sudo apt-get update
sudo apt-get install git build-essential python3-dev python3-pip flex bison chip-dt-overlays -y
pip install -r requirement.txt
cd CHIP_IO
sudo python3 setup.py install
```


## Up and running
Run 2 commands in seperated windows
```
sudo ./bash_sh
sudo python3 sensorDetect.py
```

Might need to change execution privilege
```
sudo chmod +x ./bash.sh
```

