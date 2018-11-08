from tkinter import *
from infoFunctions import *
master = Tk()

scrollbar = Scrollbar(master)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(master, yscrollcommand=scrollbar.set)
for x in data("Utrecht"):
    listbox.insert(END, x)
listbox.pack(side=LEFT, fill=BOTH)
listbox.config(width = 0)

scrollbar.config(command=listbox.yview)

mainloop()