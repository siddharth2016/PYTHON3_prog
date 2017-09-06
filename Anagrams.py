# ANAGRAMS

for _ in range(int(input())):

    A = input()
    B = input()
    C = [0]*26
    D = [0]*26
    for i in (A):
        C[ord(i)-ord('a')] += 1
    for i in B:
        D[ord(i)-ord('a')] += 1
    for i in range(26):
        C[i] = abs(C[i]-D[i])
    print(sum(C))
