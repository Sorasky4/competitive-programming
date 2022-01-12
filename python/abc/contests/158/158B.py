n, a, b = map(int,input().split())
c = a + b  #1セットのボール
d = n % c  #先頭からN個取った時、セットにならなかったボール(余り)
ans = (n // c) * a
if a <= d:
    ans += a
else:
    ans += d
print(ans)