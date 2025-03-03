# https://id-studiolab.github.io/Connected-Interaction-Kit/tutorials/adding-inputs-and-outputs/part-2

import board
import digitalio
import time

sensor = digitalio.DigitalInOut(board.D2)
sensor.direction = digitalio.Direction.INPUT

motor = digitalio.DigitalInOut(board.D13)
motor.direction = digitalio.Direction.OUTPUT

while True:
    print(sensor.value)
    if sensor.value is True:
        motor.value = True
    else:
        motor.value = False
    time.sleep(0.1)

