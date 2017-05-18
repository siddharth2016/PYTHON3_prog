#THE GREAT KIAN

n = int(input())   #Taking total numbers
ans = []
a = str(input())
num = a.split()    
num += [0]+[0]+[0]

for i in range(0,3,1):
    x = int(num[i])
    summ = 0
    j=i
    while num[j]!=0:
        summ = summ + int(num[j])
        j = j + 3
    ans += [str(summ)]

anss = ' '.join(ans)
print(anss)
