# Includo la libreria del drone
from djitellopy import Tello

lato=40
n=0

while (n<3):
    n=int(input("Inserisci il numero dei lati: "))

# Creo il drone
drone = Tello()

# Mi connetto in wi-fi
drone.connect()

# Decollo: il drone si alza di circa 80 cm
drone.takeoff()

# aimentiamo la quota di 50 cm
drone.move_up(50)

# Disegna il lato e gira a destra per n volte 
for i in range(n):
    drone.move_forward(lato)
    drone.rotate_clockwise(int(360/n))

# Capovolta in avanti
drone.flip_forward()
# Atterraggio
drone.land()