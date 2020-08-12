# THE PRIME CELLS
P = [1]*40000
for i in range(2,40000,1):
    if P[i]:
        for j in range(i*i,40000,i):
            P[j]=0
def primecell(i,j,A,n):
    #print(i,j)
    sm = 0
    x = i
    y = j
    j += 1
    while j<=n-1:
        sm = sm + A[i][j]
        j += 1
    j = y
    i += 1
    while i<=n-1:
        sm = sm + A[i][j]
        i += 1
    i = x
    j -= 1
    while j>=0:
        sm = sm + A[i][j]
        j -= 1
    j = y
    i -= 1
    while i>=0:
        sm = sm + A[i][j]
        i -= 1
    i = x
    #print(sm)
    if P[sm] and sm!=1 and sm!=0:
        return sm
    else:
        return 1
        
n = int(input())
Arr = []
for i in range(n):
    Arr += [[int(a) for a in input().strip().split()]]
#print(Arr)
count = 0
for i in range(n):
    for j in range(n):
        ans = primecell(i,j,Arr,n)
        if ans!=1:
            count += 1
print(count)
