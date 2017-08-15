# ROY AND TRAINS
from math import ceil
#take input
for _ in range(int(input())):
    t0,t1,t2,v1,v2,d = list(map(int, input().split()))
    if t0<=t1 or t0<=t2:
        if t0>t1:
            t2 += int(ceil((d/v2)*60))
            print(t2)
        elif t0>t2:
            t1 += int(ceil((d/v1)*60))
            print(t1)
        else:
            t1 += int(ceil((d/v1)*60))
            #print(t1)
            t2 += int(ceil((d/v2)*60))
            #print(t2)
            if t1<t2:
                print(t1)
            elif t2<t1:
                print(t2)
            else:
                print(t1)
    else:
        print(-1)
