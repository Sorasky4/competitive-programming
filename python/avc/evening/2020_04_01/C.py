n, m = map(int, input().split())
q = []
s = []
for i in range(m):
    x = [int(i) for i in input().split()]
    q.append(x[0])
    s.append(x[1:])
p = list(map(int, input().split()))
ans = 0


for i in range(2**n):
    ok = True
    for j in range(m):
        on_cnt = 0
        for k in range(q[j]):
            for l in range(n):
                if i >> l & 1:
                    if l == s[j][k] - 1:
                        on_cnt += 1
        if on_cnt % 2 != p[j]:
            ok = False
    if ok:
        ans += 1
print(ans)