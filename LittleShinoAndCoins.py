# LITTLE SHINO AND COINS

k = int(input())
s = str(input())
counti = 0
for i in range(0,len(s)-k+1,1):
    counta = 0
    ch=""
    for j in range(i,len(s),1):
        a = s[j]
        if counta == k and len(ch)==k:
            counti = counti + 1
        if ch.count(a)>=1 and counta==k:
            counti = counti + 1
            ch = ch + a
        elif ch.count(a)==0 and counta==k:
            counta = 0
            break
        elif ch.count(a)==0 and counta!=k:
            counta = counta + 1
            ch = ch + a
    if counta==k and len(ch)==k:
        counti = counti + 1
print(counti)
