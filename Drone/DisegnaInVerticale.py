# Import Library
from djitellopy import Tello
from math import *
import time

n=int(input("Inserisci il numero dei lati: "))
lato=20

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

x=drone.get_mission_pad_distance_x()
y=drone.get_mission_pad_distance_y()
z=drone.get_mission_pad_distance_z()
x0=x
y0=y
z0=z
print(f"x={x0}, y={y0}, z={z0}")
drone.go_xyz_speed_mid(x0,y0,z0,10, pad_id)

for i in range(n):
    x=x
    y=y-lato*cos((i*2*pi)/n)
    z=z+lato*sin((i*2*pi)/n)
    #                   X   Y   Z  speed
    print(f"x={x}, y={y}, z={z}")
    drone.go_xyz_speed_mid(x0,y0,z0,10, pad_id)
    time.sleep(1)

print(f"x={x0}, y={y0}, z={z0}")
drone.go_xyz_speed_mid(x0,y0,z0,10,pad_id)

# Landing
drone.land()