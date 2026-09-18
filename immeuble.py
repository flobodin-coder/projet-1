from turtle import *
from random import *

setup(1000, 500)
colormode(255)
speed(10)

def projet():

    
    """maison 1"""


    # position et couleur
    up()
    goto(-355, -100)
    color = (randint(0,255),randint(0,255),randint(0,255))
    pencolor(color)
    fillcolor(color)
    down()


    #taille de l'immeuble
    etage = randint(1,5)
    if etage == 1:
        nb = 60
    elif etage == 2:
        nb = 120
    elif etage == 3:
        nb = 180
    elif etage == 4:
        nb = 240
    else:
        nb = 300


    #remplissage
    begin_fill()
    forward(140)
    left(90)
    forward(nb)
    left(90)      
    forward(140)
    left(90)
    forward(nb)
    end_fill()


    #fenetre

    i = 0
    up()
    goto(-340, -60)
    down()
    fillcolor(255, 255, 255)
    pencolor(0, 0, 0)
    begin_fill()
    for j in range(0,4):
        while i != 4 :
            forward(30)
            left(90)
            i += 1
        up()
        goto(-340, -60)
        left(90)
        forward(40)   
    end_fill()





    """maison 2"""


    # position et couleur
    up()
    left(90)
    goto(-175, -100)
    color = (randint(0,255),randint(0,255),randint(0,255))
    pencolor(color)
    fillcolor(color)
    down()


    #taille de l'immeuble
    etage = randint(1,5)
    if etage == 1:
        nb = 60
    elif etage == 2:
        nb = 120
    elif etage == 3:
            nb = 180
    elif etage == 4:
        nb = 240
    else:
        nb = 300


    #remplissage
    begin_fill()
    forward(140)
    left(90)
    forward(nb)
    left(90)      
    forward(140)
    left(90)
    forward(nb)
    end_fill()


    """maison 3"""


    # position et couleur
    up()
    left(90)
    goto(5, -100)
    color = (randint(0,255),randint(0,255),randint(0,255))
    pencolor(color)
    fillcolor(color)
    down()


    #taille de l'immeuble
    etage = randint(1,5)
    if etage == 1:
        nb = 60
    elif etage == 2:
        nb = 120
    elif etage == 3:
        nb = 180
    elif etage == 4:
        nb = 240
    else:
        nb = 300


    #remplissage
    begin_fill()
    forward(140)
    left(90)
    forward(nb)
    left(90)      
    forward(140)
    left(90)
    forward(nb)
    end_fill()


    """maison 4"""

    # position et couleur
    up()
    left(90)
    goto(185, -100)
    color = (randint(0,255),randint(0,255),randint(0,255))
    pencolor(color)
    fillcolor(color)
    down()


    #taille de l'immeuble
    etage = randint(1,5)
    if etage == 1:
        nb = 60
    elif etage == 2:
        nb = 120
    elif etage == 3:
        nb = 180
    elif etage == 4:
        nb = 240
    else:
        nb = 300

        
    #remplissage
    begin_fill()
    forward(140)
    left(90)
    forward(nb)
    left(90)      
    forward(140)
    left(90)
    forward(nb)
    end_fill()







    pencolor(0 ,0, 0)
    pensize(3)
    up()
    left(90)
    goto(-400, -100)
    down()
    forward(800)







    return None


print(projet()) 














done()

