# INVERSE LIST

for _ in range(int(input())):
    n = int(input())
    Arr = [int(a) for a in input().strip().split()]
    res = [1]*n
    for i in range(n):
        res[Arr[Arr[i]-1]-1] = Arr[i]
    #print(res,Arr)
    if Arr==res:
        print("inverse")
    else:
        print("not inverse")
    
