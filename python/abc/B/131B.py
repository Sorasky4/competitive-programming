n,l = map(int,input().split())
a = [0]*n
for i in range(n):
    a[i] = l + i
sum_ = sum(a)
cnt = abs(a[0])
ans = sum(a) - a[0]
for i in range(n):
    v = a[i]
    a[i] = 0
    if abs(sum_ - sum(a)) <= cnt:
        cnt = abs(sum_ - sum(a))
        ans = sum(a)
    a[i] = v
print(ans)