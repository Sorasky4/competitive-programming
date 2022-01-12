s = input()
t = int(input())
x = 0
y = 0
idk = 0
for i in s:
    if i == 'R':
        x += 1
    elif i == 'L':
        x -= 1
    elif i == 'U':
        y += 1
    elif i == 'D':
        y -= 1
    else:
        idk += 1
ans = abs(x) + abs(y)
if t == 1:
    ans += idk
else:
    ans -= idk
    if ans < 0:
        if ans % 2 == 0:
            ans = 0
        else:
            ans = 1
print(ans)