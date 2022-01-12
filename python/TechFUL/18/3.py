import collections

def div(n):
    a = []
    for i in range(2,n+1):
        while n % i == 0:
            a.append(i)
            n //= i
    return a

n,k = map(int,input().split())
cnt = 1
a = collections.Counter(div(n))
a = list(a.values())
for i in range(len(a)):
    cnt *= a[i]*k + 1
print(cnt)