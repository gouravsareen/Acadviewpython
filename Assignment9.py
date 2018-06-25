#Q1:-
class Circle():
    def __init__(self):
        self.r=int(input("enter radius:- "))
        q=self.r
        print("radius:-",q)
    def getArea(self):
        q=self.r
        m=(3.14*q*q)
        print("Area:-",m)
    def getCircumstances(self):
        q=self.r
        n=(2*3.14*q)
        print("Circumstance:-",n)
a=Circle()
a.getArea()
a.getCircumstances()

#Q2:-
class Student():
    def __init__(self):
        self.n = input("enter name:- ")
        self.r = input("enter roll no:- ")
    def display(self):
        m=self.n
        n=self.r
        print("Name of student is:-",m)
        print("Roll_no of student is:- ",n)
a=Student()
a.display()

#Q3:-
class Temperature():
    def __init__(self):
        print("Temperature converter:-")
    def convertFahrenheit(self):
        self.a=int(input("enter celsius:- "))
        a=self.a
        b=(a*33.8)
        print("Fahrenheit:- ",b,"F")
    def convertCelsius(self):
        self.f=int(input("enter fahrenheit:- "))
        c=self.f
        d=(c/33.8)
        print("Celsius:-",d,"C")
a=Temperature()
a.convertFahrenheit()
a.convertCelsius()

#Q4:-
class MovieDetails():
    def __init__(self,Movie_name,artistname,year_of_release,ratings):
        self.a=Movie_name
        self.b=artistname
        self.c=year_of_release
        self.d=ratings
    def display(self):
        e=self.a
        f=self.b
        g=self.c
        h=self.d
        print("Movie_name:- ",e)
        print("artistname:- ",f)
        print("year_of_release:-",g)
        print("ratings:-",h)
    def update(self):
        self.a=input("enter movie name:- ")
        self.b=input("enter artist name:- ")
        self.c=input("enter year of release:- ")
        self.d=input("enter movie ratings:- ")
        e = self.a
        f = self.b
        g = self.c
        h = self.d
        print("Movie_name:- ", e)
        print("artistname:- ", f)
        print("year_of_release:-", g)
        print("ratings:-", h)
a=MovieDetails("race-2","saif",2015,4.5)
a.display()
a.update()

#Q5:-
class Expenditure():
    def __init__(self):
        self.a=int(input("enter expenditure:- "))
        self.b=int(input("enter savings:- "))
    def display(self):
        c=self.a
        d=self.b
        print("Expenditure:- ",c)
        print("Savings:- ",d)
    def total_salary(self):
        c=self.a
        d=self.b
        e=(c+d)
    def display_salary(self):
        c=self.a
        d=self.b
        e=(c+d)
        print("Total_salary:- ",e)
a=Expenditure()
a.display()
a.total_salary()
a.display_salary()