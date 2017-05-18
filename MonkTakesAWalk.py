# MONK TAKES A WALK

for i in range(int(input())):
    s = input().lower()
    count = 0
    for j in s:
        if j=='a' or j=='e' or j=='i' or j=='o' or j=='u':
            count += 1
    print(count)
