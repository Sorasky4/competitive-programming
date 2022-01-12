from collections import deque

def bfs():
    dist = [[float('inf') for j in range(m)] for i in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(n):
        for j in range(m):
            if maze[i][j] == 's':
                sx = i
                sy = j
            if maze[i][j] == 'g':
                gx = i
                gy = j
    que = deque([])
    que.append((sx, sy))
    dist[sx][sy] = 0

    while que:
        top = que.popleft()
        if top[0] == gx and top[1] == gy:
            break
        for i in range(4):
            nx = top[0] + dx[i]
            ny = top[1] + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != '#' and dist[nx][ny] == float('inf'):
                que.append((nx,ny))
                dist[nx][ny] = dist[top[0]][top[1]] + 1
    if dist[gx][gy] == float('inf'):
        return 'Fail'
    return dist[gx][gy]

m, n = map(int, input().split())
maze = [list(map(str, input().split())) for _ in range(n)]

print(bfs())