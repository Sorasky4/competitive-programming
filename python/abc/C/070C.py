from fractions import gcd  #python 3.5より前
n = int(input())
t = sorted([int(input()) for _ in range(n)])
ans = 1
for i in range(n):
    ans = ans*t[i]//gcd(ans,t[i])
print(ans)