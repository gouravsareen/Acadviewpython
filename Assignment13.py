#Q1:-
try:
    a=3
    if(a<4):
        a=a/(a-3)
        print(a)
except ZeroDivisionError:
    print("division by zero")
finally:
    print("it must execute")


#Q2:-
try:
    l=[1,2,3]
    print(l[3])
except IndexError:
    print("Index doesn't exist")


#Q3:-
try:
    raise NameError("Hi there")
except NameError:
    print("An Exception")
print("Output of this program is:- An Exception")


#Q4:-
def AbyB(a,b):
    try:
        c=((a+b)/(a-b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print("Division:- ",c)
AbyB(2.0,3.0)
AbyB(3.0,3.0)
print("output:-1    Division=-5.0")
print("output:-2    a/b result in 0")


#Q5:-
try:
    import gourav
except ImportError:
    print(" not existed file import")
try:
    m = [1, 2, 3, 4]
    print(m[4])
except IndexError:
    print("Index out of range")
try:
    age=int(input("enter age:-"))
    if(age<18):
        print("age is:- ",age)
    else:
        print("age is larger than 18")
except ValueError:
    print("entered value is not an integer")


#Q6:-
class AgeTooSmallError(Exception):
    pass
while(True):
    try:
        uage = int(input("enter the age:- "))
        if(uage<18):
            raise AgeTooSmallError
    except ValueError:
        print("entered value is not an integer")
    except AgeTooSmallError:
        print("WARNING! Entered Age Is Small")
        True
        continue
    else:
        print("you are eligible.The age is:-",uage)
        break


















