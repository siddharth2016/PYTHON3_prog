# THE OLD MONK

for _ in range(int(input())):
    N = int(input())
    A = [int(a) for a in input().split()]
    B = [int(a) for a in input().split()]
    res = 0
    mx = 0
    for i in range(N):
        for j in range(i,N,1):
            if A[i]>B[j]:
                break
            res = j-i
            if res>mx:
                mx = res
    print(mx)
