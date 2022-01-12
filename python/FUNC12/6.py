n, m = map(int,input().split())
x = [[float('inf') for i in range(n)] for i in range(n)]
for i in range(m):
    l, r, d = map(int,input().split())
    x[l-1][r-1] = d
print(x)