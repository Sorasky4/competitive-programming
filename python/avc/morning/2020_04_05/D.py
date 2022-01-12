n = int(input())
a = list(map(int, input().split()))
ans = [0] * n
s = sum(a)
e = 0
for i in range(1,n,2):
    e += a[i]
ans[0] = s - 2 * e
for i in range(n-1):
    ans[i+1] = 2 * a[i] - ans[i]
print(*ans)