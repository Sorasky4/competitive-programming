n,m = map(int,input().split())
s = [[] for _ in range(n+1)]
for i in range(m):
    p,y = map(int,input().split())
    s[p].append([y,i])
ans = [0]*m
for p in range(1,n+1):
    cnt = 1
    for (y,i) in sorted(s[p]):
        ans[i] = '{:06}{:06}'.format(p,cnt)
        cnt += 1
for j in range(len(ans)):
    print(ans[j])