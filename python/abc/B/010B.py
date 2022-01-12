n = int(input())
a = [int(i) for i in input().split()]
ans = 0
for i in a:
    if i % 2 == 0 and i % 3 == 0:
        ans += 3
    elif (i + 1) % 2 == 0 and (i + 1) % 3 == 0:
        ans += 2
    elif i % 2 == 0:
        ans += 1
print(ans)