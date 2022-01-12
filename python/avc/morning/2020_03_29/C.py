n, k = map(int, input().split())
p = list(map(int, input().split()))
l = 0
r = k
t = sum(p[l:r])
ans = (t+k)/2
for _ in range(n-k):
    t -= p[l]
    t += p[r]
    l += 1
    r += 1
    ans = max(ans, (t+k)/2)
print(ans)