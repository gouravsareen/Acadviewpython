#Q1:-
radius=float(input("enter radius:- "))
def area(rad):
    area=(3.14*rad*rad)
    return area
ar=area(radius)
print("Area:- ",ar)

#Q2:-
n=6
def perfect(n):
    sum = 0
    for i in range(1,n):
        if(n%i==0):
            sum=sum+i
    if(sum==n):
        return True
    else:
        return False
for i in range(1,1001):
    if(perfect(i)==True):
        print(i)

#Q3:-
def multiply(a,b=1):
    if b==11:
        return None
    print(str(a)+"x"+str(b)+"="+str(a*b))
    multiply(a,b+1)
multiply(12)

#Q4:-
def power(m=3,n=4):
    if(n==1):
        return m
    if(n!=1):
        return(m*power(m,n-1))
print("Result of power: ",power())

#Q5:-
dict={}
def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)
n=int(input("enter number: "))
print("factorial: ",factorial(n))
a=n
b=factorial(n)
dict['number']=a
dict['fact_result']=b
print(dict)



