import time
from djitellopy import Tello
from threading import Thread
import cv2
atterrato=0

# Tello Setup
tello = Tello()
tello.connect()
tello.set_speed(100)
def volo(mytello,n,lato,quota):
    
    # Take off
    global atterrato

    for i in range(10):
        print (10-i)
        time.sleep(1)
    print ("DECOLLO!!!!!!!!!!")
    mytello.takeoff()
    # Move up 20 cm
    mytello.move_up(quota)
    for i in range(n):
        mytello.move_forward(lato)
        mytello.rotate_clockwise(int(360/n))
        #time.sleep(2)
    
    # Landing
    print("Quota Tello: ", mytello.get_height())

    mytello.land()
    print("Quota Tello: ", mytello.get_height())
    atterrato=1

n=int(input("Inserisci i lati del poligono: "))
lato=max(20,int(input("Inserisci la lunghezza dei lati del poligono in cm (min 20): ")))
quota=max(20,int(input("Inserisci la quota a cui disegnare il poligono in cm (min 20): ")))


t1 = Thread(target=volo, args=(tello,n,lato,quota))
t1.start()

tello.streamon()
# Read the frame from video streaming
cap = tello.get_frame_read()
warning=0
print("Quota Tello: ", tello.get_height())

while True:
    # Get the video frame
    frame = cap.frame
    # Show the window
    cv2.imshow("Tello Video Stream", frame)
    # Press the 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if (atterrato==1):
        break
    # Print the battery level
    if (tello.get_battery() and warning==0):
        print("Low Battery")
        warning=1
t1.join()
tello.streamoff()
# Destroy the video window
cv2.destroyAllWindows()


print("Done!")