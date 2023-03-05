from machine import Pin
led = machine.Pin('LED', Pin.OUT)
import time

for i in range (1000):
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)
