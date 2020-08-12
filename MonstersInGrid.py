# MONSTER IN GRID

n,m,k = [int(a) for a in input().split()]
A = []
for i in range(n):
    A += [[int(a) for a in input().split()]]
ans = 0
for i in range(1<<m):
    v = k - bin(i).count('1')
    if v<=0:
        continue
    va = []
    for a in range(0,n,1):
        summ = 0
        for b in range(0,m,1):
            if (i>>b)&1:
                if A[a][b]==1:
                    summ += 1
        va += [summ]

    va.sort(reverse = True)
    l = 0
    v = min(v,n)
    for i in range(v):
        l += va[i]
    ans = max(ans,l)
print(ans)
