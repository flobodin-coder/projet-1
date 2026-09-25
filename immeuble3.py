from turtle import *
import random 

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


def fenetre(x, y):
    rect(x, y, 30, 30,"white")

def porte(x, y):
     rect(x, y, 30, 50, "brown")


def rez_chaussé(x, y, couleur):
    rect(x, y, 140, 60, couleur)
    position = (random.randint(0, 2))
    if position == 0:
        porte(x + 15, y)
        fenetre(x + 55, y + 15)
        fenetre(x + 95, y + 15)
    elif position == 1:
        fenetre(x + 15, y + 15)
        porte(x + 55, y)
        fenetre(x + 95, y + 15)
    elif position == 2:
        fenetre(x + 15, y + 15)
        fenetre(x + 55, y + 15)
        porte(x + 95, y)
    

def etage(x, y, couleur):
    rect(x, y, 140, 60, couleur)
    fenetre(x + 15, y + 15)
    fenetre(x + 55, y + 15)
    fenetre(x + 95, y + 15)


def immeuble(x, y):
    #color = random.choice( ["blue", "orange", "red", "green", "purple"])
    couleur = "blue"
    rez_chaussé(x, y, "blue")
    nb_etage = random.randint(1,5)
    if nb_etage == 1:
        etage(x , y + 60, couleur)
    elif nb_etage == 2:
        etage(x , y + 60, couleur)
        etage(x , y + 120, couleur)
    elif etage == 3:
        etage(x , y + 60, couleur)
        etage(x , y + 120, couleur)
        etage(x , y + 180, couleur)
    elif nb_etage == 4:
        etage(x , y + 60, couleur)
        etage(x , y + 120, couleur)
        etage(x , y + 180, couleur)
        etage(x , y + 240, couleur)


        


        

axe_x = [-355, -175, 5, 185]

immeuble(-355, -100)
done()


# placement =-340, -300 -260
# 15 - 30 - 10 - 30 - 10 - 30 - 15





     






done()



