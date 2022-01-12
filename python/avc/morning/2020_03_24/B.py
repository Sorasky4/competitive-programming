n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]
ans = 0
for i in range(n):
    tmp = 0
    for j in range(i,n):
        if s[i] == s[j]:
            tmp += 1
    for j in range(m):
        if s[i] == t[j]:
            tmp -= 1
    ans = max(ans, tmp)
print(ans)