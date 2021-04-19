from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

root = Tk()
root.title('Batman')
root.iconbitmap('images/batman.ico')


def open_img():
    global img
    root.filename = filedialog.askopenfilename(initialdir='/users/ti.infra/desktop/python/tkinter course/images',
                                               title='Select a File',
                                               filetypes=(("ALL FILES", "*.*"), ('JPG', '*.jpg'), ('PNG', '*.png')))
    img = ImageTk.PhotoImage(Image.open(root.filename))
    mylabelimg = Label(image=img)
    mylabelimg.pack()

btn = Button(root, text='Open Image', command=open_img).pack()


root.mainloop()
