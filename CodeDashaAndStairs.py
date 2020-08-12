# CODEFORCES DASHA AND STAIRS

import sys
A = [int(a) for a in input().strip().split()]
if A[0]==0 and A[1]==0:
    print("NO")
elif (abs(A[1]-A[0])==0) or (abs(A[1]-A[0])==1):
    print("YES")
else:
    print("NO")
