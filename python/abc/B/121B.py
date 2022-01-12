n,m,c = map(int,input().split())
b = list(map(int,input().split()))
a = [list(map(int,input().split())) for i in range(n)]
cnt = 0
ans = 0
for i in range(n):
    for j in range(m):
        cnt += a[i][j]*b[j]
    cnt += c
    if cnt > 0:
        ans += 1
    cnt = 0
print(ans)