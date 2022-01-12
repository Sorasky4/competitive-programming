n = int(input())
y = []
for i in range(n):
    xx,yy = map(int,input().split())
    y.append(yy)
ans = 0
if n < 3:
    print(ans)
    exit(0)
while len(y) > 2:
    y.sort(reverse=True)
    min_y = min(y[0],y[1],y[2])
    y[0] -= min_y
    y[1] -= min_y
    y[2] -= min_y
    ans += min_y
    if y[0] == 0 and y[1] == 0 and y[2] == 0:
        del y[0:3]
    elif y[0] == 0 and y[1] == 0:
        del y[0:2]
    elif y[0] == 0 and y[2] == 0:
        del y[0:3:2]
    elif y[1] == 0 and y[2] == 0:
        del y[1:3]
    elif y[0] == 0 or y[1] == 0 or y[2] == 0:
        y.remove(0)
print(ans)