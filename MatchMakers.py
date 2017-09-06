# MATCH MAKERS

for _ in range(int(input())):
    n = int(input())
    Girls = list(map(int, input().split()))
    Boys = list(map(int, input().split()))
    Girls.sort()
    Boys.sort(reverse = True)
    count = 0
    for i in range(n):
        if Girls[i]%Boys[i]==0 or Boys[i]%Girls[i]==0:
            count += 1
    print(count)
