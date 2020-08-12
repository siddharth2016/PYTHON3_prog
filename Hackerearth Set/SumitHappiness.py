# SUMIT HAPPINESS       

for _ in range(int(input())):
    n = int(input())
    Arr = list(map(int, input().split()))
    Arr.sort()
    countPositive = sumPositive = sumNeg = 0
    for i in range(n-1,-1,-1):
        if Arr[i]<=0:
            break
        countPositive+=1
        sumPositive+=Arr[i]
    for j in range(i,-1,-1):
        sumNeg+=Arr[j]
    res = sumPositive*countPositive + sumNeg
    #print(res)
    if i == n-1:
        print(res)
    else:
        for j in range(i, -1, -1):

            sumPositive+=Arr[j]
            sumNeg-=Arr[j]
            countPositive+=1

            tempres = countPositive*sumPositive + sumNeg
            res = max(res, tempres)
        print(res)
