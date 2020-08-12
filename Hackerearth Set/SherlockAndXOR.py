# SHERLOCK AND XOR
test = int(input())
for i in range(test):
    countOdd = 0
    countEven = 0
    n = int(input())
    A = str(input())
    A = A.split()
    for j in range(n):
        x = int(A[j])
        if x%2==0:
            countEven += 1
        else:
            countOdd += 1
    print(countOdd*countEven)
