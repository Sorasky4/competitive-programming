n, u, v = map(int,input().split())
graph = [[0 for i in range(n)] for i in range(n)]
for i in range(n-1):
    a, b = map(int,input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1
u -= 1
v -= 1
print(graph)