# Let's get physical and assemble a circuit and control it with our Pi Zero

# Requirements
1. Breadboard
2. Resistor(s)
3. LED(s) 
4. Male to female wires 
5. Raspberry Pi Zero, screen, keyboard, mouse and adaptors to make it all work

# Summary of Steps
1. Make the circuit - resistor from + to one of the rows above; long LED ends to resistor rail; short LED ends to negative rail (-)
2. Connect to Pi Zero - from GPIO 21 to positive on breadboard (+); from GND to negative on breadboard
3. Check [Pi GPIO Schematic](https://www.raspberrypi.org/documentation/usage/gpio-plus-and-raspi2) to be sure of numbers 
4. Open Python 3 IDE
5. Open a new file and save it with a name... e.g. led.py
6. Here is a simple script

``` python
from gpiozero import LED
from time import sleep

leds_on = LED(21)

while True:
  leds_on.on()
  sleep(1)
  leds_on.off()
  sleep(1)
```

8. Save the file 
9. Run the file using Run module. 


[Inspiration and Hat Tip to Cat Lamin](https://catlamin.com/2017/04/16/an-easter-gift-rpi-beginners-worksheet/)

[Picture Link](https://www.raspberrypi.org/documentation/usage/gpio-plus-and-raspi2/images/gpio-numbers-pi2.png)

