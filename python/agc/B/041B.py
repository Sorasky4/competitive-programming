# WA

import collections
x = [int(i) for i in input().split()]
a = sorted([int(i) for i in input().split()],reverse=True)
n, m, v, p = x[0], x[1], x[2], x[3]
a_ = collections.Counter(a)
ans = 0
i = 0
while ans < p:
    ans += a_[a[i]]
    i = ans
l = a[:ans]
r = a[ans:]
l_r = l[-1]
l_r_cnt = a_[l_r]
if v <= ans - l_r_cnt + 1:
    for i in r:
        if l_r <= m + i:
            ans += 1
else:
    res = v - (ans - l_r_cnt + 1)
    cnt = l[-l_r_cnt:]
    for i in range(len(r)):
        can = m + r[i]
        if l_r <= can:
            if res <= len(r) - (i + 1):
                ans += 1
            else:
                res2 = res - (len(r) - (i + 1))
                if (sum(cnt) + res2 * m) / len(cnt) <= r[i] + m:
                    ans += 1
        cnt.append(r[i])
print(ans)