#!/bin/python
import time
from gpiozero import Button
from signal import pause
from subprocess import Popen

#This function runs a command to mute whatever is plugged into Headphone
def mute_volume():
    Popen(['amixer', 'set', 'Headphone', 'mute'])

#This function unmutes whatever is plugged into Headphone
def unmute_volume():
    Popen(['amixer', 'set', 'Headphone', 'unmute'])
    #This makes the code pause for 30 seconds 
    time.sleep(30)
    #After the 30 seconds is up whatever is plugged into Headphone is again muted
    Popen(['amixer', 'set', 'Headphone', 'mute'])

#The following 2 lines allow a button pligged into GPIO 14 to mute any playing sound
button_up = Button(14)
button_up.when_pressed = mute_volume
#The next two lines allow a button plugged into GPIO 21 to unmute any playing sound
button_down = Button(21)
button_down.when_pressed = unmute_volume
pause()

#All of this code is based on some I found on the raspberry pi forums
#https://www.raspberrypi.org/forums/viewtopic.php?f=32&t=222763&p=1644293&hilit=alsamixer+volume+control+via+gpio#p1644293
#Many thanks to paddyg
