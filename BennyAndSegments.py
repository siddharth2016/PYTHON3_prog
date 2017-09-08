# BENNY AND SEGMENTS

for _ in range(int(input())):
    n,l = list(map(int, input().split()))
    d = []
    for i in range(n):
        d.append(tuple(map(int, input().split())))
    d.sort(key=lambda x: x[0])
    #print(d)
    for i in range(n):
        maxR = d[i][0] + l
        curR = d[i][1]
        for j in range(i+1,n):
            if(d[j][0]<=curR and d[j][0]>d[i][0] and d[j][1]<=maxR):
                curR = max(curR, d[j][1])
        if(curR==maxR):
            print("Yes")
            break
    else:
        print("No")
        
            
