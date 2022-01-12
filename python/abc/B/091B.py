n = int(input())
s = sorted([input() for _ in range(n)])
m = int(input())
t = sorted([input() for _ in range(m)])
ans = -100
for i in range(n):
    cnt = 0
    for j in range(n):
        if s[i] == s[j]:
            cnt += 1
    for j in range(m):
        if s[i] == t[j]:
            cnt -= 1
    ans = max(ans,cnt)
ans = max(ans,0)
print(ans)