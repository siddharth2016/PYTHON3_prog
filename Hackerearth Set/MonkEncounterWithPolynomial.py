# MONK ENCOUNTER WITH POLYNOMIAL

from math import sqrt,ceil

def binarysearch(a,b,c,k,l,r):
    if (a*(l**2) + b*l + c)>=k:
        return(l)
    else:
        mid = (l+r)//2
        if (a*(mid**2)+b*mid+c)==k:
            return(mid)
        if (a*(mid**2)+b*mid+c)<k:
            return binarysearch(a,b,c,k,mid+1,r)
        if (a*(mid**2)+b*mid+c)>k:
            return binarysearch(a,b,c,k,l,mid)


for _ in range(int(input())):
    a,b,c,k = [int(i) for i in input().strip().split()]
    if c>=k:
        print(0)
    else:
        mxr = ceil(sqrt(k))
        print(binarysearch(a,b,c,k,1,mxr))
            
