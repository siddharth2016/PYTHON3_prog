# ANTON AND CLASSES

A = []
B = []
M = [0]
for i in range(int(input())):
    A += [tuple(map(int, input().strip().split()))]
for i in range(int(input())):
    B += [tuple(map(int, input().strip().split()))]
#print(A,B)
for j in A:
    #print(j[0])
    for i in B:
        if j[0]>i[1] or i[0]>j[1]:
            M += [j[0]-i[1]] + [i[0]-j[1]]
if max(M)<=0:
    print(0)
else:
    print(max(M))
