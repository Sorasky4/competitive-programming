n = int(input())
a,b = map(int,input().split())
x,y = map(int,input().split())
mod = 998244353

from functools import lru_cache
@lru_cache(maxsize=None)
def Fib(n):
    if n == 1:
        return x
    elif n == 2:
        return y
    else:
        return Fib(n-1)*a + Fib(n-2)*b

print(Fib(n)%mod)