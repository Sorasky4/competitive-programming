n = int(input())
ans = ''
s = []
p = []
for i in range(n):
    ss, pp = map(str, input().split())
    s.append(ss)
    p.append(int(pp))
border = sum(p) / 2
for i, j in zip(s, p):
    if border < j:
        ans += i
if ans:
    print(ans)
else:
    print('atcoder')