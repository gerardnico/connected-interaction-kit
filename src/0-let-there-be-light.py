# Let There Be Light!
# Source: https://id-studiolab.github.io/Connected-Interaction-Kit/tutorials/let-there-be-light/part-2
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

while True:
    time.sleep(1.0)
    led.value = True
    print("LED is on")

    time.sleep(1.0)
    led.value = False
    print("LED is off")
