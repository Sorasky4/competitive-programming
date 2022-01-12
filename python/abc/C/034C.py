def nCk(n, k, m=10**9+7):
    a = b = 1
    for i in range(k):
        a = (a * (n-i)) % m
        b = (b * (i+1)) % m
    return (a * pow(b, m-2, m)) % m

w, h = map(int, input().split())
w -= 1
h -= 1
n = w + h
k = min(w, h)
print(nCk(n, k))