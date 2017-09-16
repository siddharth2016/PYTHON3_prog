# FIBONACCI METHOD

t1,t2,n = list(map(int, input().split()))
n = n-2
def fibo(t1,t2,n):

    if n==0:
        return t2

    else:
        temp = t1 + t2**2
        t1 = t2
        t2 = temp
        n = n-1
        return fibo(t1,t2,n)

print(fibo(t1,t2,n))
