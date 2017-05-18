# SAMU AND HER BIRTHDAY PARTY           

for i in range(int(input().strip())):
    n,k = [int(a) for a in input().strip().split()]
    Ar = []
    for j in range(n):
        Ar += [int(input(), 2)]
    #print(Ar)
    f = 0
    for j in range((1<<(k))):
        for m in Ar:
            if j&m==0:
                f=0
                break
            elif j&m!=0:
                f=1
        if f:
            k = min(bin(j).count('1'), k)
        f = 0
    print(k)
