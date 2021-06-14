# Por: Wilton Lacerda Silva
# 06/2021
# https://www.youtube.com/watch?v=1ojMMcB5pmY

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

# Escolha dos pinos do I2C
i2c = I2C(0,sda=Pin(16),scl=Pin(17),freq=100000)
# Criar e instanciar um objeto oled
oled = SSD1306_I2C(128,64,i2c)

oled.fill(0) #Preenchimento com 0 ou 1
oled.text("Gab.Tecnologico",2,4) #Texto e posição(x,y)
oled.rect(0,0,128,15,1)
oled.rect(30,16,16,16,1)
oled.fill_rect(70,16,16,16,1)
oled.hline(0,36,128,1)
temperatura = 26.12345
oled.text(str(round(temperatura,2)),2,40)

oled.show() #Apresenta no display