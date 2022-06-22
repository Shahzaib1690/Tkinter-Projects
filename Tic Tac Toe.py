from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('245x335')
root.resizable(False,False)
root.title('Tic Tac Toe')
root.configure(background='light grey')

click = True
left = 0

value = StringVar()
value.set('X Turn')
screen = Entry(root,textvariable=value,background='light grey',font='Italic 16 bold')

screen.grid(row=4,column=0,columnspan=8)

btn1 = StringVar()
btn2 = StringVar()
btn3 = StringVar()
btn4 = StringVar()
btn5 = StringVar()
btn6 = StringVar()
btn7 = StringVar()
btn8 = StringVar()
btn9 = StringVar()

def play():
    button1 = Button(root,textvariable=btn1,command =lambda :press(1,0,0),height=6,width=10,relief=SUNKEN,bg='cyan')
    button2 = Button(root,textvariable=btn2,command =lambda :press(2,0,1),height=6,width=10,relief=SUNKEN, bg='cyan')
    button3 = Button(root,textvariable=btn3,command =lambda :press(3,0,2),height=6,width=10,relief=SUNKEN, bg='cyan')
    button4 = Button(root,textvariable=btn4,command =lambda :press(4,1,0),height=6,width=10,relief=SUNKEN, bg='cyan')
    button5 = Button(root,textvariable=btn5,command =lambda :press(5,1,1),height=6,width=10,relief=SUNKEN, bg='cyan')
    button6 = Button(root,textvariable=btn6,command =lambda :press(6,1,2),height=6,width=10,relief=SUNKEN, bg='cyan')
    button7 = Button(root,textvariable=btn7,command =lambda :press(7,2,0),height=6,width=10,relief=SUNKEN, bg='cyan')
    button8 = Button(root,textvariable=btn8,command =lambda :press(8,2,1),height=6,width=10,relief=SUNKEN, bg='cyan')
    button9 = Button(root,textvariable=btn9,command =lambda :press(9,2,2),height=6,width=10,relief=SUNKEN, bg='cyan')
    button1.grid(row=0,column=0)
    button2.grid(row=0, column=1)
    button3.grid(row=0, column=2)
    button4.grid(row=1, column=0)
    button5.grid(row=1, column=1)
    button6.grid(row=1, column=2)
    button7.grid(row=2, column=0)
    button8.grid(row=2, column=1)
    button9.grid(row=2, column=2)

def press(num,r,c):
    global click,left,screen
    val = screen.get()

    if val == 'X Turn':

        value.set('O Turn')
        screen.update()

    elif val == 'O Turn':
        value.set('X Turn')
        screen.update()

    if click == True:
        label1 = Label(root,text='X',font='Arial 20 bold',bg='cyan')
        label1.grid(row=r,column=c)
        if num == 1:
            btn1.set('X')
        if num == 2:
            btn2.set('X')
        if num == 3:
            btn3.set('X')
        if num == 4:
            btn4.set('X')
        if num == 5:
            btn5.set('X')
        if num == 6:
            btn6.set('X')
        if num == 7:
            btn7.set('X')
        if num == 8:
            btn8.set('X')
        if num == 9:
            btn9.set('X')
        left +=1

        click = False
    else:
        label2 = Label(root,text='O',font='Arial 20 bold',bg='cyan')
        label2.grid(row=r,column=c)
        if num == 1:
            btn1.set('O')
        if num == 2:
            btn2.set('O')
        if num == 3:
            btn3.set('O')
        if num == 4:
            btn4.set('O')
        if num == 5:
            btn5.set('O')
        if num == 6:
            btn6.set('O')
        if num == 7:
            btn7.set('O')
        if num == 8:
            btn8.set('O')
        if num == 9:
            btn9.set('O')
        left +=1
        click = True

    win()
def win():
    global click,left

    if (btn1.get()=='X' and btn2.get()=='X' and btn3.get() == 'X' or
        btn4.get()=='X' and btn5.get()=='X' and btn6.get() == 'X' or
        btn7.get()=='X' and btn8.get()=='X' and btn9.get() == 'X' or
        btn1.get()=='X' and btn4.get()=='X' and btn7.get() == 'X' or
        btn2.get()=='X' and btn5.get()=='X' and btn8.get() == 'X' or
        btn3.get()=='X' and btn6.get()=='X' and btn9.get() == 'X' or
        btn1.get()=='X' and btn5.get()=='X' and btn9.get() == 'X' or
        btn3.get()=='X' and btn5.get()=='X' and btn7.get() == 'X'):

        messagebox.showinfo('winner','X wins')
        click = True
        left = 0
        clear()
        play()


    elif (btn1.get() == 'O' and btn2.get() == 'O' and btn3.get() == 'O' or
            btn4.get() == 'O' and btn5.get() == 'O' and btn6.get() == 'O' or
            btn7.get() == 'O' and btn8.get() == 'O' and btn9.get() == 'O' or
            btn1.get() == 'O' and btn4.get() == 'O' and btn7.get() == 'O' or
            btn2.get() == 'O' and btn5.get() == 'O' and btn8.get() == 'O' or
            btn3.get() == 'O' and btn6.get() == 'O' and btn9.get() == 'O' or
            btn1.get() == 'O' and btn5.get() == 'O' and btn9.get() == 'O' or
            btn3.get() == 'O' and btn5.get() == 'O' and btn7.get() == 'O'):

        messagebox.showinfo('winner','O wins')
        left = 0
        clear()
        play()
    elif left == 9:
        messagebox.showinfo('Draw','Match Draw')
        left = 0
        click = True
        clear()
        play()

def clear():
    btn1.set('')
    btn2.set('')
    btn3.set('')
    btn4.set('')
    btn5.set('')
    btn6.set('')
    btn7.set('')
    btn8.set('')
    btn9.set('')

Button(root,text='Clear',command=clear,font='Arial 9 bold',width=10,height=1,relief=SUNKEN).grid(row=4,column=2)
play()
root.mainloop()