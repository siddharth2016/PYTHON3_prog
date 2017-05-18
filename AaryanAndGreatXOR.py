# AARYAN, SUBSEQUENCES AND GREAT XOR

import sys
N = int(input().strip())
x = 1
Arr = [int(arr) for arr in input().strip().split()]
for i in Arr:
    x = x|i
print(x)
