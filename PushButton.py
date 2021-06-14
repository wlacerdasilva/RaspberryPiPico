# Por: Wilton Lacerda Silva
# 06/2021
# https://www.youtube.com/watch?v=JuS28GyQxRM

from machine import Pin
import utime

led_onboard = Pin(25, Pin.OUT)
button = Pin(15,Pin.IN, Pin.PULL_DOWN)
led_onboard.value(1)

while True:
    if button.value():
        led_onboard.toggle()
        utime.sleep(0.2)
    