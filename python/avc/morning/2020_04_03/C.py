import bisect

n = int(input())
l = sorted(list(map(int, input().split())))
ans = 0

for a in range(n):
    for b in range(a):
        over_c = l[a] + l[b]
        over_c_index = bisect.bisect_left(l,over_c)
        quantity = over_c_index - a - 1
        ans += max(quantity,0)
print(ans)