import time
import wiringpi
import RPi.GPIO as GPIO
from gpiozero import Button

GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)
pwm = GPIO.PWM(12,50)
pwm.start(5)

button1 = Button(2)
button2 = Button(17)

#wiringpi.wiringPiSetupGpio()
#wiringpi.pinMode(18,wiringpi.GPIO.PWM_OUTPUT)
#wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

#wiringpi.pwmSetClock(192)
#wiringpi.pwmSetRange(2000)
#delay_period=0.01

ifOpen = 0

while True:
	if(button1.is_pressed):   #closed
		pwm.ChangeDutyCycle(5)
	if(button2.is_pressed):   #open
		pwm.ChangeDutyCycle(10)
	if(button1.is_pressed):
		if (button2.is_pressed):
			break;
GPIO.cleanup()
