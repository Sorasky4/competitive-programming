from fractions import gcd  #python 3.5より前
#from math import gcd  #python 3.5以降
n = int(input())
a = sorted([int(i) for i in input().split()])
ans = gcd(a[0],a[1])
for i in range(2,len(a)):
    ans = min(ans,gcd(ans,a[i]))
print(ans)