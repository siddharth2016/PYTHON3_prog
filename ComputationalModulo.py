# COMPUTATIONAL MODULO

a,b,c,m = [int(a) for a in input().split()]
def cal(x,y):
    if y==0:
        return 1
    elif y%2==0:
        return cal(x*x,y/2)
    else:
        return x*cal(x*x,(y-1)/2)
r = cal(a,b)
print(r)
