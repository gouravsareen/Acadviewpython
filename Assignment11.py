#Q1:-
import threading
from threading import Thread
import time
class mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.g=i
    def run(self):
        time.sleep(5)
        print("value send:- ",self.g)
thread1=mythread(10)
thread1.start()
time.sleep(5)

#Q2:-
import threading
from threading import Thread
import time
class test(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(11):
            time.sleep(1)
            print("values are:- ",i)
thread1=test()
thread1.start()
time.sleep(12)

#Q3:-
import threading
from threading import Thread
import time
class Test1(threading.Thread):
    def __init__(self,g,h):
        threading.Thread.__init__(self)
        self.s=g
        self.t=h
    def run(self):
        g=self.s
        h=self.t
        for i in range(5):
            print("values are:- ",g[i])
            time.sleep(h[i])
g=[1,2,3,4,5]
h=[2,4,6,8,10]
thread2=Test1(g,h)
thread2.start()
time.sleep(22)

#Q4:-
import threading
from threading import Thread
import time
import math
class Test2(threading.Thread):
    def __init__(self,a):
        threading.Thread.__init__(self)
        self.k=a
    def run(self):
        n=self.k
        print("The factorial is: ",end="")
        print(math.factorial(n))
thread3=Test2(5)
thread3.start()






















