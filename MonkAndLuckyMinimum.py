# MONK AND LUCKY MINIMUM

for _ in range(int(input())):
    n = input()
    Arr = list(map(int, input().split()))
    if Arr.count(min(Arr))%2==1:
        print("Lucky")
    else:
        print("Unlucky")
