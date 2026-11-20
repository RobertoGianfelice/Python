# Import Library
from djitellopy import Tello

n=int(input("Inserisci il numero dei lati: "))

# Tello Setup
drone = Tello()
drone.connect()

# Take off
drone.takeoff()

drone.move_up(50)

# Rotate clockwise 
for i in range(n):
    drone.move_forward(40)
    drone.rotate_clockwise(int(360/n))

# Rotate counter clockwise 180 degree
drone.flip_forward()
# Landing
drone.land()