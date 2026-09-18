from turtle import *
from random import *

setup(1000, 500)
colormode(255)
speed(10)

def rectangle ():

    for i in range(4):
        teleport(-355 + i * 170 , -100)

        color = (randint(0,255),randint(0,255),randint(0,255))
        pencolor(color)
        fillcolor(color)

        begin_fill()
        forward(140)
        left(90)
        forward(60)
        left(90)      
        forward(140)
        left(90)
        forward(60)
        left(90)
        end_fill()


    return None

def etage():

rectangle()

done()
