# Por: Wilton Lacerda Silva
# 06/2021
#https://www.youtube.com/watch?v=wf9nKxsWiOo

from machine import Pin, ADC
import utime

led_onboard = Pin(25, Pin.OUT)
adc_0 = ADC(28)
conversion_factor = 3.3 / (65535)

while True:
    valor = adc_0.read_u16()*conversion_factor
    print("ADC: ",str(round(valor,2)),"V")
    utime.sleep(0.3)
    

