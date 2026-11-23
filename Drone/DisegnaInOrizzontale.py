# Su Windows, ricordarsi di disabilitare il firewall, sia di dominio, pubblico e privato
# Includo la libreria del drone
from djitellopy import Tello

lunghezza=50
lati=0
contatore=0

while (lati<3):
    lati=int(input("Inserisci il numero dei lati: "))

# Creo il drone
drone = Tello()
# Mi connetto in wi-fi
drone.connect()
# Decollo: il drone si alza di circa 80 cm
drone.takeoff()

# aumentiamo la quota di 50 cm
drone.move_up(50)



# Disegna il lato e gira a destra per n volte 
while (contatore<lati):
    drone.move_forward(lunghezza)
    drone.rotate_clockwise(int(360/lati))
    contatore=contatore+1

# Capovolta in avanti
drone.flip_forward()
# Atterraggio
drone.land()