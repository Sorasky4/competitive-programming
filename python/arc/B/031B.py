from collections import deque

def dfs(maze):
    for i in range(10):
        for j in range(10):
            ok = True
            visited = [[0]*10 for _ in range(10)]
            sy = i
            sx = j
            dy = [0, 1, 0, -1]
            dx = [1, 0, -1, 0]
            q = deque()
            q.append((sy, sx))
            while q:
                p = q.pop()
                for k in range(4):
                    ny = p[0] + dy[k]
                    nx = p[1] + dx[k]
                    if 0 <= ny < 10 and 0 <= nx < 10 and \
                       maze[ny][nx] != 'x' and visited[ny][nx] == 0:
                       visited[ny][nx] = 1
                       q.append((ny, nx))
            for k in range(10):
                if ok:
                    for l in range(10):
                        if maze[k][l] == 'o' and visited[k][l] != 1:
                            ok = False
                            break
                else:
                    break
            if ok:
                return 'YES'
    return 'NO'


country = [input() for _ in range(10)]
print(dfs(country))