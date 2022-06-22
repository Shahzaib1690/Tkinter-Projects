from tkinter import *

def click(event):
    global screen
    val = event.widget.cget('text')
    if val == "C":
        value.set("")
        screen.update()

    elif val == '=':
        if value.get().isdigit() :
            x = int(value.get())

        else:
            try:
                x = eval(screen.get())

            except Exception as e:
                print(e)
                x = 'Syntax Error'

        value.set(x)
        screen.update()

    else:
        value.set(value.get() + val)
        screen.update()

root = Tk()
root.title('Calculator')
root.geometry('240x325')

value = StringVar()
value.set('')
screen = Entry(root,textvariable=value,font='arial 15 bold')
screen.pack(fill=X,pady=5,padx=5,ipadx=5,ipady=5)

root.configure(background='light grey')

f = Frame(root)

b = Button(f,text='1',padx=5,pady=5,font='luciada 15 bold',bg = 'grey')
b.bind('<1>', click)
b.pack(side=LEFT,padx=10,pady=10)

b = Button(f,text='2',padx=5,pady=5,font='luciada 15 bold',bg = 'grey')
b.bind('<1>', click)
b.pack(side=LEFT,padx=10,pady=10)

b = Button(f,text='3',padx=5,pady=5,font='luciada 15 bold',bg = 'grey')
b.bind('<1>', click)
b.pack(side=LEFT,padx=10,pady=10)

b = Button(f,text='X',padx=5,pady=5,font='luciada 15 bold')
b.bind('<1>', click)
b.pack(side=LEFT,padx=10,pady=10)

f.pack()

f = Frame(root)

b = Button(f,text='4',padx=5,pady=5,font='luciada 15 bold',bg = 'grey')
b.bind('<1>', click)
b.pack(side=LEFT,padx=10,pady=10)

b = Button(f,text='5',padx=5,pady=5,font='luciada 15 bold',bg = 'grey')
b.bind('<1>', click)
b.pack(side=LEFT,padx=10,pady=10)

b = Button(f,text='6',padx=5,pady=5,font='luciada 15 bold',bg = 'grey')
b.bind('<1>', click)
b.pack(side=LEFT,padx=10,pady=10)

b = Button(f,text='/',padx=8,pady=5,font='luciada 15 bold')
b.bind('<1>', click)
b.pack(side=LEFT,padx=10,pady=10)

f.pack()

f = Frame(root)

b = Button(f,text='7',padx=5,pady=5,font='luciada 15 bold',bg = 'grey')
b.bind('<1>', click)
b.pack(side=LEFT,padx=10,pady=10)

b = Button(f,text='8',padx=5,pady=5,font='luciada 15 bold',bg = 'grey')
b.bind('<1>', click)
b.pack(side=LEFT,padx=10,pady=10)

b = Button(f,text='9',padx=5,pady=5,font='luciada 15 bold',bg = 'grey')
b.bind('<1>', click)
b.pack(side=LEFT,padx=10,pady=10)

b = Button(f,text='C',padx=4,pady=5,font='luciada 15 bold')
b.bind('<1>', click)
b.pack(side=LEFT,padx=10,pady=10)

f.pack()

f = Frame(root)

b = Button(f,text='+',padx=5,pady=5,font='luciada 15 bold')
b.bind('<1>', click)
b.pack(side=LEFT,padx=10,pady=10)

b = Button(f,text='0',padx=5,pady=5,font='luciada 15 bold',bg = 'grey')
b.bind('<1>', click)
b.pack(side=LEFT,padx=10,pady=10)

b = Button(f,text='-',padx=6,pady=5,font='luciada 15 bold')
b.bind('<1>', click)
b.pack(side=LEFT,padx=10,pady=10)

b = Button(f,text='=',padx=5,pady=5,font='luciada 15 bold')
b.bind('<1>', click)
b.pack(side=LEFT,padx=10,pady=10)

f.pack()

root.mainloop()