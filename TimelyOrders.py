# TIMELY ORDERS

def Bin(n,A,h):
    low = 0
    high = h-1
    if A[high]<=n:
        return high
    while low<=high:
        mid = (low+high)//2
        if A[mid]==n:
            return mid
        elif A[mid]>n:
            if mid==high:
                break
            high = mid
        elif A[mid]<n:
            if mid==low:
                break
            low = mid
    if A[low]>n:
            return -1
    return low

W = [0]
T = []
res = 0
for i in range(int(input())):
    a,x,t = [int(a) for a in input().strip().split()]
    if a == 1:
        W += [x+W[-1]]
        T += [t]
    elif a == 2:
        l = len(T)
        res = W[Bin(t,T,l)+1] - W[Bin(t-x-1,T,l)+1]
        print(res)
