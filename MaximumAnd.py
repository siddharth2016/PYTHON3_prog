# MAXIMUM 'AND'

import sys
for i in range(int(input().strip())):
    x = [int(arr) for arr in input().strip().split()]
    A = x[0]
    B = x[1]
    if B-A==1:
        print(A&B)
    elif B%2==1:
        print(B-1)
    else:
        print((B-1)&(B-2))
