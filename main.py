from sys import exit
from os import system
from tkinter import *
from tkinter.messagebox import showinfo
import ctypes

flag=1
flag1=0
flag2=0

def eteindre (event=None):
    system('shutdown.exe -s -t 0')
    print("le pc va s'éteindre")

def redemarer (event=None) :
    system('shutdown.exe -r -t 0')
    print("votre appareil va redémaré ")

def veille (event=None) :
    ctypes.windll.powrprof.SetSuspendState(0, 1, 0)
    showinfo("infos", "Le PC est mis en veille", parent=root)


def d (event=None):
    global flag
    flag+=1
    if flag == 5 :flag= 4
    mod()

def g (event=None):
    global flag
    flag-=1
    if flag == 0 :flag= 1
    mod()

def a (event=None):
    global flag1
    if not flag1 : flag1=1 ; mod(); root.after(10000,_a)

def _a (event=None):
    global flag1
    flag1=0
    mod()

def m (event=None):
    global foto,flag2,item2
    if event.y in range(82,115):
        if event.x in range (55,84):
            if flag2  != 1 :
                if flag2 !=0: can.delete(foto)
                foto=PhotoImage(file='./assets/v.gif')
                item2=can.create_image(69,97,image=foto)
                flag2=1 
        elif event.x in range (175,208):
            if flag2  != 2 :
                if flag2 !=0: can.delete(foto)
                foto=PhotoImage(file='./assets/e.gif')
                item2=can.create_image(189,97,image=foto)
                flag2=2
        elif event.x in range (294,326):
            if flag2  != 3 :
                if flag2 !=0: can.delete(foto)
                foto=PhotoImage(file='./assets/r.gif')
                item2=can.create_image(308,98,image=foto)
                flag2=3
        else :
            if flag2 !=0:
                can.delete(item2)
                flag2=0
    elif event.x in range(310,368):
        if event.y in range(169,188):
            if flag2  != 4 :
                if flag2 !=0: can.delete(foto)
                foto=PhotoImage(file='./assets/c.gif')
                item2=can.create_image(337,178,image=foto)
                flag2=4
        else :
            if flag2 !=0:
                can.delete(item2)
                flag2=0
    else :
        if flag2 !=0:
            can.delete(item2)
            flag2=0


def mod (event=None) :
    global photo,item
    can.delete(item)
    if flag1 :
        if flag == 1 : photo=PhotoImage(file='./assets/dash_v_.gif')
        elif flag == 2 : photo=PhotoImage(file='./assets/dash_e_.gif')
        elif flag == 3 : photo=PhotoImage(file='./assets/dash_r_.gif')
        elif flag == 4 : photo=PhotoImage(file='./assets/dash_c_.gif')
        else : print(0)
    else :
        if flag == 1 : photo=PhotoImage(file='./assets/dash_v.gif')
        elif flag == 2 : photo=PhotoImage(file='./assets/dash_e.gif')
        elif flag == 3 : photo=PhotoImage(file='./assets/dash_r.gif')
        elif flag == 4 : photo=PhotoImage(file='./assets/dash_c.gif')
        else : print(1)
    item=can.create_image(191,100,image=photo)

def jj (event=None) :
    global flag2
    if flag2 !=0:
        can.delete(item2)
        flag2=0
        if event.y in range(82,115):
            if event.x in range (55,84):
                veille()
            elif event.x in range (175,208):
                eteindre()
            elif event.x in range (294,326):
                redemarer()
        elif event.x in range(310,368):
            if event.y in range(169,188):
                exit()




root=Tk()
root.title("Mona Technology Menu d'extinction windows xp")
# Créer un cadre pour contenir l'image# Définir l'icône de la fenêtre
root.iconbitmap('./assets/favicon.ico')
root.bind('<Right>',d)
root.bind('<Left>',g)
root.bind('<m>',veille)
root.bind('<t>',eteindre)
root.bind('<r>',redemarer)
root.bind('<Alt-a>',a)
can=Canvas(height=200,width=382,bg='grey')
photo=PhotoImage(file='./assets/dash_v.gif')
item=can.create_image(191,100,image=photo)
can.grid(row=1,column=0,columnspan=5)
can.bind('<Button1-Motion>',m)
can.bind('<Button-1>',m)
can.bind('<Button1-ButtonRelease>',jj)
root.mainloop()

