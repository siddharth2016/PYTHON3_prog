# THE BEST PLAYER

n,t = list(map(int, input().split()))
d = {}
f = []
for _ in range(n):
    name,qt = input().split()
    try:
        d[int(qt)].append(name)
    except:
        d[int(qt)] = [name]
    f.append(int(qt))
f.sort(reverse = True)

for i in range(t):
    d[f[i]].sort()
    print(d[f[i]][0])
    d[f[i]].pop(0)
