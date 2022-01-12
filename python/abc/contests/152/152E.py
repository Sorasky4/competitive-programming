import fractions
#import math
from functools import reduce

def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

n = int(input())
a = [int(i) for i in input().split()]
mod = 10 ** 9 + 7
ans = 0
b = lcm(*a)

for i in range(n):
    ans += b // a[i]
print(ans%mod)