# Por: Wilton Lacerda Silva
# 06/2021
#https://www.youtube.com/watch?v=wf9nKxsWiOo

from machine import Pin, ADC
import utime

led_onboard = Pin(25, Pin.OUT)
adc_0 = ADC(28)
sensor_temp = ADC(4) #Temperatura
conversion_factor = 3.3 / (65535)

while True:
    valor = adc_0.read_u16()*conversion_factor

    temperatura = sensor_temp.read_u16()*conversion_factor
# Fómula para conversão de tensão em temperatura
    temperatura = 27 - (temperatura - 0.706)/0.001721
    print("ADC: ",str(round(valor,2)),"V   Temp: ",str(round(temperatura,2)),"C")
    utime.sleep(0.3)    
    
