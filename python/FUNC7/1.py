n,x = map(int,input().split())
m = [int(input()) for _ in range(n)]
ans = 0
minm = 1000
for i in range(n):
    x -= m[i]
    minm = min(minm,m[i])
    ans += 1
while x >= minm:
    x -= minm
    ans += 1
print(ans)