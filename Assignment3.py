#Q1:-Create a list with user defined inputs.

a=input("enter elements: ")
l=[]
l.append(a)
print("elements are:",l)


#Q2:-Add the following list to above created list:
    #'google','apple','facebook','microsoft','tesla'

m=['google','apple','facebook','microsoft','tesla']
print(l+m)

#Q3:-Count the no. of times an object occur in the list.

g=['goru','akshu','putt','akshu']
print(g.count('akshu'))

#Q4:-Create a list with numbers and sort it in ascending order.

a=[10,31,56,77,34]
a.sort()
print('Sorted elements are: ',(a))

#Q5:-Given are two one-dimensional arrays A and B which are sorted in ascending order.Write a program to merge them into a singal sorted array C that contains every item from arrays A and B,in ascending order.[List]

A=[19,10,56,34,78]
B=[90,45,87,23,42]
A.sort()
B.sort()
C=print('Sorted elements are: ',(A+B))

#Q6:-Implement a stack and queue using lists.

#STACK
stack=[1,2,3,4]
stack.append(5)
stack.append(6)
print('after elements append: ',stack)
stack.pop()
print('after pop1: ',stack)
stack.pop()
print('after pop2: ',stack)

#QUEUE
from collections import deque
queue=deque([1,2,3,4])
print(queue)
queue.append(5)
queue.append(6)
print('after elements append: ',queue)
queue.popleft()
print('elements after pop1: ',queue)
queue.popleft()
print('elements after pop2: ',queue)

#Q7:-Count even and odd numbers in that list.

List=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
count_odd=0
count_even=0
for x in List:
    if not x%2:
        count_even=count_even+1
    else:
        count_odd=count_odd+1
print('Total even no. are: ',count_even)
print('Total odd no. are: ',count_odd)






