from tkinter import *
from tkinter.messagebox import showinfo


def toonLoginFrame():
    hoofdframe.pack_forget()
    loginframe.pack()

def toonHoofdFrame():
    loginframe.pack_forget()
    hoofdframe.pack()

def login():
    if loginfield.get() == "admin":
        toonHoofdFrame()
    else:
        popbox()


def popbox():
    bericht = 'Wrong password'
    showinfo(title='Error', message=bericht)
root = Tk()

loginframe = Frame(master=root)
loginframe.pack(fill="both", expand=True)
loginfield = Entry(master=loginframe)
loginfield.pack(padx=20, pady=20)
loginbutton = Button(master=loginframe, text='login', command=login)
loginbutton.pack(padx=20, pady=20)

hoofdframe = Frame(master=root)
hoofdframe.pack(fill="both", expand=True)
backbutton = Button(master=hoofdframe, text='<', command=toonLoginFrame)
backbutton.pack(padx=20, pady=20)

toonLoginFrame()
root.mainloop()