from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#window
wd = Tk()
wd.title('Login System')
wd.geometry('600x300')
wd.resizable(width=FALSE, height=FALSE)
wd.attributes('-alpha', 0.95)

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

usr_lbl = Label(rg_fr, text='Username:', font=('Century Gothic', 20), bg='MIDNIGHTBLUE', fg='white')
usr_lbl.place(x=15, y=75)

usr_psw = Label(rg_fr, text='Password:', font=('Century Gothic', 20), bg='MIDNIGHTBLUE', fg='white')
usr_psw.place(x=15, y=150)


#entrys

usr_en = ttk.Entry(rg_fr, width=30)
usr_en.place(x=195, y=87)

psw_en = ttk.Entry(rg_fr, width=30)
psw_en.place(x=195, y=162)


#buttons

log_btn = ttk.Button(rg_fr, text='Login', width=30)
log_btn.place(x=75, y=225)

reg_btn = ttk.Button(rg_fr, text='Registrar', width=15)
reg_btn.place(x=120, y=260)




wd.mainloop()