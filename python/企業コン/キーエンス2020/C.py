n, k, s = map(int, input().split())
ans = []
for i in range(k):
    ans.append(s)
for i in range(0,n-k):
    if s == 10**9:
        ans.append(1)
    else:
        ans.append(s+1)
print(*ans)