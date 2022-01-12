n, W = map(int, input().split())
w = []
v = []
for _ in range(n):
    ww, vv = map(int, input().split())
    w.append(ww)
    v.append(vv)

dp = [[float('inf') for j in range(10**5+1)] for i in range(n+1)]
dp[0][0] = 0

for i in range(n):
    for j in range(10**5+1):
        if j < v[i]:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = min(dp[i][j], dp[i][j-v[i]] + w[i])
ans = 0
for i in range(10**5,-1,-1):
    if dp[n][i] <= W:
        ans = i
        break
print(ans)

# 今回は横軸を重さではなく価値で取り、各価値のときの重さの最小値を求めた。