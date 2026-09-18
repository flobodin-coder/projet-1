from turtle import *
from random import random as rd

setup(500, 500)

def sol():

    """sol"""
    up()
    goto(-220, -100)
    down()
    forward(420)


def immeuble():
    up()
    goto(-200, -50)
    down()
    pencolor(rd.randint(0,255))
    pencolor(rd.randint(0,255))
    pencolor(rd.randint(0,255))                 
    forward(500)

print(sol)   
print(immeuble) 


"""porte
up()
goto(-200, -100)
begin_fill()
down()
goto(-200, -50)
goto(-170, -50)
goto(-170, -100)
goto(-200, -100)
end_fill()"""













