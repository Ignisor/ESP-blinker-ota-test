import machine
import time

LED = machine.Pin(2, machine.Pin.OUT)


def blink():
    while True:
        LED.value(not LED.value())
        time.sleep(0.1)
