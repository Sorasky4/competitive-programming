x = int(input())
#6,5,6,5を繰り返す
if x % 11 == 0:
    ans = x // 11 * 2
elif 0 < x % 11 <= 6:
    ans = x // 11 * 2 + 1
else:
    ans = x // 11 * 2 + 2
print(ans)