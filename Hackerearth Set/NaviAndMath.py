# NAVI AND MATH

def power(base, exp):
    res = 1
    while exp>0:
        if exp&1:
            res = (res*base)%1000000007
        exp = exp>>1
        base = (base*base)%1000000007
    return res%1000000007

mod = 1000000007
for i in range(int(input().strip())):
    ans = "Case #" + str(i+1) + ': '
    N = int(input().strip())
    Arr = [int(a) for a in input().strip().split()]
    mask = 3
    maxx = -1
    #ct = 0
    while mask<(1<<N):
        p = 0
        sm = 0
        ml = 1
        #ct += 1
        for j in range(0,N,1):
            if mask&(1<<j):
                sm += Arr[j]
                ml = (ml*Arr[j])%mod
                #print(Arr[j])
        p = (ml*power(sm,mod-2))%mod
        if maxx<p:
            maxx = p
            #print(maxx)
        mask += 1
    #print(ct)
    ans += str(maxx)
    print(ans)
