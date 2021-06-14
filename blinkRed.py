# Por: Wilton Lacerda Silva
# 06/2021
#https://www.youtube.com/watch?v=p8gl-n2Y_Vk
import machine
import utime

led_onboard = machine.Pin(25, machine.Pin.OUT)
led_red = machine.Pin(19, machine.Pin.OUT)

while True:
    led_onboard.high()
    led_red.low()
    utime.sleep(0.5)
    led_onboard.low()
    led_red.high()
    utime.sleep(0.5)
