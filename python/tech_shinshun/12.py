def nPk(n, k, m):
    a = 1
    for i in range(n,n-k,-1):
        a = (a * i) % m
    return a
def nCk(n, k, m):
    a = b = 1
    for i in range(k):
        a = (a * (n-i)) % m
        b = (b * (i+1)) % m
    return (a * pow(b, m-2, m)) % m

n,m = map(int,input().split())
s = [int(i) for i in input().split()]
mod = 998244353
one = 0
for i in range(n):
    if s[i] == 1:
        one += 1
cnt = nPk(m,one,mod)
res = m - one
if res % 2 == 0:
    cmb = nCk(one+(res//2)-1,res//2,mod)
    ans = cnt
    for i in range(1,res//2+1):
        ans += (cnt//(m-(one-i))*one) % mod
o = n - one
ans += o*cnt
print(ans)