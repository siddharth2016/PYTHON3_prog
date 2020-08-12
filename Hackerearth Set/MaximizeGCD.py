# MAXIMISE GCD

def gcd(a,b):
    if a%b==0:
        return(b)
    if b%a==0:
        return(a)
    if a==b:
        return(a)
    if a>b:
        return gcd(a%b,b)
    if b>a:
        return gcd(a,b%a)


n = int(input())
Arr = list(map(int, input().strip().split()))
x = Arr[n-1]
mx = 1
j = 0
for i in range(n-1,-1,-1):
    G = gcd(x,Arr[i])
    #print(G)
    if mx<=G:
        mx = G
        j = i
    x = G
print(j)
