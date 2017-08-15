# NPTEL WEEK 3 PROGRAMMING ASSIGNMENT

def ascending(l):
    if len(l)==0:
        return(True)
    for i in range(len(l)-1,0,-1):
        if l[i]<l[i-1]:
            return(False)
    return(True)

#print(ascending([2,3,4,5,1]))
#print(ascending([1,2,3,4,5,5]))

def valley(l):
    if len(l)<3:
        return(False)
    for i in range(0,len(l),1):
        if i==len(l)-1:
            return(False)
        if l[i]==l[i+1]:
            return(False)
        if l[i]<l[i+1]:
            break
    if len(l[i:])<2:
        return(False)
    for j in range(i,len(l),1):
        if j==len(l)-1:
            return(True)
        if l[j]==l[j+1]:
            return(False)
        if l[j]>l[j+1]:
            return(False)

#print(valley([3,2,1,2,3]))
#print(valley([3,3,2,3]))
#print(valley([5,4,3,2,1,2]))
#print(valley([17,1,2,3,4,5]))
#print(valley([13,12,14,14]))

def transpose(A):
    B = []
    C = []
    col = len(A[0])
    row = len(A)
    for i in range(col):
        C = []
        for j in range(row):
            C.append(A[j][i])
        B.append(C)
    return(B)

#print(transpose([[1,4,9]]))
#print(transpose([[1,3,5],[2,4,6]]))
#print(transpose([[1,2]]))
