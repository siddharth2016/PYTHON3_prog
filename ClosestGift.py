# CLOSEST GIFT

from math import sqrt
def prime(n):
    for i in range(2,int(sqrt(n)),1):
        if n%i==0:
            return 0
    if n!=1 and n!=0:
        return 1
    else:
        return 0
n = int(input())
if prime(n):
    print('0')
else:
    for i in range(n,n+15,1):
        if prime(i):
            print(i-n)
            break
