# SAGAR'S LEARNING

for i in range(int(input())):
    n = int(input())
    n = n//3
    if n<=0:
        print("-1")
    else:
        x = n*2
        y = (3*n)
        print(str(n)+" "+str(x)+" "+str(y))
