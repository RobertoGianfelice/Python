# Import Library
from djitellopy import Tello
from math import *
import time

n=int(input("Inserisci il numero dei lati: "))
lato=5

# Tello Setup
drone = Tello()
drone.connect()

drone.enable_mission_pads()

drone.set_mission_pad_detection_direction(0)

# Take off
drone.takeoff()
time.sleep(2)



pad_id=drone.get_mission_pad_id()
if pad_id!=-1:
    print("ok")
else:
    print("ko")

x=0
y=30
z=10
x=drone.get_mission_pad_distance_x()
y=drone.get_mission_pad_distance_y()
z=drone.get_mission_pad_distance_z()
x0=x
y0=y
z0=z
print(f"x={x0}, y={y0}, z={z0}")
drone.go_xyz_speed(x0,y0,z0,20)

#drone.move_up(50)
# Rotate clockwise 
for i in range(1,n):
    x=x
    y=y+int(lato*cos((i*2*pi)/n))
    z=z+int(lato*sin((i*2*pi)/n))
    #                   X   Y   Z  speed
    print(f"x={x}, y={y}, z={z}")
    drone.go_xyz_speed(x,y,z,20)
print(f"x={x0}, y={y0}, z={z0}")
drone.go_xyz_speed(x0,y0,z0,20)


# Rotate counter clockwise 180 degree
#drone.flip_forward()
# Landing
drone.land()