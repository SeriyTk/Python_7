from tkinter import *
import random, time

def bros():
    x = random.choice(['Картинки для игры/b1.png',  'Картинки для игры/b2.png', 'Картинки для игры/b3.png',
                                   'Картинки для игры/b4.png', 'Картинки для игры/b5.png', 'Картинки для игры/b6.png'])
    return x

def img(event):
    global b1,b2
    for i in range(10):
        b1 = PhotoImage(file=(bros()))
        b2 = PhotoImage(file=(bros()))
        lab1['image'] = b1
        lab2['image'] = b2
        root.update()
        time.sleep(1)

root = Tk()
root.geometry('400x200')
root.title('Игра в кости. Бросай!')
root.resizable(height=False, width=False)
root.iconphoto(True, PhotoImage(file=('Картинки для игры/iconka.png')))
font = PhotoImage(file=('Картинки для игры/holst.png'))
Label(root, image=font).pack()
lab1 = Label(root)
lab1.place(relx=0.3,rely=0.5, anchor=CENTER)
lab2 = Label(root)
lab2.place(relx=0.7,rely=0.5, anchor=CENTER)
root.bind('<1>', img)
img('event')
root.mainloop()
