# BRUCE'S BATARANGS

S = input().strip()
countD = countU = i = 0
while i<(len(S)):

    if S[i]=='U':
        countU += 1
        while i<len(S) and S[i]=='U':
            i += 1

    if i<len(S) and S[i]=='D':
        countD += 1
        while i<len(S) and S[i]=='D':
            i += 1

print(min(countD, countU))
