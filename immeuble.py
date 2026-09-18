from turtle import *
from random import *

setup(1000, 500)
colormode(255)

def projet():

    
    """maison 1"""

    up()
    goto(-175, -100)
    color = (randint(0,255),randint(0,255),randint(0,255))
    pencolor(color)
    fillcolor(color)
    down()
    begin_fill()
    forward(140)
    left(90)
    forward(60)
    left(90)      
    forward(140)
    left(90)
    forward(60)
    end_fill()



    """maison 2"""
    
    up()
    left(90)
    goto(-355, -100)
    color = (randint(0,255),randint(0,255),randint(0,255))
    pencolor(color)
    fillcolor(color)
    down()
    begin_fill()
    forward(140)
    left(90)
    forward(60)
    left(90)      
    forward(140)
    left(90)
    forward(60)
    end_fill()


    """maison 3"""
    
    up()
    left(90)
    goto(5, -100)
    color = (randint(0,255),randint(0,255),randint(0,255))
    pencolor(color)
    fillcolor(color)
    down()
    begin_fill()
    forward(140)
    left(90)
    forward(60)
    left(90)      
    forward(140)
    left(90)
    forward(60)
    end_fill()


    """maison 4"""
    
    up()
    left(90)
    goto(185, -100)
    color = (randint(0,255),randint(0,255),randint(0,255))
    pencolor(color)
    fillcolor(color)
    down()
    begin_fill()
    forward(140)
    left(90)
    forward(60)
    left(90)      
    forward(140)
    left(90)
    forward(60)
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

