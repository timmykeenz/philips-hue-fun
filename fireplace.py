from phue import Bridge
from threading import Thread
import time, random

# Bridge IP
b = Bridge('192.168.1.3')

b.connect()

# Function to replicate the fire
def fire_light(light):
  while True:
    # Grab the color of the bulb in kelvin
    color_temp = random.randint(2000, 3500)
    # Determine the brightness
    brightness = random.randint(0, 255)
    # Determine the time needed to change colors
    transition_time = random.randint(1, 25)
    # Adjust the light settings
    light.brightness = brightness
    light.transitiontime = transition_time
    light.colortemp_k = color_temp
    # Sleep till the transition is complete
    time.sleep(transition_time / 10)
    
# Grab all the lights
lights = b.get_light_objects('name')

# Turn on the lights
for light in ['Living Room 1', 'Living Room 2']:
  lights[light].on = True

thread_one = Thread(target=fire_light, kwargs={'light':lights['Living Room 1']})
thread_two = Thread(target=fire_light, kwargs={'light':lights['Living Room 2']})
thread_one.start()
thread_two.start()

print('Fire place started')