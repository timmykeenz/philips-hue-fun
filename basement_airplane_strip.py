from phue import Bridge
import time

# Bridge IP
b = Bridge('192.168.1.3')

b.connect()

lights = b.get_light_objects('name')

i = 0
delay_time = 1

# Setup lights
for light in ['Jerry', 'Larry', 'Bob']:
  lights[light].on = True
  lights[light].transitiontime = 10

while True:
  if i == 0:
    lights['Bob'].brightness = 1
    lights['Jerry'].brightness = 255
  if i == 1:
    lights['Jerry'].brightness = 1
    lights['Larry'].brightness = 255
  if i == 2:
    lights['Larry'].brightness = 1
    lights['Bob'].brightness = 255


  time.sleep(delay_time)
  i += 1

  if i > 2:
    i = 0


