n = int(input())
a = [int(i) for i in input().split()]
m = 10**9+7
ans = 1
rgb = [0,0,0]
for i in range(n):
    cnt = 1
    for j in range(3):
        if a[i] == rgb[j]:
            cnt += 1
    if cnt != 1:
        cnt -= 1
    ans *= cnt
    if a[i] == 0 and 0 in rgb:
        rgb[rgb.index(0)] += 1
    else:
        rgb[rgb.index(a[i])] += 1
cnt = 1
for i in range(3):
    if a[-1] == rgb[i]:
        cnt += 1
if cnt != 1:
    cnt -= 1
ans *= cnt
print(ans%m)