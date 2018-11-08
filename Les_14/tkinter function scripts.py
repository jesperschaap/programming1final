from tkinter import *
from TreinFuncties import *

def berekenTarief():
    afstand = float(afstandEntry.get())
    prijs = int(standaardprijs(afstand))
    label["text"] = "De ritprijs is: {}".format(prijs)


root = Tk()

afstandEntry = Entry(master=root)
afstandEntry.pack()

button = Button(master=root, text="Druk hier", command=berekenTarief)
button.pack()

label = Label(master=root)
label.pack()

root.mainloop()