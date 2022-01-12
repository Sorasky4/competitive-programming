n, t = map(int,input().split())
a = [int(input()) for _ in range(n)]
ans = t
for i in range(n-1):
    if a[i+1] - a[i] <= t:
        ans += a[i+1] - a[i]
    else:
        ans += t
print(ans)