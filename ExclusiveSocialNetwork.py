# EXCLUSIVE SOCIAL NETWORKS

graph = []
n = int(input())

for _ in range(n):
    graph.append(list(input().split('-')))
#print(graph)

result = []
#print(result)
count = 0

while graph.count(0)!=n:
    for i in range(n):
        if graph[i]!=0 and (graph[i][0] not in result) and (graph[i][1] not in result):
            count += 1
            result.append(graph[i][0])
            result.append(graph[i][1])
            graph[i] = 0
        elif graph[i]==0:
            continue
        for k in range(3):
            for j in range(i+1,n,1):
                if graph[j]!=0 and ((graph[j][0] in result) or (graph[j][1] in result)):
                    result.append(graph[j][0])
                    result.append(graph[j][1])
                    graph[j] = 0
print(count)
