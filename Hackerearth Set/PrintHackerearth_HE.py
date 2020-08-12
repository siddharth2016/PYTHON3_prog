# PRINT HACKEREARTH

n = int(input())
strr = str(input())
counth = 0
counta = 0
countc = 0
countk = 0
counte = 0
countr = 0
countt = 0
for i in range(0,n,1):
    if strr[i] == 'h':
        counth+=1
    elif strr[i] == 'a':
        counta += 1
    elif strr[i] == 'c':
        countc += 1
    elif strr[i] == 'k':
        countk += 1
    elif strr[i] == 'e':
        counte += 1
    elif strr[i] == 'r':
        countr += 1
    elif strr[i] == 't':
        countt += 1

ans = []
xh = counth//2
ans += [xh]
xa = counta//2
ans += [xa]
xc = countc//1
ans += [xc]
xk = countk//1
ans += [xk]
xe = counte//2
ans += [xe]
xr = countr//2
ans += [xr]
xt = countt//1
ans += [xt]

print(min(ans))
