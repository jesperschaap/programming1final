from tkinter import *
import math
def ckwadraat():
    grondtal = int(entry.get())
    kwadraat = grondtal ** 2
    tekst = "Kwadraat: van {} = {}"
    label["text"] = tekst.format(grondtal, kwadraat)

def cwortel():
    grondtal = int(entry.get())
    wortel = math.sqrt(grondtal)
    tekst = "Wortel: van {} = {}"
    label["text"] = tekst.format(grondtal, wortel)

root = Tk()

label = Label(master=root, text='Hello World', height=2)
label.pack()

kwadraat = Button(master=root, text='Kwadraat', command=ckwadraat)
kwadraat.pack(pady=1, padx=1)

wortel = Button(master=root, text= 'Wortel', command=cwortel)
wortel.pack(pady=1, padx=1)

entry = Entry(master=root)
entry.pack(padx=10, pady=10)

mainloop()                # Toon het hoofdscherm