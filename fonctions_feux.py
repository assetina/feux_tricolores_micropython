import machine
from machine import *
from time import sleep
import time

def allumer(led):
    led.on()
    
def eteindre(led):
    led.off()
     

    
def clignoterb(buzzer):
    buzzer.on()
    sleep(0.5)
    buzzer.off()
    sleep(0.5)
    buzzer.on()
    sleep(0.5)
    buzzer.off()
    sleep(0.5)
    buzzer.on()
    sleep(0.5)
    buzzer.off()
    