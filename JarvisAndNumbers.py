#JARVIS AND NUMBERS

def magic(n,i,r):
    if n<i:
        return r+n
    else:
        q = n//i
        r = r + n%i
        #print(q,r,i)
        return magic(q,i,r)

def gcd(n,i):
    if n%i==0:
        return i
    elif i%n==0:
        return n
    elif n>i:
        return gcd(n%i,i)
    elif i>n:
        return gcd(n,i%n)

for i in range(int(input())):
    n = int(input())
    summ = 0
    rem = 0
    for j in range(2,n,1):
        summ = summ + magic(n,j,rem)
    #print(summ)
    x = n-2
    res = gcd(summ,x)
    while res!=1:
        summ = summ/res
        x = x/res
        res = gcd(summ,x)
    print(int(x))
    
