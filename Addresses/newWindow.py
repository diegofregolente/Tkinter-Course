from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Batman')
root.iconbitmap('images/batman.ico')

def open_new():
    global my_img
    top = Toplevel()
    top.title('Batman')
    top.iconbitmap('images/batman.ico')
    my_img = ImageTk.PhotoImage(Image.open('images/bat1.jpg'))
    my_label = Label(top, image=my_img)
    my_label.pack()
    btn2 = Button(top, text='Close Window', command=top.destroy)
    btn2.pack()


frame = LabelFrame(root, padx=50, pady=50)
frame.pack(padx=10, pady=10) # out of frame

btn = Button(frame, text='Open Second Window', command=open_new).pack()





root.mainloop()