# https://id-studiolab.github.io/Digital-Interfaces/assignments/05-walkie-talkie/index


##--- Library Imports
import time
import digitalio
import board
import neopixel

from MQTT import Create_MQTT
from settings import settings

##--- Defining states
state_idle = 0
state_receive = 1
state_channel_open = 2
state_transmit = 3

current_state = 0

# Define variable to save data received from the MQTT broker
last_received_value = 0

##--- Button variables
open_channel_pin = board.D13
open_channel_button = digitalio.DigitalInOut(open_channel_pin)
open_channel_button.direction = digitalio.Direction.INPUT

speak_channel_pin = board.D7
speak_button = digitalio.DigitalInOut(speak_channel_pin)
speak_button.direction = digitalio.Direction.INPUT

##-- Led variables
pin_leds = board.D3
num_leds = 1
leds = neopixel.NeoPixel(pin_leds, num_leds, auto_write=False, pixel_order=neopixel.GRBW)

led_off = (0, 0, 0, 0)
led_red = (255, 0, 0, 0)
led_blue = (0, 0, 255, 0)
led_green = (0, 255, 0, 0)
led_white = (0, 0, 0, 255)

def set_led_color(color):
    global leds
    leds.fill(color)
    leds.show()

##--- Actuator variables
actuator = digitalio.DigitalInOut(board.D4)
actuator.direction = digitalio.Direction.OUTPUT

# For more information on how to use PWM check this link: 
# https://id-studiolab.github.io/Connected-Interaction-Kit/components/piezo-buzzer/piezo-buzzer.html#define-a-tone-using-pulse-width-modulation-pwm

#actuator = pwmio.PWMOut(board.D4, variable_frequency=True)

##--- MQTT configuration

# Define variable to save data received from the MQTT broker
last_received_value = 0
device_has_received_new_value = False
   
# Method used when the board receives a message from the MQTT server.
def handle_message(client, topic, msg):
    global last_received_value
    global device_has_received_new_value

    # Assign message received to last_received variable
    last_received_value = msg

    device_has_received_new_value = True


# You can find the client Id in the settings.py this is used to identify the board
client_id = settings["mqtt_clientid"]

# Create a mqtt connection based on the settings file.
mqtt_client = Create_MQTT(client_id, handle_message)



# <-------------------------------------------->
# -- DEFINE YOUR SPEAK AND LISTEN TOPIC HERE --
# VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV


# Here you should select the topic of the person you want to talk to.
# Write the topic you want to send messages to.
mqtt_speak_topic = "Studio05-Lisa-WalkieTalkie"

# You should set as "listen_topic" their "speak_topic" and vice-versa
mqtt_listen_topic = "Studio05-Bram-WalkieTalkie"


# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# <-------------------------------------------->



# Listen for messages on the topic specified above
mqtt_client.subscribe(mqtt_listen_topic)

##--- Main loop
while True: 
    try:
        mqtt_client.loop(0.1)

    except (ValueError, RuntimeError) as e:
        print("Failed to get data, retrying\n", e)
        mqtt_client.reconnect()
        continue
    # ---------------------------------------------
    # ^ DO NOT CHANGE ANYTHING ABOVE THIS POINT ^ |
    # ---------------------------------------------

    message = "ping"

    # Use this method to publish messages on a topic:
    # mqtt_client.publish(mqtt_speak_topic, message)

    # ----------------------------------------------------------------|
    #                                                                 |
    # Use the Acting Machine Diagram to program your solution here    |
    #                                                                 |
    # Hint: Use of the "device_has_received_new_value" variable       |
    #       Use the open_channel_button and speak_button variables    |
    #       Use the led variable (copied from the reation game code)  |
    # ----------------------------------------------------------------|



    # ----------------------------------------------
    # v DO NOT CHANGE ANYTHING BELOW THIS POINT v  |
    # ----------------------------------------------
    device_has_received_new_value = False
    time.sleep(0.1)
