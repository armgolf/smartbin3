from gpiozero import DistanceSensor
from time import sleep

#proximity sensor to identify presence of an object in bin entry compartment
def itemsensor():
    sensor = DistanceSensor(echo=24, trigger=23)
    object = False
    count = 0
    #check 5 times in 5 seconds, set object variable accordingly
    for x in range(5):
        dist = sensor.distance * 100
        if dist < 10:
            count = count + 1
            if count == 5:
                object = True
        sleep(1)
    return(object)
