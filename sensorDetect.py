import CHIP_IO.GPIO as GPIO
import time
import smtplib
from config import * 

#GPIO.setmode(GPIO.BCM)
PIR_PIN = "XIO-P0"
GPIO.setup(PIR_PIN, GPIO.IN)


# EMAIL settings
sendEmail = SEND_EMAIL
sendEmailPass = SEND_PASSWORD
recceiveEmail = RECEIVE_EMAIL


try:
        print ("PIR Module Test")
        time.sleep(1)
        print ("Ready")
        while True:
                if GPIO.input(PIR_PIN):
                        print("Motion Detected!")       
                        try:
                                server = smtplib.SMTP('smtp.gmail.com', 587)
                                server.starttls()
                                server.login(sendEmail, sendEmailPass)
                                msg = "MOTION TRIGGERED!"
                                server.sendmail(sendEmail, recceiveEmail, msg)
                                print ('------')
                                print ('Sent to email')
                                print ('------')
                        except smtplib.SMTPAuthenticationError:
                                print ('------')
                                print ('Wrong username or password. Change in config.py')
                                print ('------')
                        except Exception:
                                print ('------')
                                print ('Mail cannot be sent')
                                print ('------')
                        finally:
                                server.quit()
                else:
                        print(GPIO.input(PIR_PIN))
                time.sleep(1)
except KeyboardInterrupt:
                print ("Quit")
                GPIO.cleanup()



