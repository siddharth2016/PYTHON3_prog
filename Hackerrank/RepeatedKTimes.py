# RESPEATED K TIMES

import collections
n = int(input())
Arr = [int(a) for a in input().split()]
k = int(input())
Arr.sort()
SetA = collections.Counter(Arr)
for i in SetA.keys():
    if SetA[i]==k:
        print(i)
        break
