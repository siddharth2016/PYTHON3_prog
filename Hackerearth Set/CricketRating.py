#CRICKET RATING

N = int(input())
rate = str(input())
rate = rate.split()
lenr = len(rate)
maxx = 0
for i in range(0,lenr,1):
    x = int(rate[i])
    summ = x
    for j in range(i+1,lenr,1):
        y = int(rate[j])
        summ = summ + y
        if summ>maxx:
            maxx = summ
print(maxx)
