from turtle import *

setup(500, 500)

def porte():
    up()
    goto(-200, -100)
    down()
    pensize(2)
    left(90)
    for i in range(2):
        forward(60)
        right(90)
        forward(40)
        right(90)

print(porte())
