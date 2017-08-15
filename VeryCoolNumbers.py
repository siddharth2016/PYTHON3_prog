# VERY COOL NUMBERS  #INCOMPLETE

import re
for _ in range(int(input())):
    r,k = list(map(int,input().split()))
    ct = 0
    for i in range(5,r+1,1):
        bn = bin(i)[2:]
        if len(re.findall('(?=101)', bn))>=k:
            ct += 1
    print(ct)
