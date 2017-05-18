# ANTON AND POLYHEDRONS

res = 0
for i in range(int(input())):
    s = input().strip()
    if s=='Tetrahedron':
        res += 4
    elif s=='Cube':
        res += 6
    elif s=='Octahedron':
        res += 8
    elif s=='Dodecahedron':
        res += 12
    elif s=='Icosahedron':
        res += 20
print(res)
