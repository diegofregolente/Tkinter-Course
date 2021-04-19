from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Batman')
root.iconbitmap('images/batman.ico')
root.geometry('400x400')

def show():
    myLabel = Label(root, text=var.get())
    myLabel.pack()

var = StringVar()

check = Checkbutton(root, text='Check this box', variable=var, onvalue='On', offvalue='Off')
check.deselect()
check.pack()

myButton = Button(root, text="Show Selection", command=show)
myButton.pack()

root.mainloop()
