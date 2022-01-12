from collections import Counter

def nCk(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result

n = int(input())
a = list(map(int, input().split()))
b = Counter(a)
c = {}
d = {}
for k, v in b.items():
    c[k] = nCk(v, 2) if v > 1 else 0
    d[k] = nCk(v-1, 2) if v > 2 else 0
total = sum(c.values())
for i in range(n):
    ans = total - c[a[i]] + d[a[i]]
    print(ans)