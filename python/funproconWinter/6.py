X,Y = map(int,input().split())
n = int(input())
x = []
y = []
for i in range(n):
    x1, y1 = map(int,input().split())
    x.append(x1)
    y.append(y1)
ans = 0
if min(x) < min(y):
    while X > 0:
        X -= min(x)
        Y -= y[x.index(min(x))]
        ans += 1
else:
    while Y > 0:
        X -= x[y.index(min(y))]
        Y -= min(y)
        ans += 1
print(ans)