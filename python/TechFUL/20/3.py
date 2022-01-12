s = sorted([i for i in input()]) + ['0','1']
ans = 0
i = 0
while(i < len(s)-1):
    if s[i] == s[i+1]:
        i += 1
        ans += 1
    i += 1
print(ans)