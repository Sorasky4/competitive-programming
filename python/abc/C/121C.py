'''n,m = map(int,input().split())
a = []
b = []
for _ in range(n):
    a1,b1 = map(int,input().split())
    a.append(a1)
    b.append(b1)
ans = 0
cnt = 0
flag = 1
while flag:
    flag = 0
    for i in range(n-1,0,-1):
        if a[i] < a[i-1]:
            a[i],a[i-1] = a[i-1],a[i]
            b[i],b[i-1] = b[i-1],b[i]
            flag = 1
for i in range(n):
    flag = 1
    while b[i] > 0 and cnt < m:
        ans += a[i]
        cnt += 1
        b[i] -= 1
        flag = 0
    if flag:
        break
print(ans)'''

n,m = map(int,input().split())
a = []
b = []
for _ in range(n):
    a1,b1 = map(int,input().split())
    a.append(a1)
    b.append(b1)
c = sorted(zip(a,b))
ans = 0
for i in range(n):
    if m > c[i][1]:
        ans += c[i][0]*c[i][1]
        m -= c[i][1]
    else:
        ans += c[i][0]*m
        break
print(ans)