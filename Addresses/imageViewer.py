from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Batman Image Viewer')
root.iconbitmap('images/batman.ico')

my_img1 = ImageTk.PhotoImage(Image.open('images/bat1.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('images/bat2.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('images/bat3.jpg'))


image_list = [my_img1, my_img2, my_img3]

status = Label(root, text='Image 1 of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)


my_label = Label(image=image_list[0])
my_label.grid(row=0, column=0, columnspan=3)


def next(image_number):
    global my_label
    global next_button
    global back_button

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number])
    next_button = Button(root, text='>>', command=lambda: next(image_number+1))
    back_button = Button(root, text='<<', command=lambda: back(image_number-1))
    if image_number == len(image_list)-1:
        next_button = Button(root, text='>>', state=DISABLED)


    my_label.grid(row=0, column=0, columnspan=3)
    back_button.grid(row=1, column=0)
    next_button.grid(row=1, column=2)

    status = Label(root, text='Image ' + str(image_number+1) + ' of ' + str(len(image_list)), bd=1, relief=SUNKEN,
                   anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


def back(image_number):
    global my_label
    global next_button
    global back_button

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number])
    next_button = Button(root, text='>>', command=lambda: next(image_number+1))
    back_button = Button(root, text='<<', command=lambda: back(image_number-1))
    if image_number == 0:
        back_button = Button(root, text='<<', command=back, state=DISABLED)


    my_label.grid(row=0, column=0, columnspan=3)
    back_button.grid(row=1, column=0)
    next_button.grid(row=1, column=2)

    status = Label(root, text='Image ' + str(image_number+1) + ' of ' + str(len(image_list)), bd=1, relief=SUNKEN,
                   anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)




back_button = Button(root, text='<<', command=back, state=DISABLED)
next_button = Button(root, text='>>', command=lambda: next(1))
exit_button = Button(root, text='Sair', command=root.quit)

back_button.grid(row=1, column=0)
exit_button.grid(row=1, column=1)
next_button.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()