def dijkstra(s,n,w,cost):
    d = [float("inf")] * n
    used = [False] * n
    d[s] = 0
    while True:
        v = -1
        for i in range(n):
            if (not used[i]) and (v == -1):
               v = i
            elif (not used[i]) and d[i] < d[v]:
                v = i
        if v == -1:
               break
        used[v] = True
               
        for j in range(n):
               d[j] = min(d[j],d[v]+cost[v][j])
    return d

n, m = map(int,input().split())
a = []
b = []
for i in range(m):
    aa, bb = map(int,input().split())
    a.append(aa)
    b.append(bb)
d = [int(i) for i in input().split()]
gra = [[float("inf") for i in range(n)] for i in range(n)]
for i in range(m):
    if d[a[i]-1] != d[b[i]-1]:
        gra[a[i]-1][b[i]-1] = 1
        gra[b[i]-1][a[i]-1] = 1
ans = 0
for i in range(n):
    for j in range(n):
        if dijkstra(i,n,m,gra)[j] == float("inf"):
            ans += 1
print(ans)