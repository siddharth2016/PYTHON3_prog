# BUYING EVERYTHING         #INCOMPLETE

n,m,k = list(map(int, input().split()))
Arr = list(map(int, input().split()))
if Arr.count(1)<m:
    print('-1')
elif m==1:
    print(Arr.index(1))
else:
    time = Arr.index(1)
    c = 1
    while c!=m:
        print(time,c)
        i = Arr.index(1)+1
        j = i-1
        while Arr[i]!=1:
            i += 1
        time += abs(j-i)*(c*k)
        c += 1
    print(time)
        
