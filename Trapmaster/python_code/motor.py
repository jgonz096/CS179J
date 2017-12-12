import RPi.GPIO as GPIO
from time import sleep
from gpiozero import Button
from signal import pause

GPIO.setmode(GPIO.BCM)

button = Button(2)
button2 = Button(17)

direction = 0

Motor1A = 23#pin 16 on board GPIO23
Motor1B = 24#pin18 on board GPIO24
Motor1E = 25#pin25 on board GPIO25

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

def forwards():
	print ("Going forwards")
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.HIGH)
	i = 0
	#while(i < 2500):
	#	i = i + 1
	#GPIO.output(Motor1E,GPIO.LOW)
def backwards():
	print ("Going backwards")
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor1E,GPIO.HIGH)
	i = 0
	#while(i < 2500):
	#	i = i + 1
	#GPIO.output(Motor1E,GPIO.LOW)
def off():
	print ("Turning Off")
	GPIO.output(Motor1E,GPIO.LOW)

while(True):
	
	#button.when_pressed = backwards
	button.when_released = backwards
	#button2.when_pressed = forwards
	button2.when_released = forwards
	
	if button.is_pressed:
		if button2.is_pressed:
			off()
			break
		


GPIO.cleanup()
