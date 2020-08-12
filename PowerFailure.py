#POWER FAILURE
prime = [0]*100001
for i in range(2,100001,1):
    for j in range(i,100001,i):
        prime[j] = prime[j] + 1
#print(prime[98])

test = int(input())
for i in range(test):
    nm = str(input())
    nm = nm.split()
    n = int(nm[0])
    m = int(nm[1])
    sn = str(input())
    sn = sn.split()
    for j in range(n):
        sn[j] = int(sn[j])
    sn.sort(reverse=True)
    availBattery = 0
    for j in range(sn[0],m+1,1):
        if prime[j]!=1:
            availBattery += 1
    #print(availBattery)
    combination = availBattery
    #print(combination)
    
    for j in range(1,n,1):
        availBattery1 = 0
        for k in range(sn[j],sn[j-1],1):
            if prime[k]!=1:
                availBattery1 += 1
        
        availBattery1 += availBattery - 1
        #print(availBattery1)
        combination = (combination*availBattery1)%1000000007
        #print(combination)
        #print(availBattery,availBattery1)
        availBattery = availBattery1
        #print(availBattery)
        
    print(combination)

