#Q1:-
from tkinter import *
root=Tk()
w=Label(root,text="Hello World")
w.pack()
button=Button(root,text="exit",width=25,fg="red",command=quit)
button.pack()
root.mainloop()

#Q2:-
from tkinter import *
root=Tk()
def Text():
    print("Tkinter is very easy")
button=Button(root,text="Display",width=25,fg="red",command=Text)
button.pack()
root.mainloop()

#Q3:-
from tkinter import *
root = Tk()
lb=Label(root, text='Edit')
lb.grid(row=0,column=0)
e1 = Entry(root,width=10)
e1.grid(row=0, column=1)
frame=Frame(root).grid(row=0)
bframe=Frame(root).grid(row=1)
def Edit():
    res="Welcome to " + e1.get()
    lb.configure(text=res)
button1=Button(frame,text="EditText",fg="pink",command=Edit)
button1.grid(row=0,column=2)
button2=Button(bframe,text="Exit",fg="red",command=quit)
button2.grid(row=1,column=2)
root.mainloop()

#Q4:-
from tkinter import *
window = Tk()
window.title("Tkinter")
lbl = Label(window, text="Hiii")
lbl.grid(column=0, row=0)
txt = Entry(window, width=10)
txt.grid(column=1, row=0)
def clicked():
    res = "you are " + txt.get()
    lbl.configure(text=res)
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=2, row=0)
window.mainloop()
