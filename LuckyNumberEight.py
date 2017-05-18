#!/bin/python3

import sys


n = int(input().strip())
number = input().strip()
# your code goes here
count = 0
#number = str(int(number)%10000000007)
number = " ".join(number)
number = number.split()
for i in range(0,n,1):
    ai = number[i]
    if int(ai)%8==0:
        count = (count + 1)%1000000007
    for j in range(i+1,n,1):
        aj = number[i] + number[j]
        if int(aj)%8==0:
            count = (count + 1)%1000000007
        ak = aj
        '''ak = ak + number[j+1]
        if int(ak)%8==0:
            count+=1'''
        for k in range(j+1,n,1):
            ak = ak + number[k]
            if int(ak)%8==0:
                count = (count + 1)%1000000007
            for l in range(k+1,n,1):
                al = ak + number[l]
                if int(al)%8==0:
                    count = (count + 1)%1000000007
print(count)
