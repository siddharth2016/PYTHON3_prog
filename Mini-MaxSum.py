# MINI-MAX SUM

Ar = [int(a) for a in input().strip().split()]
Ar.sort()
res = ''
res += str(sum(Ar[0:4])) + " " + str(sum(Ar[1:]))
print(res)
