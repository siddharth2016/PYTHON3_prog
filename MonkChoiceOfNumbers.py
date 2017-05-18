# MONK'S CHOICE OF NUMBERS

import sys
for i in range(int(input().strip())):
    nk = [int(a) for a in input().strip().split()]
    Arr = [int(a) for a in input().strip().split()]
    binArr = [bin(a).count('1') for a in Arr]
    binArr.sort(reverse = True)
    print(sum(binArr[0:nk[1]]))
