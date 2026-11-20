# Import Library
from djitellopy import Tello
from math import *

n=int(input("Inserisci il numero dei lati: "))
lato=20

# Tello Setup
drone = Tello()
drone.connect()



# Take off
drone.takeoff()
#                   X   Y   Z  speed

drone.go_xyz_speed(0,30,30,20)

drone.land()