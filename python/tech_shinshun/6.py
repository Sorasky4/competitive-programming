l = sorted([int(input()) for _ in range(3)], reverse=True)
flag = True
ans = 0
res1 = l[0] - l[1]
res2 = l[1] - l[2]
if l[0] == l[1] == l[2]:
    ans = 3
    flag = False
while flag:
    if res1 == res2:
        break
    elif res1 > res2:
        l[0] -= 1
        ans += 1
    else:
        l[1] -= 1
        ans += 1
    res1 = l[0] - l[1]
    res2 = l[1] - l[2]
print(ans)