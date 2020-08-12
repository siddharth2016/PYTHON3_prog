# UGLY OR BEAUTIFUL

for _ in range(int(input())):
    n = int(input())
    Arr = list(map(int, input().split()))
    B = Arr[:]
    cmp = list(range(1,n+1,1))
    Arr.sort()
    if Arr==B:
        print("Ugly")
    else:
        if cmp!=Arr:
            print("Ugly")
        else:
            print("Beautiful")
