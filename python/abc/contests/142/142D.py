import math
def div(n):
    i = 1
    a = []
    while i * i <= n:
        if n%i == 0:
            a.append(i)
            a.append(n//i)
        i += 1
    a = list(set(a))
    return a
def is_primeplus(n):
    if n == 1:
        return 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1
a,b = map(int,input().split())
c = list(set(div(a)) & set(div(b)))
ans = 0
for i in range(len(c)):
    if is_primeplus(c[i]):
        ans += 1
print(ans)