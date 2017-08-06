# REMOVE FRIENDS

for _ in range(int(input())):
    n,k = list(map(int, input().split()))
    Arr = list(map(int, input().split()))
    for i in range(k):
        f = 0
        for j in range(len(Arr)-1):
            if Arr[j]<Arr[j+1]:
                del Arr[j]
                f = 1
                break
        if not f:
            del Arr[-1]
    ans = list(map(str, Arr))
    print(' '.join(ans))
