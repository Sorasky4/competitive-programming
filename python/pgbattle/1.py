n = int(input())
s = [input() for _ in range(n)]
ans = 0
for i in s:
    if i == 'WA' or i == '-':
        ans += 5
print(ans)