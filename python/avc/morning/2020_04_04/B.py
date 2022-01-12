n = int(input())
a = sorted(list(map(int, input().split())))
b = [0] * 10**5
ans = 1
if n == 2:
    if abs(a[0] - a[1]) <= 2:
        ans = 2
for i in range(n):
    b[a[i]] += 1
for i in range(n-2):
    ans = max(ans, b[i]+b[i+1]+b[i+2])

print(ans)