# COUNTING TRIANGLES

Ar = []
count = 0
for _ in range(int(input())):
    A = [int(a) for a in input().strip().split()]
    A.sort()
    A = [str(a) for a in A]
    Ar += [''.join(A)]
#print(Ar)
for i in Ar:
    if Ar.count(i)>1:
        while Ar.count(i):
            Ar.remove(i)
    #print(Ar)
print(len(Ar))
