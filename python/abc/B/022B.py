'''
import collections
n = int(input())
a = collections.Counter([int(input()) for _ in range(n)])
ans = sum([i-1 for i in a.values() if i >= 2])
print(ans)
'''
'''
n = int(input())
a = sorted([input() for _ in range(n)])
ans = 0
for i in range(1,n):
    if a[i-1] == a[i]:
        ans += 1
print(ans)
'''
n = int(input())
a = [input() for _ in range(n)]
ans = len(a) - len(set(a))
print(ans)