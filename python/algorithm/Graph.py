n = int(input())
m = [[0 for i in range(n)] for j in range(n)]
s = [input().split() for i in range(n)]
for i in range(n):
    u,k = int(s[i][0]),int(s[i][1])
    u -= 1
    for j in range(2,k+2):
        v = int(s[i][j])
        v -= 1
        m[u][v] = 1
for i in range(n):
    print(' '.join(map(str,m[i])))