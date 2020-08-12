#MEMORISE ME!

B = [0]*1001
N = int(input())
Arr = [int(a) for a in input().strip().split()]
for i in range(int(input())):
    x = int(input())
    if B[x]:
        print(B[x])
    else:
        y = Arr.count(x)
        if y>0:
            print(y)
            B[x] = y
        else:
            print("NOT PRESENT")
