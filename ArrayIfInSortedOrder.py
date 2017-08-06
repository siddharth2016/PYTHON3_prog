# CHECKING ARRAY IF IN SORTED ORDER

def checkSorted(n,A,i):
    if i==n:
        return 1
    if A[i]>=A[i-1]:
        return checkSorted(n,A,i+1)
    else:
        return 0
n = int(input("Enter number of elements :"))
Arr = [int(a) for a in input().split()]
if checkSorted(n,Arr,1):
    print("Sorted")
else:
    print("Not Sorted")
