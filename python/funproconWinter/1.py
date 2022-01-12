n = int(input())
a = sorted([int(i) for i in input().split()])
ans = 0
for i in range(n):
    ans += abs(a[i] - a[i+n]) + abs(a[i+n] - a[i+2*n])
print(ans)