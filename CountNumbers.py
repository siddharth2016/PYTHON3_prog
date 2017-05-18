# COUNT NUMBERS

for i in range(int(input())):
    N = int(input())
    s = str(input())
    count = 0
    j = 0
    while j<(N):
        if '0'<=s[j]<='9':
            count += 1
            while '0'<=s[j]<='9':
                j += 1
        else:
            j += 1
    print(count)
