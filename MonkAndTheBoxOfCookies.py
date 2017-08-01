# MONK AND THE BOX OF COOKIES

for _ in range(int(input())):
    A = [0]*32
    for q in range(int(input())):
        n = bin(int(input()))[2:]
        i = len(n)-1
        j = 0
        while i>=0:
            if n[i]=='1':
                A[j] += 1
            j += 1
            i -= 1
        #print(A)
    mx = max(A)
    for i in range(32):
        if A[i]==mx:
            break
    print(i)
