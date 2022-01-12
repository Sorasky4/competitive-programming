n = int(input())
a = [int(i) for i in input().split()]
ans = 0
for i in a:
    while i % 2 == 0:
        i //= 2
        ans += 1
print(ans)