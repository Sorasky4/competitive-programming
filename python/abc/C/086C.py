n = int(input())
nowt, nowx, nowy = 0, 0, 0
ans = 'Yes'
for i in range(n):
    t, x, y = map(int, input().split())
    dift, difxy = t - nowt, abs(x - nowx) + abs(y - nowy)
    if dift < difxy or dift&1 != difxy&1:
        ans = 'No'
print(ans)