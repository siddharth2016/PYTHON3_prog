# BREAKUP APP       #incomplete

A = [0]*31
for i in range(int(input())):
    s = input().strip()
    for j in range(1,31,1):
        if s[0]=='G':
            A[j] += s.count(str(j))*2
        elif s[0]=='M':
            A[j] += s.count(str(j))
for i in range(10,22,1):
    if i==20:
        continue
    A[1] -= A[i]
for i in range(20,30,1):
    A[2] -= A[i]
A[2] -= A[12]
A[3] -= A[13]-A[22]-A[23]-A[30]
A[4] -= A[14]-A[24]
A[5] -= A[15]-A[25]
A[6] -= A[16]-A[26]
A[7] -= A[17]-A[27]
A[8] -= A[18]-A[28]
A[9] -= A[19]-A[29]
#print(A)
B = {}
for i in range(31):
    if A[i]:
        B[i] = A[i]
#print(B)
mx = max(A)
C = []
for key in B:
    if B[key]==mx:
        C += [(key,B[key])]
#print(C)
if len(C)==1:
    if C[0][0]==19 or C[0][0]==20:
        print("Date")
    else:
        print("No Date")
else:
    print("No Date")
