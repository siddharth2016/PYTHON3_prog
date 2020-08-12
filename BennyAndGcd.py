# BENNY AND GCD

def gcd(x,y):
    if x%y==0:
        return y
    elif y%x==0:
        return x
    elif x<y:
        return gcd(x,y%x)
    elif y<x:
        return gcd(x%y,y)

S = str(input())
S = S.split()
l = int(S[0])
r = int(S[1])
g = int(S[2])
count = 0
for i in range(g,r+1,g):
    for j in range(g,r+1,g):
        count += 1
        if i!=g and j!=g:
            if gcd(i,j)!=g:
                count -= 1
print(count)
