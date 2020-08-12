# ALEX AND REQUEST

n=int(input())+1
system = [0 for a in range(n)]
for _ in range(int(input())):
    x = int(input())
    f = 0
    for i in range(n-1,0,-1):
        if system[i]<x and x>=i:
            system[i]=x
            f = 1
            print("YES")
            #print(system)
            break
        else:
            f = 0
    if not f:
        print("NO")
