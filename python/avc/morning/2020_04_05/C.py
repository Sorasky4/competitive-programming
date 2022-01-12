from fractions import gcd
n, X = map(int, input().split())
x = list(map(int, input().split()))
a = []
for i in range(n):
    a.append(abs(X-x[i]))
if n > 1:
    b = gcd(a[0],a[1])
else:
    b = a[0]
for i in range(n):
    b = gcd(b,a[i])
print(b)