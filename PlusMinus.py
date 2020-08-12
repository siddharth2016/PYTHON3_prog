# PLUS MINUS

N = int(input())
Ar = [int(a) for a in input().strip().split()]
countn = countp = countz = 0
for i in Ar:
    if i<0:
        countn += 1
    elif i>0:
        countp += 1
    else:
        countz += 1
resp = countp/N
resn = countn/N
resz = countz/N
print("%.6f" % round(resp, 6))
print("%.6f" % round(resn, 6))
print("%.6f" % round(resz, 6))
