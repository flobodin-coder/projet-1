from turtle import *
from random import *

setup(1000, 500)
colormode(255)
speed(10)

def rect(x, y, largeur, hauteur,couleur):
    up()
    goto(x, y)
    down()
    fillcolor(couleur)
    pencolor("Black")
    begin_fill()
    forward(largeur)
    left(90)
    forward(hauteur)
    left(90)
    forward(largeur)
    left(90)
    forward(hauteur)
    left(90)
    end_fill()

def immeuble(x) :
    axe_x = [-355, -175, 5, 185]
    hauteur = 0
    for x in axe_x:
        etage = randint(1,5)
        if etage == 1:
            hauteur = 60
        elif etage == 2:
            hauteur = 120
        elif etage == 3:
            hauteur = 180
        else:
            hauteur = 240
        color = (randint(0,255),randint(0,255),randint(0,255))
        rect(x, -100, 140, hauteur, color)
    
    


immeuble(0)
done()



