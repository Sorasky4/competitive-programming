import collections

n = int(input())
a = [list(map(int,input().split())) for i in range(n)]
ans = 0
b = [0]*(n*n)
for i in range(n):
    for j in range(n):
        b[i*n+j] = a[i][j]
c = collections.Counter(b)
c = list(c.values())
for i in range(len(c)):
    while c[i] > 1:
        c[i] -= 1
        ans += 1
print(ans)