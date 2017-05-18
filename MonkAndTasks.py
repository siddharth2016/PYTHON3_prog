# MONK AND TASK

import sys
import operator
for i in range(int(input().strip())):
    N = int(input().strip())
    Arr = [int(a) for a in input().strip().split()]
    D = {}
    res = ""
    for j in range(N):
        D[j] = bin(Arr[j]).count('1')
    sortD = sorted(D.items(), key=operator.itemgetter(1))
    for a in range(N):
        #print(D[a])
        res += str(Arr[sortD[a][0]]) + " "
        
    print(res)
