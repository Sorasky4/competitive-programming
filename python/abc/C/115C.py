n,k = map(int,input().split())
h = sorted([int(input()) for _ in range(n)])
ans = h[k-1] - h[0]
for i in range(n-k+1):
    ans = min(ans,abs(h[i] - h[i+k-1]))
print(ans)