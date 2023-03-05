from machine import Pin
import time
led = machine.Pin('LED', machine.Pin.OUT)
for i in range (1000):
    led.on()
    time.sleep(0.3)
    led.off()
    time.sleep(0.3)
    led.on()
    time.sleep(0.3)
    led.off()
    time.sleep(1)
