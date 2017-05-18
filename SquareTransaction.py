# SQUARE TRANSACTION

from itertools import accumulate
N = int(input())
Ar = list(accumulate(map(int, input().strip().split())))
print(Ar)
mx = Ar[-1]
for i in range(int(input())):
    tar = int(input())
    if mx<tar:
        print(-1)
    else:
        for a in range(N):
            if Ar[a]>=tar:
                print(a+1)
                break
