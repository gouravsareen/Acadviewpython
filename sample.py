def fn(a):
    print(a*a)
fn(5)

def add(a,b):
    d=a*a
    c=b*b*b
    return d,c
m,n=add(2,3)
print(str(m)+" "+str(n))

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


