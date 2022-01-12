from collections import deque
import copy

h,w = map(int,input().split())
s = []
wall = '#'
for i in range(h):
    s.append(input())
s = [list(i) for i in s]
for i in range(h):
    for j in range(w):
        if s[i][j]=='.':
            s[i][j]=float("inf")
    s[i] = [wall] + s[i] + [wall]
s = [[wall for i in range(w+2)]] + s + [[wall for i in range(w+2)]]
tmp = copy.deepcopy(s)
ans = 0
for i in range(1,h+1):
    for j in range(1,w+1):
        tmp[i][j] = 0
        que = deque([[i,j]])
        while que:
            y, x = que.popleft()
            for a,b in [(1,0),(-1,0),(0,1),(0,-1)]:
                ny = y + a
                nx = x + b
                dist = tmp[ny][nx]
                if dist != '#':
                    if dist > tmp[y][x] + 1:
                        tmp[ny][nx] = tmp[y][x]+1
                        que.append([ny,nx])
        for k in range(1,h+1):
            for l in range(1,w+1):
                if tmp[k][l] != '#':
                    ans = max(ans,tmp[k][l])
        tmp = copy.deepcopy(s)
print(ans)