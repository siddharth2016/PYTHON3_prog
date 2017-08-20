# MERGESORT ALGORITHM

def merge(A,B):
    (C,m,n) = ([],len(A),len(B))
    (i,j) = (0,0)
    while (i+j)<(m+n):

        if i == m:
            C.append(B[j])
            j += 1
        elif j == n:
            C.append(A[i])
            i += 1
        elif A[i]<=B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    print(C)
    return(C)

def mergesort(A,left,right):
    if right - left <=1:
        return(A[left:right])
    else:
        mid = (right+left)//2
        L = mergesort(A,left,mid)
        R = mergesort(A,mid,right)
        return(merge(L,R))

a = list(range(5,0,-1))
print(mergesort(a,0,len(a)))
