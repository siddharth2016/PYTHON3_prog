#COMPARE THE TRIPLETS

a1,a2,a3 = [int(a) for a in input().strip().split()]
b1,b2,b3 = [int(b) for b in input().strip().split()]
counta=countb=0
if a1>b1:
    counta += 1
elif a1<b1:
    countb += 1
if a2>b2:
    counta += 1
elif a2<b2:
    countb += 1
if a3>b3:
    counta += 1
elif a3<b3:
    countb += 1
print(str(counta) + " " + str(countb))
