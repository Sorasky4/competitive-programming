import collections
n = int(input())
d = [int(i) for i in input().split()]
ans = 0
if d[0] == 0:
    s = collections.Counter(d)
    ss = sorted(s.items())
    if ss[0][1] == 1:
        ans = 1
        for i in range(1,len(ss)):
            if ss[i][0] != ss[i-1][0] + 1:
                ans = 0
                break
            ans *= ss[i-1][1]**ss[i][1]
print(ans%998244353)