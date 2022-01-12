n,x = map(int,input().split())
m = sorted([int(input()) for _ in range(n)])
for i in range(n):
    x -= m[i]
ans = x // m[0] + n
print(ans)