# MODIFY SEQUENCE

n = int(input())
An = [int(a) for a in input().split()]
res = 0
for i in range(n):
    res += An[i]*pow(10,i)
if res%11==0:
    print("YES")
else:
    print("NO")
