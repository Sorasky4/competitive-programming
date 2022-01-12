n = int(input())
s = list(input())
e = 0
for i in s:
    if i == 'E':
        e += 1
left = 0
right = e
ans = left + right
for i in range(n):
    if s[i] == 'E':
        right -= 1
    ans = min(ans,left+right)
    if s[i] == 'W':
        left += 1
print(ans)