# https://id-studiolab.github.io/Connected-Interaction-Kit/tutorials/adding-inputs-and-outputs/part-1.html
import board
import digitalio
import time

sensor = digitalio.DigitalInOut(board.D2)
sensor.direction = digitalio.Direction.INPUT

while True:
    print(sensor.value)
    time.sleep(0.1)
