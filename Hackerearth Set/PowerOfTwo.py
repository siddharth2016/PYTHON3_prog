# POWER OF TWO

from math import log

for i in range(int(input())):
    N = int(input())
    Ar = [int(a) for a in input().split()]
    sub = 2**N - 1
    f = 0
    for j in range(0,32,1):
        res = 2**32 - 1
        for k in range(N):
            if Ar[k]&(1<<k):
                res &= Ar[k]
        
        if res&(res-1)==0 and res!=0:
            f = 1
            break
        else:
            f = 0
    if f:
        print("YES")
    else:
        print("NO")
