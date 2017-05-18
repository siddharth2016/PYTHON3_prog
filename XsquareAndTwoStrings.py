# XSQUARE AND TWO STRINGS

import sys
summ = 0
for i in range(int(input().strip())):
    s1 = input().strip()
    s2 = input().strip()
    summ += len(s1) + len(s2)
    flag = 0
    if summ<=(5*(10**5)):
        for j in range(len(s1)):
            if s2.count(s1[j])>=1:
                flag = 1
                print("Yes")
                break
        if flag!=1:
            print("No")
