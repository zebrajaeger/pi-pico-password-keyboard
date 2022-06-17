# Rasperry Pi Pico Password Keyboard

## Install the software

- Press the boot key of your RPP und connect it to your computer via USB.
- A new drive should occour.
- Download the Circuitpyton .uf2 from [here](https://circuitpython.org/board/raspberry_pi_pico).
- Copy the downloaded .uf2 file to the new drive.
- The RPP should reboot.
- Circuitpython is now up and running.
- Clone or download this repo to your computer.

    git clone https://github.com/zebrajaeger/pi-pico-password-keyboard.git

- Copy the config.example.py file to config.py
- Change the content of the config.py file as you want.
- Copy this to the root of the RPP drive:

    code.py
    config.py
    lib

- Reboot the RPP (unplug and plug it again).

## Hardware

- All pins are pulled up with a internal resistor to 3.3V.
- Connect a switch between GND and the configured IO pin from RPP.
- Press the switch. The onboard-LED should be on for a short while and the configured text should be typed.
