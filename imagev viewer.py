from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Images,Icons and Exit Buttons')
root.iconbitmap('c:/Users/ACER/Downloads/crown_icon.ico')

my_img0 = ImageTk.PhotoImage(Image.open('c:/Users/ACER/Documents/mg.folder/mg.jpg'))
my_img1 = ImageTk.PhotoImage(Image.open('c:/Users/ACER/Pictures/atmg/mg1a.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('c:/Users/ACER/Pictures/atmg/mg1b.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('c:/Users/ACER/Pictures/atmg/mg2.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('c:/Users/ACER/Pictures/atmg/mg4.jpg'))
my_img5 = ImageTk.PhotoImage(Image.open('c:/Users/ACER/Pictures/mg3.jpg'))
my_img6 = ImageTk.PhotoImage(Image.open('c:/Users/ACER/Pictures/ccrown.jpg'))
my_img7 = ImageTk.PhotoImage(Image.open('c:/Users/ACER/Documents/mg.folder/mggg.jpg'))

image_list = [my_img0,my_img1,my_img2,my_img3,my_img4,my_img5,my_img6,my_img7]

my_label = Label(image=my_img0)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image = image_list[image_number-1])
    button_forward = Button(root, text= '>>', command= lambda: forward(image_number+1))
    button_back = Button(root, text= '<<', command=lambda: back(image_number-1))

    if image_number ==8:
        button_forward = Button(root,text='>>', state= DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1,column=0)

def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image = image_list[image_number-1])
    button_forward = Button(root, text= '>>', command= lambda: forward(image_number+1))
    button_back = Button(root, text= '<<', command=lambda: back(image_number-1))

    if image_number ==1:
        button_back = Button(root,text ='<<', state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1,column=0)

button_back = Button(root, text= '<<', command= back)
button_exit = Button(root, text= 'Exit Program', command= root.quit)
button_forward = Button(root, text= '>>', command= lambda: forward(2))

button_back.grid(row=1,column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)


root.mainloop()