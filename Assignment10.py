#Q1:-
class Animal():
    def animal_attribute(self):
        self.age=int(input("enter age of animal:-"))
        b=self.age
        print("Age of animal is:- ",b)
class Tiger(Animal):
    def __init__(self):
        print("inherted class:-")
g=Tiger()
g.animal_attribute()

#Q2:-Show the output of following program:-
#class A:
#    def f(self):
#        return self.g()
#     def g(se3lf):
#        return 'A'
#class B(A):
#    def g(self):
#        return 'B'
#a = A()
#b = B()
#print(a.f(), b.f())
#print(a.g(), b.g())
print("Output of first print command is:- A B")
print("Output of second print command is:- A B")

#Q3:-
class Cop():
    def __init__(self,name,age,work,experience,designation):
        self.a=name
        self.b=age
        self.c=work
        self.d=experience
        self.e=designation

    def display(self):
        e=self.a
        f=self.b
        g=self.c
        h=self.d
        i=self.e
        print("name:- ", e)
        print("age:- ", f)
        print("work:-", g)
        print("experience:-", h)
        print("designation:-",i)

    def update(self):
        self.a=input("enter name:- ")
        self.b=input("enter age:- ")
        self.c=input("enter work:- ")
        self.d=input("enter experience:- ")
        self.e=input("enter designation:- ")
        e=self.a
        f=self.b
        g=self.c
        h=self.d
        i=self.e
        print("name:- ", e)
        print("age:- ", f)
        print("work:- ", g)
        print("experience:- ", h)
        print("designation:- ", i)
class Mission(Cop):
    def add_mission_details(self):
        print("Mission name:-Aadhar project")
        print("Team Members:-10")
        print("Expereanced staff members:-5")
        print("Freshers:-2")
        print("Experts:-3")
a=Cop('gourav',20,'coding',2,'developer')
a.display()
a.update()
b=Mission('putt',21,'coding',3,'android')
b.display()
b.update()
b.add_mission_details()

#Q4:-
class Shape():
    def __init__(self,length,breadth):
        self.l = length
        self.b = breadth
        m = self.l
        n = self.b
    def Area(self):
        pass
class Rectangle(Shape):
    def __init__(self,length,breadth):
        print("calculating rectangle area:-")
        self.l = length
        self.b = breadth
    def Area(self):
        m = self.l
        n = self.b
        print("Area of rectangle:- ",m*n)
class Square(Shape):
    def __init__(self,side):
        print("calculating square area:-")
        self.s = side
    def Area(self):
        h = self.s
        print("Area of square :- ",h*h)
g=Shape(4,5)
g.Area()
m=Rectangle(4,5)
m.Area()
n=Square(4)
n.Area()



