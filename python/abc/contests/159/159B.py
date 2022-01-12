s = input()
n = len(s)
a = ''
ans = 'Yes'
if s[::-1] != s:
    ans = 'No'
for i in range((n-1)//2):
    a += s[i]
if a[::-1] != a:
    ans = 'No'
a = ''
for i in range((n+3)//2-1,n):
    a += s[i]
if a[::-1] != a:
    ans = 'No'
print(ans)