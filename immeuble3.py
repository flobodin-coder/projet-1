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

def immeuble(x,y,hauteur) :
    axe_x = [-355, -175, 5, 185]
    etage = 0
    for x in axe_x:
        color = (randint(0,255),randint(0,255),randint(0,255))
        rect(x, -100, 140,60, color)
        
    





etage()
done()



