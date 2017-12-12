from picamera import PiCamera
from time import sleep


#import the class definition from "email_handler.py" file
from email_handler import Class_eMail

#set the email ID where you want to send the test email 
To_Email_ID = "solidsnake93737@gmail.com"


# Send Plain Text Email 
email = Class_eMail()
email.send_Text_Mail(To_Email_ID, 'Trap Notice', 'Your Trapmaster69 has caught something. Please check it.')
del email


camera = PiCamera()
camera.start_preview()
sleep(3)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()

