# MIN-MAX HACKER EARTH

n = int(input())
arr = str(input())
arr = arr.split()
arr1 = []
for i in range(0,n,1):
    x = int(arr[i])
    arr1 += [x]
min_arr = min(arr1)
max_arr = max(arr1)

count = 0
for i in range(min_arr+1,max_arr,1):
    num = i
    for j in range(0,n,1):
        if num == arr1[j]:
            count = count + 1
            break

diff = max_arr - min_arr - 1

if count == diff:
    print("YES")
else:
    print("NO")
