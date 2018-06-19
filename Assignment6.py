#Q1:-
l=[]
for i in range(1,11):
    i=input("enter values:")
    l.append(i)
print(l)

#Q2:-
a=10
while(a==10):
    print("infinite loop")

#Q3:-
m=[]
n=[]
for i in range(1,5):
    i=input("enter values:")
    m.append(i)
print(m)
for i in range(1,5):
    n.append(i*i)
print(n)

#Q4:-
k1=[]
k2=[]
k3=[]
u=[1,2,3,'akshu','goru','nanu',2.3,3.4,4.5]
for i in u:
    if isinstance(i,int):
        k1.append(i)
print("integer values: ",k1)

for i in u:
    if isinstance(i,float):
        k2.append(i)
print("float values: ",k2)

for i in u:
    if isinstance(i,str):
       k3.append(i)
print("strings: ",k3)

#Q5:-
h1=[]
h2=[]
for i in range(1,102):
    if(i%2==0):
        h1.append(i)
print("even no.: ",h1)
for i in range(1,102):
    if(i%2!=0):
        h2.append(i)
print("odd no.: ",h2)

#Q6:-
for i in range(0,4):
    for j in range(0,i+1):
        print("* ",end="")
    print()

#Q7:-
a=input("enter name: ")
b=input("enter age: ")
c=input("enter gender: ")
d=input("enter phone no.: ")
e=input("enter marks: ")
d1={'name':a,'age':b,'gender':c,'phone no.':d,'marks':e}
for key in d1:
    print(key)

#Q8:
list=[]
for i in range(1,10):
    s=input("enter list values: ")
    list.append(s)
print(list)
r=input("enter value: ")
if list.index(r):
    j=list.index(r)
    del list[j]
print(list)
