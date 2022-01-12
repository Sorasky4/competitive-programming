N,T = map(int,input().split())
t = list(map(int,input().split()))
ans = T
for i in range(N-1):
    if t[i+1] - t[i] <= T:
        ans += t[i+1] - t[i]
    else:
        ans += T
print(ans)