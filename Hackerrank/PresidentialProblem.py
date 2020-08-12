#Presidential problem

for i in range(int(input())):
    n,q = [int(a) for a in input().strip().split()]
    s = [a for a in input().strip()]
    #print(s)
    for j in range(q):
        l,r = [int(a) for a in input().strip().split()]
        for k in range(l-1,r,1):
            if s[k]=='a':
                s[k]='z'
            else:
                #print(s[k])
                asc = ord(s[k]) - 1
                s[k] = chr(asc)
    print("".join(s))
