from math import pi

n = int(input())
r = sorted([int(input()) for _ in range(n)], reverse=True)
if n == 1:
    print(r[0] ** 2 * pi)
else:
    area = [0 for _ in range(n)]
    for i in range(n-1):
        area[i] = (r[i] ** 2 - r[i+1] ** 2) * pi
    area[-1] = r[-1] ** 2 * pi
    ans = 0
    for i in range(0,n,2):
        ans += area[i]
    print(ans)