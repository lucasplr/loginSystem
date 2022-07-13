from tkinter import *
from PIL import Image, ImageTk


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

icon = Label(f_1, image=img_0, relief=FLAT)
icon.place(x=220, y=45)


#labels

l_1 = Label(f_1, text='Login de Usuário', relief=FLAT, bg=cor3, fg=cor5, font=('Ivy 20 bold'))
l_1.place(x=140, y=140)

#entrys

e_1 = Entry(f_1, relief=GROOVE, bg=cor1, fg=cor2, width=25)
e_1.place(x=215, y=200)


wd.mainloop()