import RPi.GPIO as GPIO
from time import sleep

#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)

Motor1A = 23#pin 16 on board GPIO23
Motor1B = 24#pin18 on board GPIO24
Motor1E = 25#pin25 on board GPIO25

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

print ("Going forwards")

GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)

sleep(2)

print ("Going backwards")
GPIO.output(Motor1A,GPIO.LOW)
GPIO.output(Motor1B,GPIO.HIGH)
GPIO.output(Motor1E,GPIO.HIGH)

sleep(2)

print ("Now stop")
GPIO.output(Motor1E,GPIO.LOW)

GPIO.cleanup()
