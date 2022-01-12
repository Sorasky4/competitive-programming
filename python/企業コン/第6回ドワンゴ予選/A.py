n = int(input())
s = []
t = []
for i in range(n):
    ss,tt = map(str,input().split())
    s.append(ss)
    t.append(int(tt))
x = input()
flag = False
ans = 0
for i in range(n):
    if flag:
        ans += t[i]
    if x == s[i]:
        flag = True
print(ans)