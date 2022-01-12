x,y = map(int,input().split())
if abs(x) == abs(y):
    ans = 1
elif x > y:
    if y < 0:
        if x < 0:
            ans = abs(y) - abs(x) + 2
        else:
            ans = abs(x - abs(y)) + 1
    elif y > 0:
        ans = x - y + 2
    else:
        ans = x + y + 1
else:
    if y < 0:
        ans = abs(x-y)
    elif y > 0:
        if x < 0:
            ans = abs(y - abs(x)) + 1
        else:
            ans = y - x
    else:
        if x < 0:
            ans = abs(x)
        else:
            ans = x + 1
print(ans)