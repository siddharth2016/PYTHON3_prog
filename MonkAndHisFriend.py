# MONK AND HIS FRIEND

import sys
for i in range(int(input().strip())):
    A = [int(arr) for arr in input().strip().split()]
    xor = bin(A[0]^A[1])
    print(xor.count('1'))
