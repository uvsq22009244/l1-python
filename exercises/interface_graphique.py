import tkinter as tk
import random

def pause () : 
    x = random.randint(0, 400)
    y = random.randint(0, 400)
    canvas.create_line((x, y), (x+100, y+100), fill= "blue")
    canvas.create_line((x, y), (x+100, y+100), fill= "red")

def affichage (event):
    print(ligne)

racine = tk.Tk()

boutton = tk.Button(racine, text = "Pause", font = ("helvetica", "26"), command = pause)
canvas = tk.Canvas(racine, width = 500, height = 500, bg = "white")

boutton.grid(row = 1, column = 0)
canvas.grid(row = 0, column = 0)
racine.bind("<Button-1>", affichage)

racine.mainloop()