n = int(input())
h = [int(i) for i in input().split()]

# dp[i] = iマス目にたどり着くまでの最小コスト
dp = [float('inf')] * n
# 最初のマスまでのコストは0
dp[0] = 0
# 2マス目への行き方は「最初のマスから1つ進む」の1通り
dp[1] = abs(h[1] - h[0])
# 3マス目以降は「1つ前のマスから1つ進む」と「2つ前のマスから2つ進む」の2通り
for i in range(2,n):
    # 1つ前から移動したときの最小コスト
    step1 = dp[i-1] + abs(h[i] - h[i-1])
    # 2つ前から移動したときの最小コスト
    step2 = dp[i-2] + abs(h[i] - h[i-2])
    dp[i] = min(step1, step2)
print(dp[n-1])
