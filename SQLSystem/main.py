from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser

#window
wd = Tk()
wd.title('Login System')
wd.geometry('600x300')
wd.resizable(width=FALSE, height=FALSE)
wd.attributes('-alpha', 0.95)
wd.iconbitmap(default='img/logoicon.ico')

#icons

img_0 = PhotoImage(file='img/logo.png')

#functions

def registrar():

    #---

    log_btn.place(x=5000, y=5000)
    reg_btn.place(x=5000, y=5000)
    #---

    name_lbl = Label(rg_fr, text='Nome:', font=('Century Gothic', 20), bg='MIDNIGHTBLUE', fg='white')
    name_lbl.place(x=15, y=15)

    name_en = ttk.Entry(rg_fr, width=30)
    name_en.place(x=195, y=27)

    email_lbl = Label(rg_fr, text='Email:', font=('Century Gothic', 20), bg='MIDNIGHTBLUE', fg='white')
    email_lbl.place(x=15, y=55)

    email_en = ttk.Entry(rg_fr, width=30)
    email_en.place(x=195, y=67)

    def regData():
        Name = str(name_en.get())
        Email = str(email_en.get())
        User = str(usr_en.get())
        Password = str(psw_en.get())

        DataBaser.cursor.execute("""
        INSERT INTO Users (Name, Email, User, Password)
        VALUES (?, ?, ?, ?)
        """, (Name, Email, User, Password))
        DataBaser.conn.commit()
        messagebox.showinfo(title='Register Info', message='Registro realizado com sucesso')

    rg_btn = ttk.Button(rg_fr, text='Cadastrar', width=30, command=regData)
    rg_btn.place(x=75, y=225)   

    def voltar():
        #----
        log_btn.place(x=75, y=225)
        reg_btn.place(x=120, y=260)
        #----

        back_btn.place(x=5000, y=5000)
        rg_btn.place(x=5000, y=5000)

        #button

        name_lbl.place(x=5000, y=5000)
        name_en.place(x=5000, y=5000)

        email_lbl.place(x=5000, y=5000)
        email_en.place(x=5000, y=5000)
        
        rg_btn.place(x=5000, y=225)  

        back_btn.place(x=5000, y=260)        

    back_btn = ttk.Button(rg_fr, text='Voltar', width=15, command=voltar)
    back_btn.place(x=120, y=260)

    







#frames

lf_fr = Frame(wd, width=200, height=300, bg='MIDNIGHTBLUE', relief='raise')
lf_fr.pack(side=LEFT)

rg_fr = Frame(wd, width=395, height=300, bg='MIDNIGHTBLUE', relief='raise')
rg_fr.pack(side=RIGHT)

#labels

l_1 = Label(lf_fr, image=img_0, bg='MIDNIGHTBLUE')
l_1.place(x=50, y=100)

usr_lbl = Label(rg_fr, text='Username:', font=('Century Gothic', 20), bg='MIDNIGHTBLUE', fg='white')
usr_lbl.place(x=15, y=95)

usr_psw = Label(rg_fr, text='Password:', font=('Century Gothic', 20), bg='MIDNIGHTBLUE', fg='white')
usr_psw.place(x=15, y=132)


#entrys

usr_en = ttk.Entry(rg_fr, width=30)
usr_en.place(x=195, y=107)

psw_en = ttk.Entry(rg_fr, width=30, show='•')
psw_en.place(x=195, y=145)


#buttons

log_btn = ttk.Button(rg_fr, text='Login', width=30)
log_btn.place(x=75, y=225)

reg_btn = ttk.Button(rg_fr, text='Registrar', width=15, command=registrar)
reg_btn.place(x=120, y=260)




wd.mainloop()