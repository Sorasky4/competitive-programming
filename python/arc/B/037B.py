from collections import deque

def dfs(gra, visited, x):
    stack = deque()
    stack.append(x)
    visited[x] = 1
    pre = [[0] for _ in range(n+1)]
    ok = True
    while stack:
        p = stack.pop()
        for i in gra[p]:
            if p in pre[i]:
                pass
            elif visited[i] == 0:
                visited[i] = 1
                pre[p].append(i)
                stack.append(i)
            else:
                ok = False
    return ok

n, m = map(int, input().split())
gra = [[] for _ in range(n+1)]
visited = [0]*(n+1)
ans = 0

for i in range(m):
    u, v = map(int, input().split())
    gra[u].append(v)
    gra[v].append(u)

for i in range(1,n+1):
    if visited[i] == 0:
        if dfs(gra, visited, i):
            ans += 1
print(ans)