s = input()[::-1]
t = input()[::-1]
ok = False
for i in range(0,len(s)-len(t)+1):
    if s[i] == t[0] or s[i] == '?':
        for j in range(len(t)):
            if s[i+j] != t[j] and s[i+j] != '?':
                break
        else:
            ok = True
            s = s[:i] + t + s[i+len(t):]
            break
if ok:
    ans = ''
    for i in s[::-1]:
        ans += 'a' if i == '?' else i
else:
    ans = 'UNRESTORABLE'
print(ans)