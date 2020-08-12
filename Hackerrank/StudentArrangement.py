# STUDENT ARRANGEMENT

from sys import stdin, stdout

def nextrow(i,A):
    count = 0
    while True:
        if len(A)==0:
            return 1
        elif i in A:
            return i
        i = (i+1)%l
        count += 1
        if count >= len(A):
            break
    return 1

n,m,k = [int(a) for a in stdin.readline().split()]
Ar = list(map(int, stdin.readline().split()))
count = 0
d = {}
for i in range(1,m+1,1):
    d[i] = k
for i in range(n):
    #print(i)
    if Ar[i] in d:
        d[Ar[i]] -= 1
        if d[Ar[i]] == 0:
            del d[Ar[i]]
    else:
        x = nextrow(Ar[i]+1,d)
        #print(x)
        if x == 1:
            count += n-i
            break
        count += 1
        d[x] -= 1
        #print(d[x])
        if d[x] == 0:
            del d[x]
stdout.write(str(count)+"\n")
