import bisect
n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
p = []
m = []
for i in range(n):
    if a[i] - b[i] > 0:
        p.append(a[i] - b[i])
    else:
        m.append(a[i] - b[i])
p.sort()
ans = (len(p) * (len(p) - 1)) // 2
for i in m:
    ans += len(p) - bisect.bisect_left(p, abs(i) + 1)
print(ans)