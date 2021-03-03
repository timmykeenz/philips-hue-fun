from phue import Bridge
import time

# Bridge IP
b = Bridge('192.168.1.3')

b.connect()

lights = b.get_light_objects('name')

light_speed = .25
i = 0
# Set the lights
while True:
  i = 0
  while i < 3:
    # Turn off the previous light
    if i - 1 < 0:
      lights['Dining Room 3'].brightness = 128
    else:
      lights['Dining Room ' + str(i)].brightness = 128
    # Turn on the lights
    lights['Dining Room ' + str(i + 1)].transitiontime = light_speed * 10
    lights['Dining Room ' + str(i + 1)].on = True
    lights['Dining Room ' + str(i + 1)].brightness = 255
    time.sleep(light_speed)
    i += 1