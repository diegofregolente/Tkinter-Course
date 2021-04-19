from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Batman Program')
root.iconbitmap('images/batman.ico')

frame = LabelFrame(root, padx=50, pady=50) # inside of frame
frame.pack(padx=10, pady=10) # out of frame

b = Button(frame, text="Don't click here!")
b.grid(row=0, column=0)
b2 = Button(frame, text='... or here!')
b2.grid(row=1, column=1)

root.mainloop()