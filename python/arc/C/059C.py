n = int(input())
a = sorted([int(i) for i in input().split()])
ans = 10**9
for i in range(-100,101):
    cnt = 0
    for j in range(n):
        cnt += (a[j] - i)**2
    ans = min(ans,cnt)
print(ans)