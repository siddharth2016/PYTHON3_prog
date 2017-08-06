# BE THE JODI MAKER

for _ in range(int(input())):
    d = {}
    for i in range(int(input())):
        A = [a for a in input().split()]
        d[A[0]] = A[1]
        if i==0:
            s = A[0]
    #print(d)
    n = i+1
    ct = 0
    s1 = s
    f = 1
    #print(s1,s,n)
    while ct<n:
        if s not in d:
            f = 0
            break
        s = d[s]
        ct += 1
        if s==s1 and ct<n:
            f = 0
            break
    if s==s1 and f and n>2:
        print("YES")
        print()
    else:
        ct = 0
        for key in d:
            if d[key] in d:
                if key==d[d[key]]:
                    d[d[key]] = '0'
                    ct += 1
        print("NO")
        print(ct)
        print()
