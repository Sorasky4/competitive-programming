n = int(input())
p = [int(i) for i in input().split()]
ans = n
tmp = p[0]
for i in range(n):
    if p[i] <= tmp:
        tmp = p[i]
    else:
        ans -= 1
print(ans)