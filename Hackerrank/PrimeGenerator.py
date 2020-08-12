# PRIME GENERATOR

from math import sqrt

prime = [1]*100000
A = set()
def sieve(n):
    if len(A)!=0:
        t = list(A)[len(A)-1]+1           
        for i in range(t,int(sqrt(sqrt(n)))+1,1):
            if prime[i]:
                for j in range(i*i,int(sqrt(n))+1,i):
                    prime[j]=0
        for i in range(t,int(sqrt(n))+1,1):
            if prime[i]:
                A.add(i)
    else:            
        for i in range(2,int(sqrt(sqrt(n)))+1,1):
            if prime[i]:
                for j in range(i*i,int(sqrt(n))+1,i):
                    prime[j]=0
        for i in range(2,int(sqrt(n))+1,1):
            if prime[i]:
                A.add(i)
    return list(A)

for i in range(int(input().strip())):
    l,r = [int(a) for a in input().strip().split()]
    Ar = sieve(r)
    #print(A)
    diff = r-l+1
    B = [1]*(diff)
    for j in Ar:
        x = int(l/j)*j
        for k in range(x,r+1,j):
            if l<=k<=r:
                if B[diff-(r-k+1)] and (k not in Ar):
                    B[diff-(r-k+1)]=0
    for j in range(len(B)):
        if B[j] and j+l!=1:
            print(j+l)
    print()
