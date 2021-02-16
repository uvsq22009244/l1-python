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