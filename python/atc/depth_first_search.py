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