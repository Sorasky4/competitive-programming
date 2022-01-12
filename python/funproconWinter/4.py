n = int(input())
m = int(input())
l = []
r = []
p = []
q = []
for i in range(m):
    l1, p1 = map(int,input().split())
    l.append(l1)
    r.append(p1)
    p.append(p1)
    q.append(p1-1)
ans = 0
for i in range(m):
    for j in range(l[i],l[i] + r[i]):
        if n < j:
            break
        ans += p[i]
        p[i] -= 1
    for j in range(l[i]-1,l[i]-r[i],-1):
        if j < 1:
            break
        ans += q[i]
        q[i] -= 1
print(ans)