n = int(input())
s = [list(input()) for j in range(n)]
ans = [[s[n-i-1][j] for i in range(n)] for j in range(n)]
for i in ans:
    print(*i, sep='')