# LUCKY NUMBERS

A = []
for i in range(61):
    x = 2**i
    A = A + [x]

for i in range(int(input())):
    N = int(input())
    res = 0
    for j in range(1,61,1):
        if A[j]>N:
            break
        for k in range(0,j,1):
            if (A[j]+A[k])>N:
                break
            res = (res + A[j] + A[k])%1000000007
    print(res)
