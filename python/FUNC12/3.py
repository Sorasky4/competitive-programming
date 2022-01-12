n = int(input())
a = sorted([int(input()) for _ in range(n)])
ans = 0
tmp = 1
for i in range(n-1):
    if a[i] == a[i+1]:
        tmp += 1
    else:
        if tmp % 2 == 1:
            ans += 1
        tmp = 1
if tmp % 2 == 1:
    ans += 1
print(ans)