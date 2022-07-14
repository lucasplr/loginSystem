from tkinter import *
from PIL import Image, ImageTk
from traitlets import observe


wd = Tk()
wd.geometry('500x700')
wd.title('Local Login System')
wd.resizable(width=FALSE, height=FALSE)

#colors
cor1 = '#ffffff' #white
cor2 = '#000000' #black
cor3 = '#E1E8E8' #gray
cor4 = '#2fb1b5' #blue
cor5 = '#22b071'

#frames
f_1 = Frame(wd, width=500, height=450, bg=cor3)
f_1.grid(row=0, column=0)

f_2 = Frame(wd, width=500, height=250, bg=cor3)
f_2.grid(row=1, column=0)

#icon

img_0 = Image.open('img/icon.png')
img_0 = img_0.resize((65, 65), Image.Resampling.LANCZOS)
img_0 = ImageTk.PhotoImage(img_0)

img_1 = Image.open('img/email.png')
img_1 = img_1.resize((20, 20), Image.Resampling.LANCZOS)
img_1 = ImageTk.PhotoImage(img_1)

img_2 = Image.open('img/password.png')
img_2 = img_2.resize((20, 20), Image.Resampling.LANCZOS)
img_2 = ImageTk.PhotoImage(img_2)


icon = Label(f_1, image=img_0, relief=FLAT)
icon.place(x=220, y=45)

icon2 = Label(f_1, image=img_1, relief=FLAT)
icon2.place(x=155, y=215)

icon3 = Label(f_1, image=img_2, relief=FLAT)
icon3.place(x=155, y=277)

#labels

l_1 = Label(f_1, text='Login de Usuário', relief=FLAT, bg=cor3, fg=cor5, font=('Ivy 20 bold'))
l_1.place(x=140, y=140)

#entrys

e_1 = Entry(f_1, relief=GROOVE, bg=cor1, fg=cor2, width=25)
e_1.place(x=200, y=218)

e_2 = Entry(f_1, relief=GROOVE, bg=cor1, fg=cor2, width=25)
e_2.place(x=200, y=280)

wd.mainloop()