from machine import Pin
from servo import Servo


led_orange= Pin(13,Pin.OUT)
led_rouge= Pin(12,Pin.OUT)
led_verte= Pin(14,Pin.OUT)
buzzer= Pin(25,Pin.OUT)
servo= Servo(Pin(27))