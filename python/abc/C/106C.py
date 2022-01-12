s = input()
k = int(input())
# 5千兆＝ 5 * 10**15
ans = '1'
for i in range(len(s)):
    if s[i] != '1' and i < k:
        ans = s[i]
        break
print(ans)