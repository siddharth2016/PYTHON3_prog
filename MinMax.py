# MIN MAX

n = int(input())
Arr = [int(a) for a in input().split()]
Arr.sort()
print(sum(Arr[0:n-1]), sum(Arr[1:]))
