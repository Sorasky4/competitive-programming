n = int(input())
s = input()
ans = 0
cnt = 0
wcnt = 0
for i in range(n):
    if s[i] == '0':
        cnt += 1
    else:
        ans = max(ans,wcnt+cnt+1)
        wcnt = cnt
        cnt = 0
ans = max(ans,wcnt+cnt+1)
if '1' not in s:
    ans = n
print(ans)