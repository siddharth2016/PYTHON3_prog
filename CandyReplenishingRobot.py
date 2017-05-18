# CANDY REPLENISHING ROBOT

n,t = [int(a) for a in input().strip().split()]
Ar = [int(a) for a in input().strip().split()]
i = 0
c = n
count = 0
while t:
    #print(c)
    if c<5:
        count += (n-c)
        c += (n-c)
        #print(count)
    c -= Ar[i]
    t -= 1
    i += 1
print(count)
