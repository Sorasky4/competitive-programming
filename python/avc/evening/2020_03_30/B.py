n = int(input())
a = []
for i in range(2):
    a.append(list(map(int, input().split())))
ans = 0
for i in range(n):
    ans = max(ans, sum(a[0][:i+1]) + sum(a[1][i:]))
print(ans)