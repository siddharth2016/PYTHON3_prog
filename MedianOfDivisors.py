# MEDIAN OF DIVISORS

from sys import stdin, stdout

def factors(n):
    return list(x for tup in ([i, n//i] 
                for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)

def qsort(inlist):
    if inlist == []: 
        return []
    else:
        pivot = inlist[0]
        lesser = qsort([x for x in inlist[1:] if x < pivot])
        greater = qsort([x for x in inlist[1:] if x >= pivot])
        return lesser + [pivot] + greater
    
for i in range(int(stdin.readline())):
    A = [int(a) for a in stdin.readline().split()]
    N = len(A)
    p = 1
    for j in A:
        p *= j
    div = qsort(factors(p))
    #print(div)
    num = len(div)
    if num%2==0:
        nume = div[num//2]+div[(num//2)-1]
        if nume%2!=0:
            stdout.write(str(nume)+"/"+str(2)+"\n")
        else:
            stdout.write(str(nume//2)+"/"+str(1)+"\n")
    else:
        nume = div[num//2]
        stdout.write(str(nume)+"/"+str(1)+"\n")
