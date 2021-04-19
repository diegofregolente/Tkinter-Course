from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Batman')
root.iconbitmap('images/batman.ico')

def slide():
    root.geometry(str(horinzotal.get())+'x'+str(vertical.get()))

vertical = Scale(root, from_=165, to=400)
vertical.pack()
horinzotal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horinzotal.pack()

mybtn = Button(root, text='Look Me', command=slide).pack()

root.mainloop()
