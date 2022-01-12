'''
h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
for i in range(h):
    s[i].insert(0,'9')
    s[i].append('9')
wall = ['9' for _ in range(w+2)]
s.insert(0, wall)
s.append(wall)
ans = [[0 for i in range(w)] for j in range(h)]
for i in range(1,h+1):
    for j in range(1, w+1):
        if s[i][j] == '.':
            cnt = 0
            for k in range(i-1,i+2):
                for l in range(j-1,j+2):
                    if s[k][l] == '#':
                        cnt += 1
            s[i][j] = cnt
        ans[i-1][j-1] = s[i][j]
for i in ans:
    print(*i, sep='')
'''

#解説コード

h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

dx = [-1, 0, 1, 1, 1, 0, -1, -1]  #任意のマスの周り8方向のマスの差分を
dy = [1, 1, 1, 0, -1, -1, -1, 0]  #左上から時計回りに用意した

for i in range(h):
    for j in range(w):
        if s[i][j] == '.':
            bomb = 0
            for k in range(8):
                if 0 <= i + dy[k] < h and 0 <= j + dx[k] < w:
                    if s[i+dy[k]][j+dx[k]] == '#':
                        bomb += 1
            s[i][j] = bomb
for i in s:
    print(*i, sep='')