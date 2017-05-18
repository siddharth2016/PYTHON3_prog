# RECURSIVE SUMS

def sumdigit(num,al):
    summ = 0
    if al==1:
        return num
    else:
        for i in range(0,al,1):
            a = int(num[i])
            summ = summ + a
        summ = str(summ)
        summl = len(summ)
        return sumdigit(summ,summl)

test = int(input())
for i in range(0,test,1):
    num = ""
    M = int(input())
    for j in range(0,M,1):
        arr = str(input())
        arr = arr.split()
        len1 = int(arr[0])
        d = arr[1]
        num = num + len1*d
    al = len(num)
    a = sumdigit(num,al)
    print(a)
