# MIXING STRING

def mixString(A,n):
    if len(A)==1:
        return A
    else:
        B = []
        maxi = 0
        ii=jj=0
        for i in range(n):
            ss = A[i]
            for j in range(n):
                if j!=i:
                    ss1 = A[j]
                    for k in range(len(ss)):
                        ssi = k
                        ssli = 0
                        while ssi<len(ss) and ss1[ssli]==ss[ssi]:
                            ssli = ssli + 1
                            ssi = k + ssli
                            if ssli>=len(ss1):
                                break
                        if ssi == len(ss):
                            break
                    if ssli>maxi:
                        maxi = ssli
                        jj = j
                        ii = i
            #print(maxi,ii,jj)
        if ii==jj==0:
            A[ii] = A[ii] + A[1]
            for i in range(n):
                if i!=1:
                    B = B + [A[i]]
        else:
            A[ii] = A[ii] + A[jj][maxi:]
            for i in range(n):
                if i!=jj:
                    B = B + [A[i]]
        return mixString(B,len(B))
        

N = int(input())
A = []
for ni in range(N):
    ss = str(input())
    A = A + [ss]
x = mixString(A,len(A))
print(len(x[0]))
