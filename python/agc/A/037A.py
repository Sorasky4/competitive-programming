s = input()
ans = 1
before = s[0]
now = ''
for i in range(1,len(s)):
    now += s[i]
    if before != now:
        before = now
        now = ''
        ans += 1
print(ans)