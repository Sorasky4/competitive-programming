a = sorted(list(map(int, input().split())))
ans = 0
while a[2] - a[0] > 0 and a[2] - a[1] > 0:
    a[0] += 1
    a[1] += 1
    ans += 1
if (a[2] - min(a[0],a[1])) & 1:
    ans += -((-(a[2] - min(a[0], a[1])) // 2)) + 1
else:
    ans += (a[2] - min(a[0], a[1])) // 2
print(ans)