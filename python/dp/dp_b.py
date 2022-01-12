#pypyなら通る
n, k = map(int, input().split())
h = [int(i) for i in input().split()]

dp = [0] * n
dp[1] = abs(h[1] - h[0])

for i in range(2,n):
    min_cost = 999999999
    for j in range(1,min(i,k)+1):
        tmp = dp[i-j] + abs(h[i] - h[i-j])
        min_cost = min(min_cost, tmp)
    dp[i] = min_cost

print(dp[n-1])