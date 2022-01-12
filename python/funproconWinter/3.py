n, m = map(int,input().split())
ans = [0 for _ in range(m+1)]
ans[n-1] = 1
for i in range(n,m+1):
    for j in range(i-n,i):
        ans[i] += ans[j]
print(ans[m])