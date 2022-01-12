a,b,c,d = map(int,input().split())
ans = b - a + 1
x = c * d
e = c
f = d
if e < f:
    e = f
    f = c
r = e % f
while r != 0:
    e = f
    f = r
    r = e % f
x //= f
ans -= b // c - (a-1) // c + b // d - (a-1) // d
ans += b // x - (a-1) // x
print(ans)