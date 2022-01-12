s, l, r = map(int, input().split())
if s <= l:
    ans = l
elif r <= s:
    ans = r
else:
    ans = s
print(ans)