from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Batmam')
root.iconbitmap('images/batman.ico')
root.geometry('400x400')

# Drop Down Boxes
def show():
    label = Label(root, text=clicked.get()).pack()

optionsMenu =  ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]

clicked = StringVar()
clicked.set(optionsMenu[0])

drop = OptionMenu(root, clicked, *optionsMenu)
drop.pack()

myButton = Button(root, text='Show Selection', command=show).pack()













root.mainloop()
