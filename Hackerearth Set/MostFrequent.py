# MOST FREQUENT

n,mx,mn=int(input()),0,10**4
A=[int(a) for a in input().split()]
a=set(A)
for i in a:
    q=A.count(i)
    if q>mx:
        mx = q
        mn = i
    elif q==mx and i<mn:
        mn = i
print(mn)
