import turtle
import time

n=0
lato=50
while (n<3):
    n=int(input("Inserisci il mnumero di lati: "))
    
tarta=turtle.Turtle()
screen=turtle.Screen()
tarta.speed(20)
screen.colormode(255)

for i in range(n):
    tarta.forward(40)
    time.sleep(1)
    tarta.right(360/n)
    time.sleep(1)

screen.exitonclick()