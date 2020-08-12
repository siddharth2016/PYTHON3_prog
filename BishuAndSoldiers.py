# BISHU AND SOLDIERS

def Bin(n,h,A):
    low = 0
    high = h-1
    while high>=low:
        mid = (low+high)//2
        if A[high]<=n:
            return high
        elif A[mid]>n:
            high = mid - 1
        elif A[mid]==n:
            return mid

N = int(input())
A = []
for i in range(N):
    A += [int(input())]
A.sort()
for i in range(int(input())):
    x = int(input())
    ind = Bin(x, N, A)
    #print(ind)
    print(ind+1, sum(A[:ind+1]))
