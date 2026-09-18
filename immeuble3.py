from turtle import *
from random import *

setup(1000, 500)

def rect(x, y, largeur, hauteur,couleur):
    up()
    goto(x, y)
    down()
    fillcolor(couleur)
    pencolor(couleur)
    begin_fill
    forward(largeur)
    left(90)
    forward(hauteur)
    left(90)
    forward(largeur)
    left(90)
    forward(hauteur)
    left(90)
    end_fill

def etage(x, ) :
    axe_x = [-355, -175, 5, 185]
    color = (randint(0,255),randint(0,255),randint(0,255))
    for x in axe_x:
        rect(x, -100, 140,60, color)





done()



