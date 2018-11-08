from tkinter import *

root = Tk()               # Creëer het hoofdschermroot.

def clicked():      #Functie moet altijd zonder parameters anders werkt hij niet
    label["text"] = entry.get()

label = Label(master=root,
              text='NS Reisplanner',
              background='yellow',
              foreground='blue',
              font=('Helvetica', 30, 'bold italic'),
              width=14,
              height=3)
label.pack()
button = Button(master=root, text='Druk hier', command=clicked) #als er wordt gelklikt dan word entry ingevuld in label
button.pack(pady=10,fill=X,padx=50)

entry = Entry(master=root)
entry.pack(padx=10, pady=10)

mainloop()                # Toon het hoofdscherm