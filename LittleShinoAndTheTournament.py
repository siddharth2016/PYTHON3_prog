# LITTLE SHINO AND THE TOURNAMENT

n,q = list(map(int, input().split()))
Arr = list(map(int, input().split()))
P = Arr[:]
res = {}
query = []
for i in range(q):
    query.append(int(input()) - 1)
    res[P[query[i]]] = 0
while len(Arr)>1:
    for i in range(0,len(Arr)//2):
        if Arr[i] in res:
            res[Arr[i]] += 1
        if Arr[i+1] in res:
            res[Arr[i+1]] += 1
        if Arr[i]>Arr[i+1]:
            Arr.pop(i+1)
        else:
            Arr.pop(i)
#print(res)
for i in query:
    print(res[P[i]])
