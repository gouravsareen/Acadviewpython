#Q1:-
import numpy as np
a=np.random.rand(10,1)
print(a)
print("Mean:- ",a.mean())

#Q2:-
import numpy as np
b=np.random.rand(20,1)
print(b)
print("Variance:- ",b.var())
print("Standard Deviation:- ",b.std())

#Q3:-
import numpy as np
a=np.random.rand(10,20)
b=np.random.rand(20,25)
print("Array-1:---",a)
print("Array-2:---",b)
c=np.dot(a,b)
print("Multiply:---",c)
print("Shape of c Array:-",c.shape)
print("Sum of elements of Array c:-",np.sum(c))

#Q4:-
import numpy as np
def function(x):
    return (1/(1+(np.exp(-x))))
arr=np.random.rand(10,1)
print("Random no. Array:-",arr)
arr=function(arr)
print("required output:-",arr)




