from math import gcd

n, q = map(int, input().split())
a = list(map(int, input().split()))
s = list(map(int, input().split()))
b = [0] * n
b[0] = a[0]
for i in range(1,n):
    b[i] = gcd(b[i-1], a[i])
for i in range(q):
    c = gcd(s[i], b[-1])
    if c != 1:
        print(c)
        continue
    l = 0
    r = n
    while l < r:
        mid = (l + r) // 2
        if gcd(s[i], b[mid]) == 1:
            r = mid
        else:
            l = mid + 1
    print(l+1)