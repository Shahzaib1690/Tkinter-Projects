from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
def newfile():
    global file
    file = None
    root.title('Untitled - Notepad')
    textarea.delete(1.0,END)

def openfile():
    global file
    file = None
    file  = askopenfilename(defaultextension='.txt',filetypes=[('All Files','*.*'),('Text Documents','*.txt')])

    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + '-notepad')
        textarea.delete(1.0, END)
        f = open(file, 'r')
        textarea.insert(1.0,f.read())

def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt',defaultextension='.txt',filetypes=[('All Files','*.*'),('Text Documents','*.txt')])

        if file == '':
            file = None
        else:
            f =open(file,'w')
            f.write(textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file + '-Notepad'))
            print('Saved')
    else:
        f = open(file,'w')
        f.write(textarea.get(1.0, END))
        f.close()

def cut():
    textarea.event_generate('<<Cut>>')

def copy():
    textarea.event_generate('<<Copy>>')

def paste():
    textarea.event_generate('<<Paste>>')

def delete():
    textarea.delete(1.0,END)

def about():
    showinfo('Notepad','A notepad using tkinter')
root = Tk()
root.title('Untitled - Notepad')
root.geometry('700x700')

file = None

SB  = Scrollbar(root)
SB.pack(fill=Y,side=RIGHT)
textarea = Text(root,font='lucida 13',yscrollcommand=SB.set)
textarea.pack(expand=True,fill=BOTH)
SB.config(command= textarea.yview)


mainmenu = Menu(root)

# File Menu
filemenu = Menu(mainmenu,tearoff=0)
filemenu.add_command(label='New',command=newfile)
filemenu.add_command(label='Open',command=openfile)
filemenu.add_command(label='Save',command=savefile)
filemenu.add_command(label='Exit',command=quit)
mainmenu.add_cascade(label='File',menu=filemenu)

# Edit Menu

editmenu = Menu(mainmenu,tearoff=0)
editmenu.add_command(label='Cut',command=cut)
editmenu.add_command(label='Copy',command=copy)
editmenu.add_command(label='Paste',command=paste)
editmenu.add_command(label='Delete',command=delete)
mainmenu.add_cascade(label='Edit',menu=editmenu)

# Help

helpmenu = Menu(mainmenu,tearoff=0)
helpmenu.add_cascade(label='About',command=about)
mainmenu.add_cascade(label='Help',menu= helpmenu)

root.config(menu=mainmenu)
root.mainloop()