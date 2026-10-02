from turtle import *
import random 

setup(1000, 500)
colormode(255)
speed(100)

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


def couleur_aleatoire():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def fenetre(x, y):
    rect(x, y, 30, 30,"white")



def porte1(x, y):
    rect(x, y, 30, 50, couleur_aleatoire())


def porte2(x, y):
    couleur = couleur_aleatoire()
    rect(x, y, 30, 35, couleur)
    up()
    goto(x + 30, y + 35)
    setheading(90)
    down()
    fillcolor(couleur)
    begin_fill()
    circle(15, 180)
    end_fill()
    setheading(0)


def porte(x, y):
    if random.randint(0, 1) == 0:
        porte1(x, y)
    else:
        porte2(x, y)


def balcon(x, y):
    rect(x, y, 30, 15, "lightgray")
    for i in range(1, 6):
        up()
        goto(x + i * 5, y)
        setheading(90)
        down()
        forward(15)
    setheading(0)


def porte_fenetre(x, y):
    rect(x, y, 30, 50, "white")
    balcon(x, y)


def ouverture(x, y):
    if random.randint(0, 1) == 0:
        fenetre(x, y + 15)
    else:
        porte_fenetre(x, y)



def toit1(x, y):
    up()
    goto(x - 5, y)
    down()
    fillcolor("black")
    begin_fill()
    goto(x + 145, y)
    goto(x + 70, y + 25)
    goto(x - 5, y)
    end_fill()


def toit2(x, y):
    rect(x - 5, y, 150, 6, "black")


def toit(x, y):
    if random.randint(0, 1) == 0:
        toit1(x, y)
    else:
        toit2(x, y)


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
    ouverture(x + 15, y)
    ouverture(x + 55, y)
    ouverture(x + 95, y)


def immeuble(x, y):
    axe_x = [-355, -175, 5, 185]
    up()
    goto(-450, y)
    setheading(0)
    pencolor("Black")
    down()
    goto(450, y)
    for i in axe_x:
        couleur = couleur_aleatoire()          # CORRIGÉ : couleur aléatoire
        rez_chaussé(i, y, couleur)
        nb_etage = random.randint(0, 4)        # CORRIGÉ : 0 à 4 étages
        if nb_etage == 1:
            etage(i , y + 60, couleur)
        elif nb_etage == 2:
            etage(i , y + 60, couleur)
            etage(i , y + 120, couleur)
        elif nb_etage == 3:                    # CORRIGÉ : etage -> nb_etage
            etage(i , y + 60, couleur)
            etage(i , y + 120, couleur)
            etage(i , y + 180, couleur)
        elif nb_etage == 4:
            etage(i , y + 60, couleur)
            etage(i , y + 120, couleur)
            etage(i , y + 180, couleur)
            etage(i , y + 240, couleur)
        toit(i, y + 60 * (nb_etage + 1))       # AJOUT : le toit


immeuble(-355, -100)
done()







done()

