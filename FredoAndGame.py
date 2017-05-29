#FREDO AND GAME

for i in range(int(input())):
    f = 1
    a,n = [int(x) for x in input().strip().split()]
    arr = [int(x) for x in input().strip().split()]
    for j in range(n):
        if a==0:
            f = 0
            break
        if arr[j]==0:
            a = a - 1
        elif arr[j]==1:
            a = a + 3 - 1
    if not f:
        print("No " + str(j))
    else:
        print("Yes " + str(a))
