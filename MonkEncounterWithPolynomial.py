# MONK ENCOUNTER WITH POLYNOMIAL

from math import sqrt

for _ in range(int(input())):
    a,b,c,k = [int(i) for i in input().strip().split()]
    if c>=k:
        print(0)
    else:
        for i in range(int(sqrt(k/a))+1):
            res = a*(i**2) + b*(i) + c
            if res>=k:
                print(i)
                break
