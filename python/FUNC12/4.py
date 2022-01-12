n, k = map(int,input().split())
h = sorted([int(input()) for _ in range(n)],reverse=True)
ans = h[0] - h[k-1]
for i in range(0,n-k+1):
    ans = min(ans, h[i] - h[i+k-1])
print(ans)