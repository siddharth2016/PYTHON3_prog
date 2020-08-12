# MISSING SOLDIERS

def merge(A,B):
    (C,m,n,i,j) = ([],len(A),len(B),0,0)
    while (i+j)<(m+n):
        if i == m:
            C.append(B[j])
            j += 1
        elif j==n:
            C.append(A[i])
            i += 1
        elif A[i][0]<=B[j][0]:
            C.append(A[i])
            i += 1
        elif A[i][0]>B[j][0]:
            C.append(B[j])
            j += 1
    return(C)

def mergesort(A,left,right):
    if right-left<=1:
        return(A[left:right])
    else:
        mid = (left+right)//2
        L = mergesort(A,left,mid)
        R = mergesort(A,mid,right)
        return(merge(L,R))
Arr = []
for _ in range(int(input())):
    x,y,d = list(map(int, input().split()))
    Arr.append([x,x+d])

res = mergesort(Arr,0,len(Arr))
#print(res)
mark = count = 0
for i in res:
    if mark<=i[0]:
        mark = i[0]
        count += i[1] - mark + 1
        mark = i[1]+1
    elif mark<=i[1]:
        count += i[1] - mark + 1
        mark = i[1] + 1
print(count)

