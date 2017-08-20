# PLAY WITH NUMBERS

from sys import stdin,stdout
n,q = list(map(int, stdin.readline().split()))
Arr = [int(a) for a in stdin.readline().split()]
sumArr = [0]
s = 0
for i in range(n):
    s += Arr[i]
    sumArr.append(s)
#print(sumArr)
res = 0
for _ in range(q):
    l,r = list(map(int, input().split()))
    l = l-1
    res = (sumArr[r]-sumArr[l])//(r-l)
    stdout.write(str(res)+"\n")
