x, y = map(int, input().split())
ans = 1

while x <= y//2:
    x *= 2
    ans += 1

if x > y:
    ans -= 1

print(ans)