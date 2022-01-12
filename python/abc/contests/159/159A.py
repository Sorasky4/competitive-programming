def nCk(n, k, m=10**9+7):
    a = b = 1
    for i in range(k):
        a = (a * (n-i)) % m
        b = (b * (i+1)) % m
    return (a * pow(b, m-2, m)) % m

n,m = map(int, input().split())
ans = 0
if n > 1:
    ans += nCk(n, 2)
if m > 1:
    ans += nCk(m, 2)
print(ans)