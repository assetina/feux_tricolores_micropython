from time import sleep
from configuration_feux import *
from fonctions_feux import *



while True:
    allumer(led_rouge)
    sleep(2)
    for i in range(0,90):
        servo.write_angle(i)
    sleep(10)
    eteindre(led_rouge)
    servo.write_angle(-90)
    sleep(2)
    allumer(led_verte)
    sleep(5)
    eteindre(led_verte)
    allumer(led_orange)
    sleep(5)
    eteindre(led_orange)
    clignoterb(buzzer)
    
    