from gpiozero import LED
from gpiozero import Button
from time import sleep



led = LED(17)
button = Button(2)
while(1):
    button.wait_for_press()
    led.toggle()
