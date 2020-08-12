# ALEX AND PRIORITY REQUESTS

import operator
d = {}
for _ in range(int(input())):
    q = [int(a) for a in input().split()]
    if q[0]==1:
        d[q[1]] = q[2]
    elif q[0]==2:
        d.pop(q[1],None)
    elif q[0]==3:
        dd = sorted(d.items(), key=operator.itemgetter(1))
        print(dd[0][1],dd[len(dd)-1][1])
    elif q[0]==4:
        dd = sorted(d.items(), key=operator.itemgetter(0))
        print(dd[len(dd)-1][1])
