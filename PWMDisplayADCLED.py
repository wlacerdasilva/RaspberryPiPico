# Por: Wilton Lacerda Silva
# 06/2021


from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
import utime

cd# Escolha dos pinos do I2C
i2c = I2C(0,sda=Pin(16),scl=Pin(17),freq=100000)
# Criar e instanciar um objeto oled
oled = SSD1306_I2C(128,64,i2c)
# Criar e intanciar objetos led e botão PWM
led_onboard = machine.PWM(machine.Pin(25))
led_red = machine.PWM(machine.Pin(19))
led_red.freq(1000)
# O pino do botão foi setado com um resistor de pull_down
button = machine.Pin(15,Pin.IN, Pin.PULL_DOWN)
# Configuração dos ADCs
adc_0 = ADC(28) #GP28 equivale ao canal 2
sensor_temp = ADC(4) #Canal 4 Temperatura
conversion_factor = 3.3 / (65535)

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
        oled.fill_rect(0,16,16,16,1)
        contador = contador + 1
        oled.fill_rect(20,16,24,16,0)
        oled.text(str(contador),20,20)
        oled.show()
        sinalizador = False
        utime.sleep(0.2)
    if button.value() == True and sinalizador == False:
        oled.fill_rect(0,16,16,16,0)
        oled.rect(0,16,16,16,1)
        oled.show()
        sinalizador = True
        utime.sleep(0.2)
    valor = adc_0.read_u16()
    led_onboard.duty_u16(valor-1)
    led_red.duty_u16(valor)
    oled.fill_rect(40,16,40,16,0)
    oled.text(str(round(valor*conversion_factor,2))+"V",40,20)
    oled.fill_rect(40,32,40,16,0)
    oled.text(str(valor),40,36)
    oled.fill_rect(40,48,80,16,0)
    oled.text(str(round(valor*100/65535,1))+"%",40,52)
    oled.fill_rect(80,48,40,16,0)
    temperatura = sensor_temp.read_u16()*conversion_factor
    temperatura = 27 - (temperatura - 0.706)/0.001721
    oled.fill_rect(89,16,39,16,0)
    oled.text(str(round(temperatura,1)),90,20)
    oled.show()


