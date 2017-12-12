import time
import os
from gpiozero import LED
import RPi.GPIO as GPIO
import wiringpi
from gpiozero import Button

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
pwm = GPIO.PWM(12,50)
pwm.start(5)

button1 = Button(2)
button2 = Button(17)

DEBUG = 1


led = LED(27)


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
SPICLK = 18
SPIMISO = 23
SPIMOSI = 24
SPICS = 25
 
# set up the SPI interface pins
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPICS, GPIO.OUT)
 
# 10k trim pot connected to adc #0
potentiometer_adc = 0;
 
last_read = 0       # this keeps track of the last potentiometer value
tolerance = 1       # to keep from being jittery we'll only change
                    # volume when the pot has moved more than 5 'counts'
 
isopen = 1
 
while True:
	# we'll assume that the pot didn't move
	trim_pot_changed = False

	# read the analog pin
	trim_pot = readadc(potentiometer_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
	# how much has it changed since the last read?
	pot_adjust = abs(trim_pot - last_read)

	if DEBUG:
		print "trim_pot:", trim_pot
		print "pot_adjust:", pot_adjust
		print "last_read", last_read

	if ( pot_adjust > tolerance ):
	   trim_pot_changed = True
	   led.on()
	else:
		led.off()

	if DEBUG:
		print "trim_pot_changed", trim_pot_changed

	if ( trim_pot_changed and trim_pot >= 15):
		led.on()
		if (button2.is_pressed):
			pwm.ChangeDutyCycle(10)
			isopen = 1
		else:
			isopen = 0
			pwm.ChangeDutyCycle(5)
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
		if(button1.is_pressed):
			if (button2.is_pressed):
				break;
	else:
		led.off()
		if (isopen == 1) or (button2.is_pressed):
			pwm.ChangeDutyCycle(10)
			isopen = 1
		elif (isopen == 0):
			pwm.ChangeDutyCycle(5)
		if(button1.is_pressed):
			if (button2.is_pressed):
				break;
			
	# hang out and do nothing for a half second
	time.sleep(0.5)



#p = GPIO.PWM(18,50)
#p.start(0)
#try:
#	while 1:
#		for dc in range(0,101,5):
#			p.ChangeDutyCycle(dc)
#			time.sleep(0.1)
#		for dc in range(100,-1,-5):
#			p.ChangeDutyCycle(dc)
#			time.sleep(0.1)
#except KeyboardInterrupt:
#	pass
#p.stop()
#GPIO.cleanup()
