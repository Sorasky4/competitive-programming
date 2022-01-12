def warshall_floyd(c, d):
    for i in range(10):
        for j in range(10):
            for k in range(10):
                c[j][k] = min(c[j][k],c[j][i] + c[i][k])
                if k == 1:
                    d[j] = c[j][k]
    return d

h, w = map(int, input().split())
c = [[int(i) for i in input().split()] for j in range(10)]
a = [[int(i) for i in input().split()] for j in range(h)]
dist = [0] * 10
ans = 0
warshall_floyd(c, dist)

for i in range(h):
    for j in range(w):
        if a[i][j] != -1:
            ans += dist[a[i][j]]

print(ans)