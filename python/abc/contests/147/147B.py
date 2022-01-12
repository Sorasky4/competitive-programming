s = input()
mid = len(s)//2
ans = 0
s_ = []
for i in range(len(s)-1,mid-1,-1):
    s_ += s[i]
s_ = ''.join(map(str,s_))
for i in range(mid):
    if s_[i] != s[i]:
        ans += 1
print(ans)