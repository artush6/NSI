import tkinter as tk


def gerer_click(ev):
    valeur = int(b["text"])
    valeur += 1
    b.config(text=str(valeur))


fenetre = tk.Tk()
b = tk.Button(fenetre, text='0')
b.pack()

b.bind("<Button-1>", gerer_click)

fenetre.title("Cliquer sur le bouton")
fenetre.geometry("800x400")
fenetre.mainloop()
