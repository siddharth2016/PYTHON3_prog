# JARVIS AND LONE INTEGER

import sys
for i in range(int(input().strip())):
    N = int(input().strip())
    Arr = [int(arr) for arr in input().strip().split()]
    Arr.sort()
    j=0
    res = -1
    while j<N:
        x = Arr.count(Arr[j])
        if x%2==0:
            j = j + x
        else:
            res = Arr[j]
            break
    print(res)
