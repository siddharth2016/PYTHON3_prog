# THE NORMAL TYPE   #INCOMPLETE

N = int(input())
Ar = [int(a) for a in input().strip().split()]
Br = len(set(Ar))
if Br==1:
    print(int((N*(N+1))/2))
elif Br==N:
    print(1)
else:
    i=j=res=0
    f = 1
    di = {}
    while j<N:
        if f:
            di[Ar[j]] = di[Ar[j]] + 1 if Ar[j] in di else 1
            if len(di)==Br:
               f = 0
            else:
                j += 1
        else:
            res += (N-j)
            if di[Ar[i]]>1:
                di[Ar[i]] -= 1
            else:
                di.pop(Ar[i])
                f = 1
                j += 1
            i += 1
    print(res)
