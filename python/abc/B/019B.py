s = input()
ans = []
cnt = 1
for i in range(1,len(s)):
    if s[i-1] != s[i]:
        ans.append(s[i-1])
        ans.append(str(cnt))
        cnt = 1
    else:
        cnt += 1
ans.append(s[-1])
ans.append(cnt)
print(''.join(map(str,ans)))