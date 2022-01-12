import math

n,m = map(int,input().split())
large = n if n >= m else m
ans = math.factorial(large)
if abs(n-m)>1:
    ans = 0
elif n == m:
    ans *= (math.factorial(n)*2)
else:
    ans *= math.factorial(large-1)
print(ans%(10**9+7))