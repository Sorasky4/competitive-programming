import math

n = int(input())
x = [int(i) for i in input().split()]
mod = 10**9 + 7
ans = 0
diff = [x[i+1] - x[i] for i in range(n-1)]
p = [0 for i in range(n-1)]
for i in range(n-1):
    for j in range(i+1):
        p[i] += pow(j+1,-1)
    ans += diff[i] * p[i]
ans = int((ans * math.factorial(n-1) % mod))
print(ans)

#TLEはおいといて何がダメなの･･･