import setup
from setup import RPL
import post_to_web as PTW # see post_to_web.py for instructions

sensor_pin = 16
RPL.pinMode(sensor_pin,RPL.INPUT)
x = 1

while True:
  if x == 1:
     import time
     import setup
     from setup import RPL
     import RoboPiLib as RPL
     start = time.time()
     start = int(start)
     if start == 3:
        import RoboPiLib as RPL
        import setup
        RPL.servoWrite(0,0)
        RPL.servoWrite(1,0)
        exit
      
  if RPL.digitalRead(sensor_pin) == 1:
     import RoboPiLib as RPL
     import setup
     RPL.servoWrite(0,1000)
     RPL.servoWrite(1,2000)
     
  if RPL.digitalRead(sensor_pin) == 0:
     import RoboPiLib as RPL
     import setup
     RPL.servoWrite(0,1450)
     RPL.servoWrite(1,1550)
     x = 1
     
      
     while True:
        elapsed = (time.time() - start)
        elapsed = int(elapsed)
        if elapsed % 1 == 3:
          import robooff
          execfile(robooff)
          


