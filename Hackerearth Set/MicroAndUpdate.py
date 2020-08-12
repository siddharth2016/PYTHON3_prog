# MICRO AND UPDATE

for i in range(int(input().strip())):
    n,k = [int(a) for a in input().strip().split()]
    Arr = [int(a) for a in input().strip().split()]
    Arr.sort()
    x = k - Arr[0]
    #print(x)
    if x<=0:
        print('0')
    else:
        print(x)
