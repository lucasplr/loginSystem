from ctypes import POINTER
from tkinter import *
from PIL import Image, ImageTk



wd = Tk()
wd.geometry('500x400')
wd.title('Local Login System')
wd.resizable(width=FALSE, height=FALSE)

#colors
cor1 = '#ffffff' #white
cor2 = '#000000' #black
cor3 = '#E1E8E8' #gray
cor4 = '#2fb1b5' #blue
cor5 = '#22b071'

#frames

f_0 = Frame(wd, width=500, height=170, bg=cor3)
f_0.grid(row=0, column=0)


f_1 = Frame(wd, width=500, height=130, bg=cor3)
f_1.grid(row=1, column=0)

f_2 = Frame(wd, width=500, height=130, bg=cor3)
f_2.grid(row=1, column=1)

f_3 = Frame(wd, width=500, height=100, bg=cor3)
f_3.grid(row=2, column=0)

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


icon = Label(f_0, image=img_0, relief=FLAT)
icon.place(x=220, y=25)

icon2 = Label(f_1, image=img_1, relief=FLAT)
icon2.place(x=155, y=5)

icon3 = Label(f_1, image=img_2, relief=FLAT)
icon3.place(x=155, y=75)

#labels

l_1 = Label(f_0, text='Login de Usuário', relief=FLAT, bg=cor3, fg=cor5, font=('Ivy 20 bold'))
l_1.place(x=140, y=105)

l_2 = Label(f_3, text='Não possui conta?', bg=cor3, fg=cor2, font=('Ivy 10'))
l_2.place(x=185, y=60)

l_3 = Label(f_2, text='Bem vindo', bg=cor3, fg=cor2, font=('Ivy 25'))
l_3.place(x=185, y=25)

#functions

checar = 0

def test():
    if checar == 1:
        f_1.grid(row=1, column=1)
        f_2.grid(row=1, column=0)
    if checar == 0:
        f_2.grid(row=1, column=1)
        f_1.grid(row=1, column=0)
    
    l_3.after(1000, test)




def check():
    global checar
    if btn['text'] == 'Login':
        login()
    elif btn['text'] == 'Registrar':
        registrar()
        changetolog()
    elif btn['text'] == 'Deslogar':
        deslogar()


def login():
    global checar

    a = open('log.txt')
    

    log = e_1.get()
    password = e_2.get()

    registrados = a.readlines()

    if btn['text'] != 'Login':
        changetolog()
    else:
        if log  + '\n' in registrados:
            changetodeslog()
            checar = 1
            test()
        else:
            print('Usuário não cadastrado')
    a.close()

def registrar():

    a = open('log.txt', 'a')

    log = str(e_1.get())
    password = e_2.get()

    a.write(f'{log}\n')

    a.close()

def deslogar():
    global checar
    if btn['text'] == 'Deslogar':
        checar = 0
        test()
        changetolog()

    

def changetoreg():
    if btn['text'] == 'Login':    
        btn['text'] = 'Registrar'
    

def changetolog():
    if btn['text'] == 'Registrar':
        btn['text'] = 'Login';
    elif btn['text'] == 'Deslogar':
        btn['text'] = 'Login';

def changetodeslog():
    if btn['text'] == 'Login':
        btn['text'] = 'Deslogar'

#entrys

e_1 = Entry(f_1, relief=GROOVE, bg=cor1, fg=cor2, width=25)
e_1.place(x=200, y=8)

e_2 = Entry(f_1, relief=GROOVE, bg=cor1, fg=cor2, width=25, show='*')
e_2.place(x=200, y=78)


#buttons

btn = Button(f_3, text='Login', relief=FLAT, command=check, overrelief=RAISED, bg=cor4, fg=cor1, font=('Ivy 10'), width=10, height=2, cursor="hand2")
btn.place(x=220, y=0)   

btn2 = Button(f_3, text='Registro', command=changetoreg, bg=cor3, fg=cor4, relief=FLAT, font=('Ivy 10'), cursor="hand2")
btn2.place(x=300, y=55)

wd.mainloop()