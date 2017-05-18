# WAR
test = int(input())
for i in range(0,test,1):
    n = int(input())
    a = str(input())
    a = a.split()
    b = str(input())
    b = b.split()
    Bob = []
    Alice = []
    for j in range(0,n,1):
        Bob = Bob + [int(a[j])]
        Alice = Alice + [int(b[j])]
    maxb = max(Bob)
    maxa = max(Alice)
    if(maxa>maxb):
        print("Alice")
    elif(maxb>maxa):
        print("Bob")
    else:
        print("Tie")
