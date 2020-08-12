# SUM OF NUMBERS

for i in range(int(input().strip())):
    n = int(input().strip())
    arr = [int(a) for a in input().strip().split()]
    s = int(input().strip())
    for j in range(0,2**n,1):
        x = 0
        for k in range(0,n,1):
            if (j & (1<<k)):
                x += arr[k]
        if x==s:
            print("YES")
            break
    if j==2**n:
        print("NO")
