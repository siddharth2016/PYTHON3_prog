# THE CASTLE GATE
test = int(input())
for i in range(0,test,1):
    N = int(input())
    count = 0
    for j in range(1,N+1,1):
        for k  in range(j+1,N+1,1):
            x = j^k;
            if not(x>N):
                count = count + 1
    print(count)
