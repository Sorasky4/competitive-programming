import itertools
import math

n = int(input())
p = [i for i in input().split()]
q = [i for i in input().split()]

perm = sorted(list(itertools.permutations([str(int(i+1)) for i in range(n)])))
for i in range(math.factorial(n)):
    if list(perm[i]) == p:
        a = i + 1
    if list(perm[i]) == q:
        b = i + 1
print(abs(a-b))