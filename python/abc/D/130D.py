n, k = map(int, input().split())
a = [int(i) for i in input().split()]
# 累積和で全区間考えるとO(n^2)で間に合わない
# 区間の左端を固定して、条件を満たす最小区間を見つけたら残り右側全て条件を満たす
# 尺取り法を使う
ans = 0
r = 0
total = 0
for l in range(n):
    while total < k:
        if r < n:
            total += a[r]
            r += 1
        else:
            break
    if total < k:
        break
    else:
        total -= a[l]
        ans += n - r + 1
print(ans)