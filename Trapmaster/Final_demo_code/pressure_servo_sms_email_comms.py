#Name: Jorge Gonzalez
#Username: jgonz096
#SID:861112270
#Class: CS179j

import time
import os
from gpiozero import LED
import RPi.GPIO as GPIO
import wiringpi
from gpiozero import Button
from time import sleep
#Twilio library is used for sending SMS notifications
from twilio.rest import Client
#This file is important to import as it gives the trap be a client
#to request food recommendations from the food database.
import myclient

#Gives user privileges of using Twilio library, since an account is needed
client = Client('AC70ae102e0d6f11f826857b5baea76c3f','99a18fe57d3de06ac661f52ae7f2bd41')

#Uses email handler code to setup Email usage. This sets up a variable
#for emails mapped to the email of the user
from email_handler import Class_eMail
To_Email_ID = "solidsnake93737@gmail.com"
email = Class_eMail()

#setup up GPIO pins for usage on raspberry pi
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)

#setup for PWM motor control
pwm = GPIO.PWM(12,50)
pwm.start(5)

#setup for buttons. Provided uses below
button1 = Button(2) #No use here. Used for testing in other code
button2 = Button(17) #Used to Open the door when closed
button3 = Button(22) #Used for making a connection to the server for food recommendations
button4 = Button(5) #Turns off device

#debugging tool. when set to 1, it displays weight readouts on the screen
DEBUG = 0#1

#LED setup. led lights up when there is a weight sensed
led = LED(27)

#function: readadc
#description: This came from adafruits website on using the mcp3008
#			chip since the raspberry pi does not have internal ADC.
#			It reads SPI data from the chip using 8 bits, for a range
#			of 0 through 1024
#credit: Adafruit website tutorial on mcp3008
def readadc(adcnum,clockpin,mosipin,misopin,cspin):
	if((adcnum > 7) or (adcnum < 0)):
		return -1
	GPIO.output(cspin,True)
	GPIO.output(clockpin,False) #start clock low
	GPIO.output(cspin, False)     # bring CS low
 
        commandout = adcnum
        commandout |= 0x18  # start bit + single-ended bit
        commandout <<= 3    # we only need to send 5 bits here
        for i in range(5):
                if (commandout & 0x80):
                        GPIO.output(mosipin, True)
                else:
                        GPIO.output(mosipin, False)
                commandout <<= 1
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
 
        adcout = 0
        # read in one empty bit, one null bit and 10 ADC bits
        for i in range(12):
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
                adcout <<= 1
                if (GPIO.input(misopin)):
                        adcout |= 0x1
 
        GPIO.output(cspin, True)
        
        adcout >>= 1       # first bit is 'null' so drop it
        return adcout
 
# change these as desired - they're the pins connected from the
# SPI port on the ADC to the Cobbler
#credit: Adafruit website tutorial on mcp3008
SPICLK = 18
SPIMISO = 23
SPIMOSI = 24
SPICS = 25
 
# set up the SPI interface pins
#credit: Adafruit website tutorial on mcp3008
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPICS, GPIO.OUT)
 
# 10k trim pot connected to adc #0
#credit: Adafruit website tutorial on mcp3008
#note: I used my own potentiometer as compared to adafruits since mine 
#		has a more user friendly knob. I ended up removing it though
#		after it was no longer needed since there was no need to adjust
#		adc values
potentiometer_adc = 0;
 
last_read = 0       # this keeps track of the last potentiometer value
tolerance = 1       # to keep from being jittery we'll only change
                    # volume when the pot has moved more than 5 'counts'
 
isopen = 1
issent = 0
#credit: Adafruit website tutorial on mcp3008
#Note: This while Loop is a modified version of the Adafruit code for 
#		reading ADC values. Everything stems from reading those
#		values. I built everything else up from it. 
while True:
	# we'll assume that the pot didn't move
	trim_pot_changed = False

	# read the analog pin
	trim_pot = readadc(potentiometer_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
	# how much has it changed since the last read?
	pot_adjust = abs(trim_pot - last_read)
	

	#if DEBUG is on, print debuggnig values
	if DEBUG:
		print "trim_pot:", trim_pot
		print "pot_adjust:", pot_adjust
		print "last_read", last_read

	#if a change is detected, there was movement, so light the LED
	if ( pot_adjust > tolerance ):
	   trim_pot_changed = True
	   led.on()
	else:
		led.off()

	if DEBUG:
		print "trim_pot_changed", trim_pot_changed
	
	#if there is a change and that change is larger than the threshold,
	#activate the trap
	if ( trim_pot_changed and trim_pot >= 15 ):
		led.on()
		#if open button is pressed while activated, it takes priority as
		#user is likely trying to release creature. Dont want to close 
		#prematurely. Continue otherwise
		if (button2.is_pressed):
			pwm.ChangeDutyCycle(10)
			isopen = 1
			issent = 0
		else:
			#set trap to closed
			isopen = 0
			pwm.ChangeDutyCycle(5)
			if (issent == 0):
				#Send the user a SMS notification
				client.messages.create(from_='19093216714',to='19097497707',body='Greetings from TrapMaster69@420blzit.com! You\'ve caught something! . Please check your email for an image of it.')
				#Send the user an Email notification with image
				email.send_Text_Mail2(To_Email_ID, 'Trap Notice', 'Your Trapmaster69 has caught something.')
				issent = 1
			elif (issent == 1):
				#if trap was already closed, do nothing, report it
				print 'already sent'
		set_volume = trim_pot / 10.24           # convert 10bit adc0 (0-1024) trim pot read into 0-100 volume level
		set_volume = round(set_volume)          # round out decimal value
		set_volume = int(set_volume)            # cast volume as integer

		print 'Volume = {volume}%' .format(volume = set_volume)
		set_vol_cmd = 'sudo amixer cset numid=1 -- {volume}% > /dev/null' .format(volume = set_volume)
		os.system(set_vol_cmd)  # set volume
		
		
		if DEBUG:
			print "set_volume", set_volume
			print "tri_pot_changed", set_volume

		# save the potentiometer reading for the next loop
		last_read = trim_pot
		if(button4.is_pressed):
			break;
	else:
		led.off()
		#while OPEN button is pressed, keep trap open. User wants it to be
		#open while pressed
		while(button2.is_pressed):
			pwm.ChangeDutyCycle(10)
			isopen = 1
			issent = 0
		#if open, set variables accordingly, else keep it closed
		if (isopen == 1):
			pwm.ChangeDutyCycle(10)
			isopen = 1
			issent = 0
		elif (isopen == 0):
			pwm.ChangeDutyCycle(5)
		#if FOOD button is pressed, make a connection to the server
		#and have user input the desired pest to get food for
		if(button3.is_pressed):
			myclient.run_client()
		#if OFF button is pressed, shut off device
		if(button4.is_pressed):
			break;
		
	# hang out and do nothing for a half second
	time.sleep(0.5)

#delete email object and cleanup GPIO pins for next run
del email
GPIO.cleanup()
