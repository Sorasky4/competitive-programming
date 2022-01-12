n = int(input())
k = int(input())
x = [int(i) for i in input().split()]
ans = 0
for i in range(n):
    type_a = x[i] * 2
    type_b = (k - x[i]) * 2
    ans += min(type_a, type_b)
print(ans)