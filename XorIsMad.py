# XOR IS MAD
for i in range(int(input())):
    N = int(input())
    binNo = '{0:b}'.format(N)
    for j in range(len(binNo)):
        if binNo[j]=='1':
            break
    numZero = binNo[j:].count('0')
    ans = 2**numZero - 1
    print(ans)
