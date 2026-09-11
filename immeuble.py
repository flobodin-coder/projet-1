from turtle import *
from random import rd 

setup(500, 500)

def porte():

    """immeuble"""


 










    """porte"""
    up()
    goto(-200, -100)
    begin_fill()
    fillcolor(rd.choice(["brown", "black", "gray"]))
    down()
    goto(-200, -50)
    goto(-170, -50)
    goto(-170, -100)
    goto(-200, -100)
    end_fill()


print(porte())
