# AISH AND XOR

N = int(input().strip())
Arr = [0] + [int(a) for a in input().strip().split()]
for i in range(int(input())):
    q = [int(a) for a in input().strip().split()]
    l = q[0]
    r = q[1]
    subArr = Arr[l:r+1]
    subArr1 = subArr.count(1)
    subArr0 = subArr.count(0)
    ans = ""
    if (subArr1)%2==0:
        ans += '0 ' + str(subArr0)
        print(ans)
    else:
        ans += '1 ' + str(subArr0)
        print(ans)
    
