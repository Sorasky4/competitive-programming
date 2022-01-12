import collections
def div(n):
    a = []
    for i in range(2,n+1):
        while n % i == 0:
            a.append(i)
            n //= i
    return a
n = int(input())
cnt = 1
ans = 0
for i in range(1,n+1,2):
    a = collections.Counter(div(i))
    a = list(a.values())
    for j in range(len(a)):
        cnt *= (a[j]+1)
    if cnt == 8:
        ans += 1
    cnt = 1
print(ans)