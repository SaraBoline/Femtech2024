from neopixel import Neopixel
from machine import Pin, ADC, PWM
import time

pixels = Neopixel(5, 0, 0, "GRB") # no, state, pin, mode
button = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP)
#pwm_led = PWM(Pin(15,mode=Pin.OUT))
#pwm_led.freq(1_000)


while True:
    if not button.value():
        pixels.set_pixel(0, (255, 0, 0))
        pixels.show()
        time.sleep_ms(200)
        print("button pressed")
        pixels.set_pixel(0, (0, 0, 0))
        pixels.show()
