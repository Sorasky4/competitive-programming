# 512ms
# dequeをスタックとして使う
from collections import deque

def dfs(maze, visited, sy, sx):
    stack = deque()
    stack.append((sy, sx))
    visited[sy][sx] = 1
    while stack:
        p = stack.pop()
        y = p[0]
        x = p[1]
        if maze[y][x] == 'g':
            return 'Yes'
        for i, j in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            ny = y + i
            nx = x + j
            if 0 <= ny < h and 0 <= nx < w and maze[ny][nx] != '#' and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                stack.append((ny, nx))

    return 'No'

if __name__ == '__main__':
    h, w = map(int, input().split())
    maze = [input() for _ in range(h)]

    for i in range(h):
        if maze[i].find('s') != -1:
            sy = i
            sx = maze[i].find('s')
            break

    visited = [[0]*w for _ in range(h)]
    print(dfs(maze, visited, sy, sx))

'''
# 710ms
# 再帰を用いた実装
# まず再帰上限の引き上げ
import sys
sys.setrecursionlimit(10**7)

def dfs(y, x):
    if y < 0 or h <= y or x < 0 or w <= x or maze[y][x] == '#':
        return
    if visited[y][x] == 1:
        return
    visited[y][x] = 1

    # 4方向を試す
    dfs(y, x + 1) #右
    dfs(y + 1, x) #上
    dfs(y, x - 1) #左
    dfs(y - 1, x) #下


if __name__ == '__main__':
    h, w = map(int, input().split())
    maze = [list(input()) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]

    # 上下左右の4方向
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    # スタートとゴールを探す
    for i in range(h):
        for j in range(w):
            if maze[i][j] == 's':
                sy = i
                sx = j
            if maze[i][j] == 'g':
                gy = i
                gx = j

    dfs(sy, sx) # スタート地点から探索

    # ゴール地点に訪れたかどうか
    ans = 'Yes' if visited[gy][gx] == 1 else 'No'
    print(ans)
'''

'''
# 1710ms
# スタックを用いた実装
from queue import LifoQueue

def dfs(maze, h, w):
    visited = [[0]*w for _ in range(h)] # 0が未訪問 1が訪問済み
    # 上下左右の4方向
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    # スタートを探す
    for i in range(h):
        for j in range(w):
            if maze[i][j] == 's':
                sy = i
                sx = j
                break

    visited[sy][sx] = 1 # スタート地点を訪問済みにする
    q = LifoQueue()
    q.put((sy, sx)) # スタート地点をスタックに追加
    while not q.empty(): # スタックの中身がなくなるまで繰り返す
        p = q.get() # 最後にスタックにいれた地点を取り出す

        if maze[p[0]][p[1]] == 'g':
            return 'Yes'

        for i in range(4):
            ny = p[0] + dy[i]
            nx = p[1] + dx[i]
            if 0 <= ny < h and 0 <= nx < w and maze[ny][nx] != '#' and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                q.put((ny, nx))

    return 'No'


if __name__ == '__main__':
    h, w = map(int, input().split())
    maze = [list(input()) for _ in range(h)]
    print(dfs(maze, h, w))
'''