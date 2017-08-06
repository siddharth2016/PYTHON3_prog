# MONK AND ROTATIONS

for _ in range(int(input())):
    res = []
    n,k = list(map(int, input().split()))
    Arr = input().split()
    k = k%n
    if k==0:
        print(' '.join(Arr))
    else:
        for i in range(n-k,n,1):
            res.append(Arr[i])
        for i in range(n-k):
            res.append(Arr[i])
        print(' '.join(res))

