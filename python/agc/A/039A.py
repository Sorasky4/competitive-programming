'''
s = input()
k = int(input())
ans = 0
cnt = 0
if len(s) == 1:
    ans = k//2
else:
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            cnt += 1
        else:
            ans += ((cnt+1)//2)*k
            cnt = 0
    ans += ((cnt+1)//2)*k
    if s[0] == s[-1]:
        if s[0] != s[1] and s[-1] != s[-2]:
            ans += k - 1
        if len(s) > 2 and (s[0] == s[1] == s[2] or s[-1] == s[-2] == s[-3]):
            ans += 1
print(ans)
'''

s = input()
k = int(input())
ans = 0
cnt = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        cnt += 1
    else:
        ans += (cnt//2)*k
        cnt = 1
ans += ((cnt)//2)*k
if cnt == len(s):
    ans = len(s)*k//2
elif s[0] == s[-1]:
    l = 1
    r = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            l += 1
        else:
            break
    for i in range(len(s)-1,0,-1):
        if s[i] == s[i-1]:
            r += 1
        else:
            break
    ans -= (l//2 + r//2 - ((l+r)//2))*(k-1)
print(ans)