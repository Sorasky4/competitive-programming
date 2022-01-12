import collections

def div(n):
    a = []
    for i in range(2,n+1):
        while n % i == 0:
            a.append(i)
            n //= i
    return a

n = int(input())
ans = 1
g = []
h = 1
d = collections.Counter(div(n))
e = list(d.values())
f = list(d.keys())
for i in range(len(e)):
    for j in range(e[i]):
        g.append(f[i])
for i in range(len(e)):
    h *= (e[i]+1)
print(h)

'''無理！！！'''