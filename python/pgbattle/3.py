from collections import deque

def dfs(maze, py, px, qy, qx):
    stack = deque()
    stack.append((py, px))
    n = 'u'
    cnt = 0
    while stack:
        p = stack.pop()
        y = p[0]
        x = p[1]
        if cnt > 10**6:
            return -1
        if x == qx and y == qy:
            return cnt
        if n == 'u':
            for i, j in ([0, -1], [1, 0], [0, 1], [-1, 0]):
                ny = y + i
                nx = x + j
                if 0 <= ny < h and 0 <= nx < w and maze[ny][nx] != '#':
                    stack.append((ny, nx))
                    cnt += 1
                    if i == 0 and j == -1:
                        n == 'l'
                    if i == 1 and j == 0:
                        n == 'u'
                    if i == 0 and j == 1:
                        n == 'r'
                    if i == -1 and j == 0:
                        n == 'd'
                    break
        if n == 'd':
            for i, j in ([0, 1], [-1, 0], [0, -1], [1, 0]):
                ny = y + i
                nx = x + j
                if 0 <= ny < h and 0 <= nx < w and maze[ny][nx] != '#':
                    stack.append((ny, nx))
                    cnt += 1
                    if i == 0 and j == -1:
                        n == 'l'
                    if i == 1 and j == 0:
                        n == 'u'
                    if i == 0 and j == 1:
                        n == 'r'
                    if i == -1 and j == 0:
                        n == 'd'
                    break
        if n == 'r':
            for i, j in ([1, 0], [0, 1], [-1, 0], [0, -1]):
                ny = y + i
                nx = x + j
                if 0 <= ny < h and 0 <= nx < w and maze[ny][nx] != '#':
                    stack.append((ny, nx))
                    cnt += 1
                    if i == 0 and j == -1:
                        n == 'l'
                    if i == 1 and j == 0:
                        n == 'u'
                    if i == 0 and j == 1:
                        n == 'r'
                    if i == -1 and j == 0:
                        n == 'd'
                    break
        if n == 'l':
            for i, j in ([-1, 0], [0, -1], [1, 0], [0, 1]):
                ny = y + i
                nx = x + j
                if 0 <= ny < h and 0 <= nx < w and maze[ny][nx] != '#':
                    stack.append((ny, nx))
                    cnt += 1
                    if i == 0 and j == -1:
                        n == 'l'
                    if i == 1 and j == 0:
                        n == 'u'
                    if i == 0 and j == 1:
                        n == 'r'
                    if i == -1 and j == 0:
                        n == 'd'
                    break
    return -1

if __name__ == '__main__':
    h, w = map(int, input().split())
    px, py, qx, qy = map(int, input().split())
    px -= 1
    py -= 1
    qx -= 1
    qy -= 1
    maze = [input() for _ in range(h)]
    print(dfs(maze, py, px, qy, qx))