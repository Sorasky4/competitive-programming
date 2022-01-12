n, k = map(int,input().split())
r, s, p = map(int,input().split())
t = input()
win = ['x' for i in range(n)]
ans = 0
if t[0] == 'r':
    win[0] = 'p'
elif t[0] == 's':
    win[0] = 'r'
else:
    win[0] = 's'
for i in range(1,n):
    if t[i] == 'r':
        win[i] = 'p'
    elif t[i] == 's':
        win[i] = 'r'
    else:
        win[i] = 's'
for i in range(k,n):
    if win[i-k] == win[i] and win[i-k] != 'x':
        win[i] = 'x'
for i in range(n):
    if win[i] == 'r':
        ans += r
    elif win[i] == 's':
        ans += s
    elif win[i] == 'p':
        ans += p
print(ans)