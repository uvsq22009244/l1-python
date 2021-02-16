import tkinter as tk
import random as rd

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def draw_pixel(i, j, color):
    """ Colorie le pixel de coordonnées (i,j) de la couleur color """
    canvas.create_line((i, j), (i+1, j), fill=color)

def ecran_aleatoire():
    for i in range(256):
        for j in range(256):
            color = get_color(rd.randint(0,255), rd.randint(0,255), rd.randint(0,255))
            draw_pixel(i, j, color)

def degrade_gris():
    for i in range(256):
        color = get_color(i, i, i)
        for j in range(256):
            draw_pixel(i, j, color)


def degrade_2D():
    for i in range(256):
        for j in range(256):
            color = get_color(i, 0, j)
            draw_pixel(i, j, color)


racine = tk.Tk()
# création des widgets\n",
bouton_aleatoire = tk.Button(racine, text="Aléatoire", bg="grey100", fg="blue", padx=20, font=("Times", "20"), command=ecran_aleatoire)
bouton_degrade_gris = tk.Button(racine, text="Dégradé gris", bg="grey100", fg="blue", padx=20, font=("Times", "20"), command=degrade_gris)
bouton_degrade_2D = tk.Button(racine, text="Dégradé 2D", bg="grey100", fg="blue", padx=20, font=("Times", "20"), command=degrade_2D)
canvas = tk.Canvas(racine, width=256, height=256, bg="black")

# placement des widgets\n",
bouton_cercle.grid(column=0, row=1)
bouton_carre.grid(column=0, row=2)
bouton_croix.grid(column=0, row=3)
canvas.grid(column=1, row=1, rowspan=3)

racine.mainloop()
