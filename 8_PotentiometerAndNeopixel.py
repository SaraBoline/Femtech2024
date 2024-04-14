#neopixel virker med potentiometer



from neopixel import Neopixel
from machine import Pin, ADC, PWM
import time

pixels = Neopixel(5, 0, 0, "GRB") # no, state, pin, mode
adc = ADC(Pin(26, mode=Pin.IN))
#pwm_led = PWM(Pin(15,mode=Pin.OUT))
#pwm_led.freq(1_000)


def map_to_rainbow_color(value):
    num_colors = 7  # Number of colors in the rainbow
    # Map the potentiometer value to the range of rainbow colors
    if value > 0 and value < 300:
        return (255, 0, 0)  # Red
    elif value > 301 and value < 600:
        return (255, 127, 0)  # Orange
    elif value > 601 and value < 900:
        return (255, 255, 0)  # Yellow
    elif value > 901 and value < 1200:
        return (0, 255, 0)  # Green
    elif value > 1201 and value < 1500:
        return (0, 0, 255)  # Blue
    elif value > 1501 and value < 1800:
        return (75, 0, 130)  # Indigo
    elif value >1801 and value < 2100:
        return (148, 0, 211)  # Violet


while True:
    duty = adc.read_u16() #  between ~350-65535
    low_res = duty >> 5
    color = map_to_rainbow_color(int(low_res))
    pixels.set_pixel(0, (color))
    pixels.show()
    time.sleep_ms(100)
    print(low_res)
    print('#%02x%02x%02x' % color)
    
