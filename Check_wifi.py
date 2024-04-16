import network
import time
import urequests
from machine import ADC, PWM, Pin
import json

button = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP)


#Autorisation
ssid = "DIKU2"
password = "PeterNaur"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

url = "https://ml.dataekspeditioner.dk/add/"


while(True):
    if wlan.isconnected():
        
        
        if not button.value():
            print("pushed")
            
            payload = json.dumps({
              "email": "peaches@marioland.com",
              "state": "#ff0000"
            })

            headers = {
              'Content-Type': 'application/json'
            }

            response = urequests.request("POST", url, headers=headers, data=payload)

            print(response) # e.g. <Response [200]>
            
    else:
        print("not connected")
    time.sleep(0.5)


