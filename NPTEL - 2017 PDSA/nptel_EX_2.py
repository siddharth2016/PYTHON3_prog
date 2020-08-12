# Perfect

from math import sqrt

def perfect(n):
    sm = 0
    for i in range(1,(n//2)+1,1):
        if n%i==0:
            sm += i
    if sm==n:
        return(True)
    else:
        return(False)

# depth

def depth(st):
    mx = 0
    cto = 0
    ctc = 0
    for i in st:
        if i=='(':
            cto += 1
        elif i==')':
            ctc += 1
            if ctc==cto:
                if mx<cto:
                    mx = cto
                cto = ctc = 0
    return(mx)

# sumsquares

def sumsquares(lt):
    sm = 0
    for i in lt:
        if int(sqrt(i)+0.5)**2 == i:
            sm += i
    return(sm)
