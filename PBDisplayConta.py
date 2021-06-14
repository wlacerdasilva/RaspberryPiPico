# Por: Wilton Lacerda Silva
# 06/2021
# https://www.youtube.com/watch?v=JuS28GyQxRM

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime

# Escolha dos pinos do I2C
i2c = I2C(0,sda=Pin(16),scl=Pin(17),freq=100000)
# Criar e instanciar um objeto oled
oled = SSD1306_I2C(128,64,i2c)
# Criar e intanciar objetos led e botão
led_onboard = machine.Pin(25, Pin.OUT)
# O pino do botão foi setado com um resistor de pull_down
button = machine.Pin(15,Pin.IN, Pin.PULL_DOWN)

#Inicialização do Display
oled.fill(0) #Preenchimento com 0 ou 1
oled.text("Gab. Tecnologia",2,4) #Texto e posição(x,y)
oled.rect(0,0,128,15,1)
oled.rect(0,16,16,16,1)
oled.text("0",20,20)
oled.show() #Apresenta no display

sinalizador  = True
contador = 0;

while True:

    if button.value() == True and sinalizador == True:
        led_onboard.value(1)
        oled.fill_rect(0,16,16,16,1)
        contador = contador + 1
        oled.fill_rect(20,16,24,16,0)
        oled.text(str(contador),20,20)
        oled.show()
        sinalizador = False
        utime.sleep(0.2)
    if button.value() == True and sinalizador == False:
        led_onboard.value(0)
        oled.fill_rect(0,16,16,16,0)
        oled.rect(0,16,16,16,1)
        oled.show()
        sinalizador = True
        utime.sleep(0.2)
    
