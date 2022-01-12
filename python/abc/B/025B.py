n, a, b = map(int, input().split())
ans = 0
for i in range(n):
    s, d = map(str, input().split())
    d = int(d)
    if s == 'West':
        if d < a:
            ans -= a
        elif a <= d <= b:
            ans -= d
        else:
            ans -= b
    else:
        if d < a:
            ans += a
        elif a <= d <= b:
            ans += d
        else:
            ans += b
if ans < 0:
    print('West', -ans)
elif ans == 0:
    print(0)
else:
    print('East', ans)