#DORSPLEN

import sys
Arr = [int(a) for a in input().strip().split()]
Arr.sort()
r = Arr[0]
g = Arr[1]
b = Arr[2]
count = 0
count += r
g -= r
b -= r
if g==0 and b==0:
    print(count)
else:
    if g%2==0 and b%2==0:
        count += (g//2) + (b//2)
        g = b = 0
        print(count)
    elif g%2==0:
        count += (g//2)
        count += (b//2)+(b%2)
        print(count)
    elif b%2==0:
        count += (b//2)+(g//2)+(g%2)
        print(count)
    else:
        x = min(g,b)
        count += x
        y = max(g,b)
        y -= x
        count += (y//2)+(y%2)
        print(count)
        
