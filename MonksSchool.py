# MONKS SCHOOL

def merge(A,B):
    (C,m,n,i,j) = ([],len(A),len(B),0,0)
    while (i+j)<(m+n):
        if i == m:
            C.append(B[j])
            j += 1
        elif j == n:
            C.append(A[i])
            i += 1
        elif int(A[i][1])<int(B[j][1]):
            C.append(A[i])
            i += 1
        elif int(A[i][1])>int(B[j][1]):
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

n,m = list(map(int, input().split()))
teaches = {}
teacher = []

for i in range(n):
    teacher += [str(input())]
    teaches[teacher[i]] = []
#print(teacher,teaches)
teacher = sorted(teacher)

for i in range(m):
    a,b,c = input().split()
    teaches[a] += [(b,c)]
#print(teaches,teacher)

for faculty in teacher:
    print(faculty)
    A = mergesort(teaches[faculty],0,len(teaches[faculty]))
    for student in A:
        print(" ".join(student))
