n,q = map(int,input().split())
a = []
b = []
p = []
x = []
for i in range(n-1):
    a1,b1=[int(i) for i in input().split()]
    a.append(a1)
    b.append(b1)
for i in range(q):
    p1,x1=[int(i) for i in input().split()]
    p.append(p1)
    x.append(x1)
cnt = [0]*n
root = [0]*n
for i in range(q):
    cnt[p[i]-1] += x[i]
    for j in range(n-1):
        if a[j] == p[i]:
            cnt[b[j]-1] += x[i]
            root[j] = b[j]
        if a[j] in root:
            cnt[b[j]-1] += x[i]
            root[j] = b[j]
    root = [0]*n
print(' '.join(map(str,cnt)))