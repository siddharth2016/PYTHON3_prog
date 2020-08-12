# BENNY AND SUMS
sn = str(input())
sn = sn.split()
n = int(sn[0])
m = int(sn[1])
sn = str(input())
sn = sn.split()
for i in range(m):
    s = str(input())
    s = s.split()
    l = int(s[0])
    r = int(s[1])
    x = int(s[2])
    summ = 0
    for j in range(l-1,r,1):
        if int(sn[j])%x==0:
               continue
        summ = summ + (int(sn[j])%x)
    print(summ)
