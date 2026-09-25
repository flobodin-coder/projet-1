

def immeuble(x) :
    global axe_x

    hauteur = 0
    for x in axe_x:
        etage = randint(1,5)
        if etage == 1:
            hauteur = 60
        elif etage == 2:
            hauteur = 120
        elif etage == 3:
            hauteur = 180
        else:
            hauteur = 240

        rect(x, -100, 140, hauteur, color)


def porte(x, h_porte, l_porte):
    global axe_x
    position = (randint(0, 2))
    for i in axe_x:
            if position == 0:
                x = axe_x[0] - 15
                goto(x, -100)
            elif position == 1:
                x = axe_x[0] - 55
                goto(x, -100)
            elif position == 2 :
                x = axe_x - 95

            pencolor("black")
            fillcolor("white")
            begin_fill()
            forward(l_porte)
            left(90)
            forward(h_porte)
            left(90)
            forward(l_porte)
            left(90)
            forward(h_porte)
            end_fill()
