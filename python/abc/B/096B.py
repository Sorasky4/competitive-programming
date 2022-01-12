a = list(map(int,input().split()))
k = int(input())
ans = sum(a)
m = max(a[0],a[1],a[2])
ans -= m
for _ in range(k):
    m *= 2
ans += m
print(ans)