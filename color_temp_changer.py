from phue import Bridge
import time

# Bridge IP
b = Bridge('192.168.1.3')

b.connect()

lights = b.get_light_objects('name')

# Set the lights
for light in ['Living Room 1', 'Living Room 2']:
  lights[light].on = True
  lights[light].brightness = 255

i = 0
maxIterations = 5
while i < maxIterations:
  for light in ['Living Room 1', 'Living Room 2']:
  	# Top color temp is 6500k
    lights[light].colortemp_k = 6500
  time.sleep(1)
  for light in ['Living Room 1', 'Living Room 2']:
  	# Bottom color temp is 2000k
    lights[light].colortemp_k = 2000
  time.sleep(1)
  # Increment i so we eventually break the loop
  i += 1

# Tear down the lights
for light in ['Living Room 1', 'Living Room 2']:
  lights[light].on = False