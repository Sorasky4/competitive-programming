w, h, n = map(int, input().split())
l = 0
r = w
u = h
d = 0
for i in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        l = max(l, x)
    elif a == 2:
        r = min(r, x)
    elif a == 3:
        d = max(d, y)
    else:
        u = min(u, y)
print((r - l) * (u - d) if r - l > 0 and u - d > 0 else 0)