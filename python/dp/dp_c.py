n = int(input())
a = []
b = []
c = []
for i in range(n):
    x = list(map(int, input().split()))
    a.append(x[0])
    b.append(x[1])
    c.append(x[2])
# dp[i][j] = i+1日目で最後にjを選んだ時の最大幸福度
dp = [[0 for i in range(3)] for j in range(n)]
dp[0][0] = a[0]  # 1日目にaを選んだ場合
dp[0][1] = b[0]  # 1日目にbを選んだ場合
dp[0][2] = c[0]  # 1日目にcを選んだ場合
for i in range(1,n):
    # i+1日目にaを選んだ場合 = a[i](i+1日目のa)で得る幸福度 + 前日bまたはcを選んだ場合の最大幸福度
    dp[i][0] = a[i] + max(dp[i-1][1], dp[i-1][2])
    # i+1日目にbを選んだ場合 = b[i](i+1日目のb)で得る幸福度 + 前日aまたはcを選んだ場合の最大幸福度
    dp[i][1] = b[i] + max(dp[i-1][0], dp[i-1][2])
    # i+1日目にcを選んだ場合 = c[i](i+1日目のc)で得る幸福度 + 前日aまたはbを選んだ場合の最大幸福度
    dp[i][2] = c[i] + max(dp[i-1][0], dp[i-1][1])
# n日目(n-1+1日目)の幸福度の内、最大のものを出力
print(max(dp[n-1]))