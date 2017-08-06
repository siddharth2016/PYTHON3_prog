# TOWERS OF HANOI PROBLEM

n = int(input("Number of Disks: "))

def toh(n,A,B,C):
    if n==1:
        print("Move disk 1 from",A,"to",C)
        return
    toh(n-1,A,C,B)
    print("Move disk",n,"from",A,"to",C)
    toh(n-1,B,A,C)

toh(n,'A','B','C')
