import math
import itertools
n = int(input())
x = []
y = []
for _ in range(n):
    x1,y1 = map(int,input().split())
    x.append(x1)
    y.append(y1)
ans = 0
l = [int(i) for i in range(n)]
p = list(itertools.permutations(l,n))
for i in range(len(p)):
    for j in range(n-1):
        ans += ((x[p[i][j]]-x[p[i][j+1]])**2 + (y[p[i][j]]-y[p[i][j+1]])**2)**(0.5)
print(ans/math.factorial(n))