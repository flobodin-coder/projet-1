from turtle import *
from random import *

setup(1000, 500)
colormode(255)
speed(10)

axe_x = [-355, -175, 5, 185]
axe_y = [-100]
largeur = 140
longueur = 60


for x in axe_x:
    teleport(x, axe_y)
    color = (randint(0,255),randint(0,255),randint(0,255))
    pencolor(color)
    fillcolor(color)

    begin_fill()
    forward(largeur)
    left(90)
    forward(longueur)
    left(90)
    forward(largeur)
    left(90)
    forward(longueur)
    left(90)


"""def rez_chaussé (x, y, largeur, longueur):

    for i in range(4):
        
        color = (randint(0,255),randint(0,255),randint(0,255))
        pencolor(color)
        fillcolor(color)

        begin_fill()
        forward(largeur)
        left(90)
        forward(longueur)
        left(90)
        forward(largeur)
        left(90)
        forward(longueur)
        left(90)"""
















"""def immeuble():
    rez_chaussé()
    pencolor(color)
    fillcolor(color)
    etage = randint(1-4)
    if etage == 1:
        nb = 60
    elif etage == 2:
        nb = 120
    elif etage == 3:
        nb = 180
    else :
        nb = 240

    begin_fill()

    end_fill()"""



    






done()
