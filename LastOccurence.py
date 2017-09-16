# LAST OCCURENCE

for _ in range(int(input())):

    n = int(input())
    Arr = list(map(int, input().split()))
    query = []
    for q in range(int(input())):
        query.append(int(input()))

    d = {}
    for i in range(n):
        d[Arr[i]] = i+1
    for q in query:
        try:
            print(d[q])
        except:
            print(-1)
