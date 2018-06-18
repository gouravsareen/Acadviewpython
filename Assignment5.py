#1.
a=int(input("enter a year"))
if(a%4==0):
        print("Entered year is leap year")
else:
    print("entered year is not a leap year")


#2.
a=int(input("enter the length"))
b=int(input("enter the breadth"))
if(a==b):
    print("square")
else:
    print("rectangle")

#3.
d=int(input("enter the age of d"))
e=int(input("enter the age of e"))
f=int(input("enter the age of f"))
if(d>e and d>f):
    biggest=d
    print("d is oldest")
elif(e>d and e>f):
    biggest=e
    print("e is oldest")
else:
    biggest=f
    print("f is oldest")
if(d<e and d<f):
    smallest=d
    print("d is youngest")
elif(e<d and e<f):
    smallest=e
    print("e is youngest")
else:
    smallest=f
    print("f is youngest")


#4.
g=int(input("enter a value between 1 to 200"))
if(g<=50):
    print("sorry! no prize this time")
elif(g>=51 and g<=150) :
    print("congratulations! you won a wooden dog")
elif(g>=151 and g<=180):
    print("congratulations! you won a Book")
elif(g>=181 and g<=200):
    print("congratulations! you won a Chocolates")
else:
    print("wrong choice")

#5.
n=int(input("enter the purchase quantity:"))
if(n<10):
    print("total cost=",n*100)
else:
    cost=n*100
    final_cost=cost-(cost*10)/100
    print("cost before discount: ",cost)
    print("cost after discount: ", final_cost)




