from gpiozero import DistanceSensor
from time import sleep

#proximity sensor to identify when the door is open or closed
def door():
    sensor = DistanceSensor(echo=19, trigger=26)
    object = False
    count = 0
    #check 5 times in 5 seconds, set object variable accordingly
    for x in range(2):
        dist = sensor.distance * 100
        if dist > 10:
            count = count + 1
            if count == 2:
                open = True
        sleep(1)
    return(open)
