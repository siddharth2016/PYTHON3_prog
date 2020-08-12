# ANIRUDDHA'S QUEUE

for _ in range(int(input())):
    n = int(input())
    A = [int(a) for a in input().split()]
    m = int(input())
    sm = 0
    i = 0
    tsm = sum(A)
    rem = m%tsm
    if rem==0:
        for j in range(n):
            sm += A[j]
            if sm==tsm:
                print(j+1)
                break
    else:
        while(True):
            sm += A[i]
            if sm>=rem:
                print(i+1)
                break
            i = (i+1)%n
            
