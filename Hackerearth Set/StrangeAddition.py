# STRANGE ADDITION

for _ in range(int(input())):
    n1,n2 = [a[::-1] for a in input().strip().split()]
    #print(int(n1),int(n2))
    sm = str(int(n1) + int(n2))[::-1]
    print(int(sm))
    
