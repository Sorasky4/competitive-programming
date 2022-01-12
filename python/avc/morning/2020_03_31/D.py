from collections import deque

h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]

def bfs():
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    que = deque()
    for i in range(h):
        for j in range(w):
            if a[i][j] == '#':
                que.append((i, j))
                a[i][j] = 0

    while que:
        p = que.popleft()
        for i in range(4):
            ny = p[0] + dy[i]
            nx = p[1] + dx[i]

            if 0 <= nx < w and 0 <= ny < h and a[ny][nx] == '.':
                que.append((ny,nx))
                a[ny][nx] = a[p[0]][p[1]] + 1
    ans = 0
    for i in range(h):
        ans = max(ans, *a[i])
    return ans

print(bfs())