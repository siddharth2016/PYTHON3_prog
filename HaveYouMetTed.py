# HAAAAVE YOU MET TED!?

for i in range(int(input().strip())):
    n = int(input().strip())
    Ar = [int(a) for a in input().strip().split()]
    minn = 100
    for j in range(0,n,1):
        if bin(Ar[j]).count('1')<minn:
            minn = bin(Ar[j]).count('1')
    print(minn)
