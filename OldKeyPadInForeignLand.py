# OLD KEYPAD IN A FOREIGN ISLAND

n = int(input())
Arr = list(map(int, input().split()))
k = int(input())
Key = list(map(int, input().split()))
if n>sum(Key):
    print('-1')
else:
    A = [0]*k
    i = j = 0
    res = 0
    Arr.sort(reverse = True)
    Key.sort()
    for i in Arr:
        #print(A)
        for j in range(k):
            if Key[j]==A[j]:
                continue
            if j==k-1:
                A[j] += 1
                res += i*A[j]
                break
            if A[j]>A[j+1]:
                continue
            if A[j]==A[j+1] and j+1==k-1:
                A[j] += 1
                res += i*A[j]
                break
            if A[j]==A[j+1] and j+1!=k-1 and A[j]!=0:
                continue
            A[j] += 1
            res += i*A[j]
            break
    print(res)
            
