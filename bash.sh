#!/bin/bash
while true; do
	fswebcam -r 1280x720 --no-banner /var/www/html/image.jpg
	sleep 0.5
	read var < data.txt
	if (( $var == "1" ))
	then 
		fswebcam -r 1280x720 --no-banner images/image%H:%M:%S.jpg
		fswebcam -r 1280x720 --no-banner images/image%H:%M:%S.jpg
		fswebcam -r 1280x720 --no-banner images/image%H:%M:%S.jpg
	fi
done
