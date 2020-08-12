# STUDENTS LOVE STUDYING

for _ in range(int(input())):
    n,m,k = list(map(int, input().split()))
    A = []
    B = []
    ans = []
    j = 0
    for i in range(n):
        A.append(list(map(int, input().split())))
    for i in range(m):
        B.append(list(map(int, input().split())))
    #print(A,B)
    for i in range(n):
        C = []
        for j in range(k):
            res = 0
            for a in range(m):
                res += A[i][a]*B[a][j]
            C.append(str(res))

        ans.append(C)
    #print(ans)
    for q in ans:
        print(" ".join(q))
            
