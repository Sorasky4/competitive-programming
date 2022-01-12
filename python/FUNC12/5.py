n, k = map(int,input().split())
r, s, p = map(int,input().split())
t = [i for i in input()]
ans = 0
for i in range(n):
    if t[i] == 'r':
        tmp = p
        ans += p
    elif t[i] == 's':
        tmp = r
        ans += r
    elif t[i] == 'p':
        tmp = s
        ans += s
    if k <= i and t[i-k] == t[i]:
        ans -= tmp
        t[i] = 'X'
print(ans)