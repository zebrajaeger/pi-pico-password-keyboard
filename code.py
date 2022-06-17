
import time

import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
# https://github.com/Neradoc/Circuitpython_Keyboard_Layouts/tree/main/libraries/layouts
from adafruit_hid.keyboard_layout_win_de import KeyboardLayout
from adafruit_hid.keycode import Keycode

from config import configItems

time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayout(keyboard)  

for configItem in configItems:
    key_pin = digitalio.DigitalInOut(configItem['pin'])
    key_pin.direction = digitalio.Direction.INPUT
    key_pin.pull = digitalio.Pull.UP
    configItem['switch'] = key_pin;

print(configItems)
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

print("Waiting for key pin...")

while True:
    for configItem in configItems:
        switch = configItem['switch']
        if not switch.value:              
            print("Pin #{} is grounded.".format(configItem['pin']))
            
            led.value = True

            while not switch.value:
                pass  
            
            keyboard_layout.write(configItem['value'])

            led.value = False

    time.sleep(0.01)
