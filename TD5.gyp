    "# TD 5: Interface graphique\n",
    
    "## 1. Prise en main\n",

import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400

root = tk.Tk()
canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

# Début de votre code
x = CANVAS_WIDTH // 2
y1 = 100
y2 = CANVAS_HEIGHT - 100
canvas.create_line(x, y1, x, y2)
canvas.create_oval(x - 50, y1 + 50, x + 50, y1 - 50)
canvas.create_oval(x - 50, y2 + 50, x + 50, y2 - 50)
canvas.create_oval(x - 50, (y1 + y2) // 2 + 50, x + 50, (y1 + y2) // 2 - 50)

# Fin de votre code
canvas.pack()
#Lance l'attente des événements d'action de l'utilisateur pour leur traitement
root.mainloop()
 

    "## 2. Dessins aléatoires\n",


import tkinter as tk
import random as rd

def cercle():
    x = rd.randint(0, 400)
    y = rd.randint(0, 400)
    canvas.create_oval((x, y), (x+100, y+100), fill=color)

def carre():
    x = rd.randint(0, 400)
    y = rd.randint(0, 400)
    canvas.create_rectangle((x, y), (x+100, y+100), fill=color)

def croix():
    x = rd.randint(0, 400)
    y = rd.randint(0, 400)
    canvas.create_line((x, y), (x+100, y+100), fill=color)
    canvas.create_line((x+100, y), (x, y+100), fill=color)

def choisir_couleur():
    global color
    color = input("Choisis une couleur: ")

color = "blue"
racine = tk.Tk()
racine.title("Mon dessin")

# création des widgets\n",
bouton_cercle = tk.Button(racine, text="Cercle", bg="grey100", fg="blue", padx=20, font=("Times", "20"), command=cercle)
bouton_carre = tk.Button(racine, text="Carré", bg="grey100", fg="blue", padx=20, font=("Times", "20"), command=carre)
bouton_croix = tk.Button(racine, text="Croix", bg="grey100", fg="blue", padx=20, font=("Times", "20"), command=croix)
bouton_couleur = tk.Button(racine, text="Choisir une couleur", bg="grey100", fg="blue", padx=20, font=("Times", "20"), command=choisir_couleur)
canvas = tk.Canvas(racine, width=500, height=500, bg="black", bd=10, relief="raised")

# placement des widgets\n",
bouton_cercle.grid(column=0, row=1)
bouton_carre.grid(column=0, row=2)
bouton_croix.grid(column=0, row=3)
bouton_couleur.grid(column=1, row=0)
canvas.grid(column=1, row=1, rowspan=3)

racine.mainloop()


    "## 3. Cible en couleur\n",


import tkinter as tk

COTE = 500
colors = ["blue", "green", "black", "yellow", "magenta", "red"]
nb_cercles = 30
racine = tk.Tk()
canvas = tk.Canvas(racine, width=COTE, height=COTE, bg="black")
canvas.grid()
epaisseur = (COTE // 2) // nb_cercles
for i in range(nb_cercles):
    canvas.create_oval((epaisseur*i, epaisseur*i),
                        (COTE-epaisseur*i, COTE-epaisseur*i),
                         fill=colors[i % len(colors)],
                         outline=colors[i % len(colors)]
                        )
racine.mainloop()


    "## 4. Couleurs\n",


mport tkinter as tk
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
bouton_cercle = tk.Button(racine, text="Aléatoire", bg="grey100", fg="blue", padx=20, font=("Times", "20"), command=ecran_aleatoire)
bouton_carre = tk.Button(racine, text="Dégradé gris", bg="grey100", fg="blue", padx=20, font=("Times", "20"), command=degrade_gris)
bouton_croix = tk.Button(racine, text="Dégradé 2D", bg="grey100", fg="blue", padx=20, font=("Times", "20"), command=degrade_2D)
canvas = tk.Canvas(racine, width=256, height=256, bg="black")

# placement des widgets\n",
bouton_cercle.grid(column=0, row=1)
bouton_carre.grid(column=0, row=2)
bouton_croix.grid(column=0, row=3)
canvas.grid(column=1, row=1, rowspan=3)

racine.mainloop()

   
    "## 5. Fonction undo\n",


import tkinter as tk
import random as rd

objets=[]

def cercle():
    global objets
    x = rd.randint(0, 400)
    y = rd.randint(0, 400)
    objets.append(canvas.create_oval((x, y), (x+100, y+100), fill=color))

def carre():
    global objets
    x = rd.randint(0, 400)
    y = rd.randint(0, 400)
    objets.append(canvas.create_rectangle((x, y), (x+100, y+100), fill=color))

def croix():
    global objets
    x = rd.randint(0, 400)
    y = rd.randint(0, 400)
    objets.append(canvas.create_line((x, y), (x+100, y+100), fill=color))
    objets.append(canvas.create_line((x+100, y), (x, y+100), fill=color))

def choisir_couleur():
    global color
    color = input("Choisis une couleur: ")

def undo():
    repeat = 1
    if len(objets) != 0:   
        if canvas.type(objets[-1]) == "line":
            repeat = 2
        for i in range(repeat):
            canvas.delete(objets[-1])
            del(objets[-1])

color = "blue"
racine = tk.Tk()
racine.title("Mon dessin")

# création des widgets\n",
bouton_cercle = tk.Button(racine, text="Cercle", bg="grey100", fg="blue", padx=20, font=("Times", "20"), command=cercle)
bouton_carre = tk.Button(racine, text="Carré", bg="grey100", fg="blue", padx=20, font=("Times", "20"), command=carre)
bouton_croix = tk.Button(racine, text="Croix", bg="grey100", fg="blue", padx=20, font=("Times", "20"), command=croix)
bouton_couleur = tk.Button(racine, text="Choix couleur", bg="grey100", fg="blue", padx=20, font=("Times", "20"), command=choisir_couleur)
bouton_undo = tk.Button(racine, text="Undo", bg="grey100", fg="blue", padx=20, font=("Times", "20"), command=undo)
canvas = tk.Canvas(racine, width=500, height=500, bg="black", bd=10, relief="raised")

# placement des widgets\n",
bouton_cercle.grid(column=0, row=1)
bouton_carre.grid(column=0, row=2)
bouton_croix.grid(column=0, row=3)
bouton_couleur.grid(column=1, row=0)
bouton_undo.grid(row=0, column=2)
canvas.grid(column=1, row=1, rowspan=3, columnspan=3)

racine.mainloop()