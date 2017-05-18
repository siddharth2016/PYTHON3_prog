# MATTEY MULTIPLICATION

for i in range(int(input().strip())):
    n,m = [int(a) for a in input().strip().split()]
    prod = n*m
    exp = ""
    s = 0
    for j in range(55,-1,-1):
        x = n<<j
        if x<=prod:
            if x==prod:
                exp += '('+str(n)+'<<'+str(j)+')'
                print(exp)
                break
            else:
                s += x
                if s<=prod:
                    exp += '('+str(n)+'<<'+str(j)+')'+' + '
                    if s==prod:
                        print(exp[:len(exp)-3])
                        break
                elif s>prod:
                    s -= x
                
