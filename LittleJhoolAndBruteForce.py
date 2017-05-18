#LITTLE JHOOL AND BRUTE FORCE

test = int(input())
for l in range(0,test,1):
    ans = []
    count=1
    num = int(input())
    cnum = int(num**(1/3))
    for i in range(1,cnum+1,1):
        ci = i**3
        for j in range(i,cnum+1,1):
            cj = j**3
            cn = ci + cj
            if cn<num:
                ans = ans + [cn]
                
    ans.sort()
    for i in range(len(ans)-1,-1,-1):
        n = ans[i]
        count = 1
        for j in range(i-1,-1,-1):
            x = ans[j]
            if n==x:
                count = count + 1
        if count>1:
            print(n,"\n")
            flag = 0
            break
        else:
            flag = 1
    if flag:
        print("-1")
