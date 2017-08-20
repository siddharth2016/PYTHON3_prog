# MERGESORT INVERSION PROBLEM

def merge(A,B):
    #print(A,B)
    (m,n,count,i,j) = (len(A),len(B),0,0,0)
    while (i+j)<(m+n):
        if i == m:
            j += 1
        elif j == m:
            i += 1
        elif A[i]<=B[j]:
            i += 1
        elif A[i]>B[j]:
            j += 1
            count += (m-i)
    #print(count)
    return(count)

def mergesort(A,left,right):
    if right-left<=1:
        return 0
    else:
        mid = (left+right)//2
        L = mergesort(A,left,mid)
        R = mergesort(A,mid,right)
        return(merge(A[left:mid],A[mid:right])+L+R)

#print(mergesort([1,4,6,3,2,5],0,6))
n = int(input())
Arr = list(map(int, input().split()))
print(mergesort(Arr,0,n))
