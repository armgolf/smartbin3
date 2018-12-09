import time #required for pausing the script
import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
import requests
import os
import json
from gpiozero import DistanceSensor
import photo
import identify
import rotate
import openplate
import itemsensor
import door

#an object has been put in the bin, rotate, and identify the object
def binstatus1(items):
    object = itemsensor()
    open = door.door()
    while object == False and open == True:
        object = itemsensor()
        open = door.door()
    if object == True:
        time.sleep(2)
        rotate.rotate() #rotate objects in the top compartment 90 degrees and update items
        photo.photo() #capture image of the object and assign it to variable
        a = identify.identify() #identify object in the image captured
        time.sleep(7) #wait 7 seconds for object identification
        items[1] = a #assign object type to compartments array
        print(items)
        return(items)
    if object == False and open == False:
        return(items)

#the door is closed, empty any compartments which contain items
def binstatus2(items):
    while items != [0,0,0,0]:
        open = door.door()
        #for each element of the items array
        for i in range(1, 4):
            open = door.door()
            #check if the object is equal to the bottom compartment category
            if items[i-1] == i:
                platenumber = i
                #if object matches compartment category, empty the compartment
                openplate.openplate()
                items[i] = 0
                rotate.rotate()
            else:
                rotate.rotate()
            if open == True:
                break
    return(items)

#initialise items array
items = [0,0,0,0]
power = True
while power == True:
    open = door.door()
    #if an object has been input to the bin, rotate and identify it
    if open == True:
        items = binstatus1(items)

    #check if another object is about to be input to the bin
    open = door.door()
    #while the door is open wait for object to be input or door to close
    if open == False:
        binstatus2(items)
