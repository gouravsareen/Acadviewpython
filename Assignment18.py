#Q1:-
from tkinter import *
root=Tk()
dict={'Gourav':361,'Akshita':354,'Varinda':353,'Partap':355,'Ankush':362,'Parul':364,'Aaushi':359,'Manjeet':394,'Deepanshu':388,'Chiraag':387,'shivam':345,'abhi':357}
x=StringVar()
l3=Label(root,text="")
l3.grid(row=1,column=1)
def display(evt):
    l3.config(text=dict[l1.get(ACTIVE)])
    print(dict[l1.get(ACTIVE)])
L1=Label(root,text="Name:")
L1.grid(row=0,column=0)
L2=Label(root,text="Mobile_no:")
L2.grid(row=0,column=1)
s1=Scrollbar(root,orient=VERTICAL)
l1=Listbox(root,height=10,yscrollcommand=s1.set)
for i in dict.keys():
    l1.insert(END,i)
s1.config(command=l1.yview)
l1.grid(row=1,column=0,rowspan=3)
s1.grid(row=1,column=0,rowspan=3,sticky=W,ipady=60)
l1.bind("<<ListboxSelect>>",display)
root.mainloop()

#Q2:-
from tkinter import *
root=Tk()
dict1={'Gourav':361,'Akshita':354,'Varinda':353,'Partap':355,'Ankush':362,'Parul':364,'Aaushi':359,'Manjeet':394,'Deepanshu':388,'Chiraag':387,'shivam':345,'abhi':357}
x=StringVar()
y=StringVar()
L3=Label(root,text="")
L3.grid(row=1,column=1)
def show1(evt):
    L3.config(text=dict1[l1.get(l1.curselection())])
def show2():
    dict1[x.get()]=y.get()
    z=x.get()
    print(dict1)
    l1.insert(END,z)
    print(z)
    show3()
L1=Label(root,text="Name:").grid(row=0,column=0)
L2=Label(root,text="Roll_no:").grid(row=0,column=1)
s1=Scrollbar(root,orient=VERTICAL)
l1=Listbox(root,height=10,yscrollcommand=s1.set,exportselection=0)
def show3():
    s1.config(command=l1.yview)
    s1.grid(row=1,column=0,rowspan=3,sticky=W,ipady=60)
    l1.grid(row=1, column=0, rowspan=3)
    l1.bind("<<ListboxSelect>>",show1)
for i in dict1.keys():
        l1.insert(END,i)
        print(i)
        show3()
l4=Label(root,text="enter name=").grid(row=4,column=0)
L5=Label(root,text="enter roll_no=").grid(row=4,column=1)
e1=Entry(root,textvariable=x).grid(row=5,column=0)
e2=Entry(root,textvariable=y).grid(row=5,column=1)
b1=Button(root,text="Go",command=show2).grid(row=6)
root.mainloop()




