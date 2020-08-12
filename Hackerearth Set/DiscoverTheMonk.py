# DISCOVER THE MONK

def Bin(i,A,l):
    low = 0
    high = l-1
    if A[high]<i or A[low]>i:
        return 0
    while low<=high:
        mid = (low+high)//2
        if A[mid]>i:
            high = mid - 1
        elif A[mid]<i:
            low = mid + 1
        elif A[mid]==i:
            return 1
    return 0


n,q = tuple(map(int, input().split()))
Ar = [int(a) for a in input().strip().split()]
Ar.sort()
for i in range(q):
    x = int(input())
    if Bin(x,Ar,n):
        print("YES")
    else:
        print("NO")
