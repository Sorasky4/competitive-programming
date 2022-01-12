h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
dp = [[float('inf') for i in range(w)] for j in range(h)]
if s[0][0] == '.':
    dp[0][0] = 0
    total = 0
else:
    dp[0][0] = 1
    total = 1
for i in range(1,w):
    if s[0][i] == '#':
        if s[0][i-1] == '#':
            dp[0][i] = total
        else:
            total += 1
            dp[0][i] = total
    else:
        dp[0][i] = total
if s[0][0] == '.':
    total = 0
else:
    total = 1
for i in range(1,h):
    if s[i][0] == '#':
        if s[i-1][0] == '#':
            dp[i][0] = total
        else:
            total += 1
            dp[i][0] = total
    else:
        dp[i][0] = total
for i in range(1,h):
    for j in range(1,w):
        if s[i][j] == '#':
            if s[i-1][j] == '#' and s[i][j-1] == '#':
                dp[i][j] = min(dp[i-1][j], dp[i][j-1])
            elif s[i-1][j] == '#':
                dp[i][j] = min(dp[i-1][j], dp[i][j-1] + 1)
            elif s[i][j-1] == '#':
                dp[i][j] = min(dp[i][j-1], dp[i-1][j] + 1)
            else:
                dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1)
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1])
print(dp[h-1][w-1])