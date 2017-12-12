from gpiozero import Buzzer
from time import sleep



buzzer = Buzzer(17)
while(1):
    #buzzer.on()
    #sleep(1)
    #buzzer.off()
    #sleep(1)
    buzzer.beep()
