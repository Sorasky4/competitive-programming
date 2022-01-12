#import math
#import fractions
from functools import reduce

'''
def gcdList(ls):
    return reduce(math.gcd, ls)
#    return reduce(fractions.gcd, ls)
'''

def gcd(a,b):
    while b:
        a, b = b, a % b
    return a
def gcdList(ls):
    return reduce(gcd,ls)

n,y = map(int,input().split())
x = sorted([int(i) for i in input().split()])
x_ = [0 for _ in range(n)]
for i in range(n):
    x_[i] = abs(y-x[i])
print(gcdList(x_))