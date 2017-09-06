# NPTEL EX 4

def frequency(l):
    setl = list(set(l))
    a = []
    minf = []
    maxf = []
    mx = 0
    mn = 10**7
    for i in range(len(setl)):
        x = l.count(setl[i])
        a.append(x)
        if x>mx:
            mx = x
        if x<mn:
            mn = x
    for i in range(len(a)):
        if a[i]==mn:
            minf.append(setl[i])
        if a[i]==mx:
            maxf.append(setl[i])
    tup = ()
    minf.sort()
    maxf.sort()
    tup += (minf,maxf)
    return(tup)

#print(frequency([13,12,11,13,14,13,7,11,13,14,12,14,14,7]))
#print(frequency([1,2,3,4,5,5,4,3,2,3,4,5,5,4,5]))
#print(frequency([1,1,1,1,1]))
#print(frequency([4,4,4,1,1,2,2,2,3,3]))

def merge(A,B):
    (C,m,n,i,j) = ([],len(A),len(B),0,0)
    while (i+j)<(m+n):
        if i==m:
            C.append(B[j])
            j+=1
        elif j==n:
            C.append(A[i])
            i+=1
        elif A[i][0]>B[j][0]:
            C.append(B[j])
            j += 1
        elif A[i][0]==B[j][0]:
            if A[i][1]>B[j][1]:
                C.append(B[j])
                j += 1
            else:
                C.append(A[i])
                i += 1
        else:
            C.append(A[i])
            i += 1
    return(C)

def mergesort(A,left,right):
    if right-left<=1:
        return(A[left:right])
    else:
        mid = (left+right)//2
        L = mergesort(A,left,mid)
        R = mergesort(A,mid,right)
        return(merge(L,R))

def onehop(l):
    d = {}
    ans = []
    for i in range(len(l)):
        d.setdefault(l[i][0], [])
        d[l[i][0]].append(l[i][1])
    #print(d)
    for key in d:
        for i in range(len(d[key])):
            if d[key][i] in d:
                temp = d[key][i]
                #print("#",temp)
                for j in range(len(d[temp])):
                    if d[temp][j]!=key and (key,d[temp][j]) not in ans:
                        ans.append((key,d[temp][j]))
                        #print(ans)
    #print(ans)
    ans = mergesort(ans,0,len(ans))
    return(ans)

#print(onehop([(2,3),(1,2),(3,1),(1,3),(3,2),(2,4),(4,1)]))
#print(onehop([(1,2),(3,4),(5,6)]))
#print(onehop([(1,2),(2,1)]))
#print(onehop([(1,2)]))
#print(onehop([(1,3),(1,2),(2,3),(2,1),(3,2),(3,1)]))
