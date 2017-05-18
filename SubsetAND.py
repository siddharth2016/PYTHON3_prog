# SUBSET AND

import sys
for i in range(int(input().strip())):
    zn = [int(a) for a in input().strip().split()]
    z = zn[0]
    A = [int(a) for a in input().strip().split()]
    f = 0
    for i in range(zn[1]):
        z = z&A[i]
        if z==0:
            f = 1
            print('Yes')
            break
    if f!=1:
        print("No")
