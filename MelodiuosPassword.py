# MELODIUOS PASSWORD
from sys import stdin,stdout
cons = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
vow = ['a','e','i','o','u']
n = int(input())
if n==1:
    for a in cons:
        print(a)
    for a in vow:
        print(a)
elif n==2:
    i=j=0
    while i<20:
        A = ['']*n
        for j in range(0,n,2):
            A[j] = cons[i]
        for a in vow:
            for j in range(1,n,2):
                A[j] = a
            stdout.write(''.join(A)+"\n")
        i += 1
    i = 0
    while i<5:
        A = ['']*n
        for j in range(0,n,2):
            A[j] = vow[i]
        for a in cons:
            for j in range(1,n,2):
                A[j] = a
            stdout.write(''.join(A)+"\n")
        i += 1
elif n==3:
    i=j=k=0
    A = ['']*n
    for i in cons:
        A[j] = i
        for a in vow:
            A[j+1] = a
            for b in cons:
                A[j+2] = b
                stdout.write(''.join(A)+"\n")

    for i in vow:
        A[j] = i
        for a in cons:
            A[j+1] = a
            for b in vow:
                A[j+2] = b
                stdout.write(''.join(A)+"\n")
elif n==4:
    i=j=k=0
    A = ['']*n
    for i in cons:
        A[j] = i
        for a in vow:
            A[j+1] = a
            for b in cons:
                A[j+2] = b
                for c in vow:
                    A[j+3] = c
                    stdout.write(''.join(A)+"\n")

    for i in vow:
        A[j] = i
        for a in cons:
            A[j+1] = a
            for b in vow:
                A[j+2] = b
                for c in cons:
                    A[j+3] = c
                    stdout.write(''.join(A)+"\n")

    
elif n==5:
    i=j=0
    #count = 0
    A = ['']*n
    for i in cons:
        A[j] = i
        for a in vow:
            A[j+1] = a
            for b in cons:
                A[j+2] = a
                for c in vow:
                    A[j+3] = c
                    for d in cons:
                        A[j+4] = d
                        stdout.write(''.join(A)+"\n")
                        #count += 1

    for i in vow:
        A[j] = i
        for a in cons:
            A[j+1] = a
            for b in vow:
                A[j+2] = a
                for c in cons:
                    A[j+3] = c
                    for d in vow:
                        A[j+4] = d
                        stdout.write(''.join(A)+"\n")
                        #count += 1
    #print(count)
                        
elif n==6:
    i=j=0
    A = ['']*n
    for i in cons:
        A[j] = i
        for a in vow:
            A[j+1] = a
            for b in cons:
                A[j+2] = b
                for c in vow:
                    A[j+3] = c
                    for d in cons:
                        A[j+4] = d
                        for e in vow:
                            A[j+5] = e
                            stdout.write(''.join(A)+"\n")

    for i in vow:
        A[j] = i
        for a in cons:
            A[j+1] = a
            for b in vow:
                A[j+2] = b
                for c in cons:
                    A[j+3] = c
                    for d in vow:
                        A[j+4] = d
                        for e in cons:
                            A[j+5] = e
                            stdout.write(''.join(A)+"\n")
                        
