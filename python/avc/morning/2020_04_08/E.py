#わっかんねABC142-E
'''
n, m = map(int, input().split())
#ダメだったので解説
#bitDP
#0<=j<2**n, 1以上n以下の整数kについて、現在購入している鍵で宝箱kを開けられることと
#jを2進数表記したときにk-1桁目が1であることが同値という状態を表す
#dpi,j=i+1番目以降の鍵は購入せずに状態をjにする為に必要な最小費用
dp = [[float('inf') for j in range(2**n)] for i in range(1,m+1)]
dp[0][0] = 0
for i in range(1,m+1):
    a, b = map(int, input().split())
    c = sum(map(lambda x: int(x)-1, input().split()))
    for j in range(2**n):
        if (j >> c) & 1:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j] + a)
print(dp)
'''