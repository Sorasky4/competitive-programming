n = int(input())
a = sorted(list(map(int, input().split())))
b = [0 for _ in range(n)]

if n % 2:
    for i in range(1,n,2):
        b[i] = b[i+1] = n - i
else:
    for i in range(0,n,2):
        b[i] = b[i+1] = n - (i + 1)
b.sort()

for i, j in zip(a, b):
    if i != j:
        print(0)
        exit()

print((2**(n//2))%(10**9+7))