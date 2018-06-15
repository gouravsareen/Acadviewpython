#TUPLES:
#Q1:-Write a program to create a tuple with different data types and do the following operations.
    #1.Find the length of tuple.
from typing import Tuple

t=(1,2.5,'gourav',[3,"dog"],{'name':'sareen'})
print('Length of tuple is:',len(t))

#Q2:-Find largest and smallest elements of a tuple.
t1=(12,56,98,43,76)
print('Largest value in tuple t1 is:',max(t1))
print('Smallest value in tuple t1 is:',min(t1))

#Q3:-Write a program to find the product of all elements of a tuple.
t2=(3*5*7*9)
print('Product of elements is:',t2)

#SETS:
#Q1:-Create two sets using user define values.
    #1.Calculate difference between two sets:
a=input("enter elements: ")
t3=set()
t3.update(a)
print("elements are:",t3)
b=input("enter elements: ")
t4=set()
t4.update(b)
print("elements are:",t4)
print('Difference between two sets is:',(t3-t4))
print('Difference between two sets is:',(t4-t3))

    #2.Compare two sets.
print((t3>=t4))
print((t3<=t4))
print((t4>=t3))
print((t4<=t3))


    #3.Print the result of intersection of two sets.

print('Intersection of two sets is:',t3&t4)

#DICTIONARIES:
#Q1:-Create a dictionary to store name and marks of student by user input.
a=input("enter name: ")
b=input("enter marks: ")
d={'name':a,'marks':b}
print(d)

#Q2:-Sort the dictionary created in last question according to marks.
t={'goru':98,'akshi':99,'putt':40,'varinda':60,'ankush':50}
from collections import OrderedDict
dd=OrderedDict(sorted(t.items(),key=lambda x:x[1]))
print(dd)

#Q3:-Count the number of occurrence of each letter in word "MISSISSIPPI".Store count of every letter with the letter in a dictionary.
l=['M','I','S','S','I','S','S','I','P','P','I']
dicti={'M':l.count('M'),'I':l.count('I'),'S':l.count('S'),'P':l.count('P')}
print(dicti)






