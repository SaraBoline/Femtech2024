from machine import ADC
from time import sleep

adcpin = ADC(26)
#OBS pin 26

while True:
    adc_value = adcpin.read_u16()
    print (adc_value)
    sleep(1)
