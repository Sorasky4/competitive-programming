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
n = int(input())
cost = [[float("inf") for i in range(n)] for i in range(n)]
way = []
for i in range(n-1):
    a, b = map(int,input().split())
    cost[a-1][b-1] = 1
    cost[b-1][a-1] = 1
for i in range(n):
    way.append(dijkstra(i,n,n-1,cost))
q = int(input())
for i in range(q):
    cnt = 0
    x, y = map(int,input().split())
    #x -> y 2の倍数でたどり着けたら可能。その2/1地点で出会う
    cnt = (way[x-1][y-1])
    if cnt % 2 != 0:
        ans = -1
    else:
        for j in range(n):
            if way[x-1][j] == cnt//2:
                if way[j][y-1] == cnt//2:
                    ans = j+1
    print(ans)