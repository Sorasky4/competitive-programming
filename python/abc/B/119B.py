n = int(input())
x = []
u = []
ans = 0
for i in range(n):
    x1,u1 = [str(i) for i in input().split()]
    x.append(x1)
    u.append(u1)
for i in range(n):
    if u[i] == 'BTC':
        ans += float(x[i]) * 380000.0
    else:
        ans += int(x[i])
print(ans)