import tkinter as tk
import random

def cercle():
    x = random.randint(0, 400)
    y = random.randint(0, 400)
    canvas.create_oval((x, y), (x+100, y+100), fill= "blue")

def carre():
    x = random.randint(0, 400)
    y = random.randint(0, 400)
    canvas.create_rectangle((x, y), (x+100, y+100), fill= "red")

def croix():
    x = random.randint(0, 400)
    y = random.randint(0, 400)
    canvas.create_line((x, y), (x+100, y+100), fill= "yellow")
    canvas.create_line((x, y), (x+100, y+100), fill= "yellow")

def choisir_couleur():
    global color
    color = input("Choisis une couleur: ")

color = "blue"

dessin = tk.Tk()

dessin.title("Mon dessin")

boutton_cercle = tk.Button(dessin, text="Cercle", padx = "0.5cm", pady = "0.5cm", font = ("", "10"), command = cercle) 
boutton_carre = tk.Button(dessin, text="Carre", padx = "0.5cm", pady = "0.5cm", command = carre)
boutton_croix = tk.Button(dessin, text="Croix", padx = "0.5cm", pady = "0.5cm", command = croix)
boutton_couleur = tk.Button(dessin, text="Choisir une couleur", padx = "0.5cm", pady = "0.5cm", command = choisir_couleur)
canvas = tk.Canvas(dessin, width= 500, height = 500, bg = "black", bd = 50, relief = "raised")

boutton_cercle.grid(row=1, column=0)
boutton_carre.grid(row=2, column=0)
boutton_croix.grid(row=3, column=0)
boutton_couleur.grid(row=0, column=1)
canvas.grid(row= 1, column = 1, rowspan = 3)

dessin.mainloop()
