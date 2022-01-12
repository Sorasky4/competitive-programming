a = list(map(int,input().split()))
mod = 10**9 + 7
x = 1
for i in a:
    x *= i
print(x % mod)