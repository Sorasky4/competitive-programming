import collections
n = int(input())
s = [i for i in input()]
m = 0
for i in range(1,n):
    x = s[0:i]
    y = s[i:n]
    c1 = collections.Counter(x)
    c2 = collections.Counter(y)
    d1 = set(c1.keys())
    d2 = set(c2.keys())
    e = list(d1 & d2)
    m = max(m,len(e))
print(m)