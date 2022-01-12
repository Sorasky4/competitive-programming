def nCk(n, k, m=10**9+7):
    a = b = 1
    for i in range(k):
        a = (a * (n-i)) % m
        b = (b * (i+1)) % m
    return (a * pow(b, m-2, m)) % m

x,y = map(int,input().split())
if (x+y)%3 != 0 or min(x,y)*2 < max(x,y):
    ans = 0
else:
#パスカルの三角形より,n-1Ck-1を求める
    n = (x+y)//3 + 1
    k = x - (n-1) + 1
    ans = nCk(n-1,k-1)
print(ans)