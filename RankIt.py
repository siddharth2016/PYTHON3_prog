# RANK IT

def Bins(n,h,A):
    low = 0
    high = h-1
    while low<=high:
        mid = (low+high)//2
        if A[mid]<n:
            low = mid + 1
        elif A[mid]>n:
            high = mid - 1
        else:
            return mid

N = int(input())
A = [int(a) for a in input().strip().split()]
A.sort()
for i in range(int(input())):
    x = int(input())
    print(Bins(x,N,A) + 1)
