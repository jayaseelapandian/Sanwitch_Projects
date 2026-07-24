from machine import Pin, ADC

while True:
    if ADC(Pin(4)).read() == 1:
        Pin(2, Pin.OUT).value(1)
    if ADC(Pin(4)).read() == 0:
        Pin(2, Pin.OUT).value(0)