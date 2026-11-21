# importo le librerie della tartaruga e della gestione del tempo
import turtle
import time

n=0
lato=50
while (n<3):
    n=int(input("Inserisci il numero di lati: "))
    
# Faccio "nascere" una tartaruga
tarta=turtle.Turtle()

# Preparo la "tela" per il disegno
screen=turtle.Screen()
tarta.speed(20)
screen.colormode(255)

# Per n volte, disegno un lato e poi mi giro
for i in range(n):
    tarta.forward(lato)
    time.sleep(1)
    tarta.right(360/n)
    time.sleep(1)

# Quando hai finito, clicca sulla tela
screen.exitonclick()