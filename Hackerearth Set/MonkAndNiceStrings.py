# MONK AND NICE STRINGS

Arr = []
n = int(input())
for _ in range(n):
    Arr.append(input())
ct = []
for i in range(n-1,-1,-1):
    count = 0
    st1 = Arr[i]
    for j in range(i-1,-1,-1):
        if st1>Arr[j]:
            count += 1
    ct.append(count)
for i in range(n-1,-1,-1):
    print(ct[i])
