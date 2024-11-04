import machine
import utime
import urandom

led = machine.Pin(1, machine.Pin.OUT)
button1 = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP)
button2 = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)


fastest_button = None

def button_handler(pin):
    button1.irq(handler=None)
    button2.irq(handler=None)
    global fastest_button
    fastest_button = pin
    

led.value(1)
utime.sleep(urandom.uniform(5,10))
led.value(0)
button1.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)
button2.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)

while fastest_button is None:
    utime.sleep(1)

if fastest_button is button1:
    print("Button 1 wins")
    led.value(1)
    utime.sleep(0.2)
    led.value(0)
    
elif fastest_button is button2:
    print("Button 2 wins")
    led.value(1)
    utime.sleep(0.2)
    led.value(0)
    utime.sleep(0.2)
    led.value(1)
    utime.sleep(0.2)
    led.value(0)
    



