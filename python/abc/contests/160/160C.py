k, n = map(int, input().split())
a = [int(i) for i in input().split()]
ans = a[-1] - a[0]
for i in range(1,n):
    ans = min(ans, k - a[i] + a[i-1])
print(ans)