n = int(input())
s = []
p = []
ans = [0]*n
for i in range(n):
    s1,p1 = [str(i) for i in input().split()]
    s.append(s1)
    p.append(p1)
    ans[i] = i + 1
for i in range(n):
    p[i] = int(p[i])
flag = 1
while flag:
    flag = 0
    for i in range(n-1,0,-1):
        if s[i] < s[i-1]:
            s[i],s[i-1] = s[i-1],s[i]
            p[i],p[i-1] = p[i-1],p[i]
            ans[i],ans[i-1] = ans[i-1],ans[i]
            flag = 1
flag = 1
while flag:
    flag = 0
    for i in range(n-1):
        if s[i] == s[i+1] and p[i] < p[i+1]:
            p[i],p[i+1] = p[i+1],p[i]
            ans[i],ans[i+1] = ans[i+1],ans[i]
            flag = 1
for i in range(n):
    print(ans[i])