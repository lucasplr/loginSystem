from tkinter import *
from tkinter import messagebox


#window
wd = Tk()
wd.title('Login System')
wd.geometry('600x300')
wd.resizable(width=FALSE, height=FALSE)

#icons

img_0 = PhotoImage(file='img/logo.png')


#frames

lf_fr = Frame(wd, width=200, height=300, bg='MIDNIGHTBLUE', relief='raise')
lf_fr.pack(side=LEFT)

rg_fr = Frame(wd, width=395, height=300, bg='MIDNIGHTBLUE', relief='raise')
rg_fr.pack(side=RIGHT)

#labels

l_1 = Label(lf_fr, image=img_0, bg='MIDNIGHTBLUE')
l_1.place(x=50, y=100)









wd.mainloop()