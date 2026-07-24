from machine import Pin

while True:
    if Pin(4, Pin.IN).value() == 1:
        Pin(2, Pin.OUT).value(1)
    if Pin(4, Pin.IN).value() == 0:
        Pin(2, Pin.OUT).value(0)