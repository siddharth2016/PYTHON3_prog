# PEBBLES GAME      INCOMPLETE

from math import sqrt,ceil
'''def quicksort(A,left,right):
    if right-left<=1:
        return()
    l = A[left]
    yellow = left+1
    for green in range(left+1,right,1):
        if A[green]<=l:
            (A[yellow],A[green]) = (A[green],A[yellow])
            yellow +=1
    (A[left],A[yellow-1]) = (A[yellow-1],A[left])

    quicksort(A,left,yellow)
    quicksort(A,yellow,right)

def findDistance(x1,y1,x2,y2):
    return(sqrt((x1-x2)**2 + (y1-y2)**2))

for _ in range(int(input())):
    n,m = list(map(int, input().split()))
    sortArr = list(map(int, input().split()))
    quicksort(sortArr,0,n)
    print(sortArr)
    res = 0
    res += findDistance(sortArr[0],sortArr[1],sortArr[1],sortArr[0])
    res += findDistance(sortArr[1],sortArr[0],sortArr[n-1],sortArr[0])
    res += findDistance(sortArr[n-1],sortArr[0],sortArr[n-1],sortArr[n-2])
    res += findDistance(sortArr[n-1],sortArr[n-2],sortArr[n-2],sortArr[n-1])
    res += findDistance(sortArr[n-2],sortArr[n-1],sortArr[0],sortArr[n-1])
    res += findDistance(sortArr[0],sortArr[n-1],sortArr[0],sortArr[1])
    res = ceil(res)
    print(m*res)
'''

for _ in range(int(input())):
    n,m=list(map(int, input().split()))
    A=list(map(int, input().split()))
    sm1=min(A)
    lr1=max(A)
    A.remove(sm1)
    A.remove(lr1)
    sm2=min(A)
    lr2=max(A)
    per=4*(lr1-sm1)
    q=sm2-sm1
    q1=q*q*2
    r=lr1-lr2
    r1=r*r*2
    h1=pow(q1,0.5)
    h2=pow(r1,0.5)
    
    ans=per-2*q-2*r+h1+h2
    print(ceil(ans)*m)
