n = int(input())
s = sorted([int(input()) for _ in range(n)])
ans = sum(s)
if str(ans)[-1] == '0':
    for i in s:
        if str(i)[-1] != '0':
            ans -= i
            break
    else:
        ans = 0
print(ans)