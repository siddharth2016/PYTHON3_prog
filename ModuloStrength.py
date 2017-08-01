(n,k),sm=[int(a) for a in input().split()],0
A,r=[int(a)%k for a in input().split()],[0]*k
for i in A:
    if r[i]:
        continue
    r[i]=A.count(i)
    sm += r[i]*(r[i]-1)
print(sm)
