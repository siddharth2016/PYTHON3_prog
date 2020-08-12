# ROY AND CODING CONTEST #INCOMPLETE

for _ in range(int(input())):
    n,m = list(map(int, input().split()))
    if n==1:
        print(0)
    elif m==1:
        print(n)
    else:
        countmin = 0
        pd = 0
        mac = 1
        while(pd<m):
            mac += pd
            #print(mac)
            if (mac-pd)<=(m-pd):
                pd += (mac-pd)
            elif (m-pd)<(mac-pd):
                pd += (m-pd)
            else:
                pd += 1
            countmin += 1
            #print(mac,pd,countmin,'###')
            if mac>=n:
                break
        if mac>=n:
            print(countmin)
            #print('#%')
        else:
            q = (n-mac)//m
            rem = (n-mac)%m
            if rem==0:
                print(countmin+q)
                #print('#')
            else:
                print(countmin+q+1)
                #print('##')
