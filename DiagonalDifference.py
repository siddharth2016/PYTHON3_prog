# DIAGONAL DIFFERENCE

N = int(input())
Ar = []
for i in range(N):
    Ar.append([int(a) for a in input().strip().split()])
countpd = countd = 0
j = 0
k = N-1
for i in range(N):
    countpd += Ar[i][j]
    countd += Ar[i][k]
    j += 1
    k -= 1
print(abs(countpd - countd))
