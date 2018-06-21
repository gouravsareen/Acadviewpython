#Q1:-what is time tuple.
print("Many of Python's time functions handle time as a tuple of nine numbers ,as shown below:-")
print("index:","    ","field:","            ","values:")
print("0","         ","tm_year","           ","2018")
print("1","         ","tm_mon","            ","1 to 12")
print("2","         ","tm_mday","           ","1 to 31")
print("3","         ","tm_hour","           ","0 to 23")
print("4","         ","tm_min","            ","0 to 59")
print("5","         ","tm_sec","            ","0 to 61(60 and 61 are leap year)")
print("6","         ","tm_wday","           ","0 to 6(0 is monday)")
print("7","         ","tm_yday","           ","1 to 366(julian day)")
print("8","         ","tm_isdst","          ","-1,0,1,-1,means library determines DST")
print("tm_year:-gives a 4 digits current year")
print("tm_mon:-gives the current month")
print("tm_mday:-gives the current day")
print("tm_hour:-gives the current hour")
print("tm_min:-gives the current minute")
print("tm_sec:-gives the current second")
print("tm_wday:-gives the current day of week")
print("tm_yday:-gives the current day of year")
print("tm_isdst:-gives the daylight savings")

import datetime
print(datetime.datetime.now().time())

#Q3:-
import datetime
d=datetime.date.today()
print("Month:- ",d.month)

#Q4:-
import datetime
d=datetime.date.today()
print("date:- ",d.day)

#Q5:-
from time import localtime,strftime
print(strftime("%d",localtime()))

#Q6:-
from time import localtime,strftime
print(strftime("%H:%M:%S",localtime()))

#Q7:-
import math
n=int(input("enter a number: "))
print("The factorial is: ",end="")
print(math.factorial(n))

#Q8:-
import math
m=int(input("enter a number: "))
n=int(input("enter a number: "))
print("The GCD of the number is: ",end="")
print(math.gcd(m,n))

#Q9:-
import os
print(os.name)
print(os.environ)