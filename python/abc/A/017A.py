s = []
e = []
ans = 0
for i in range(3):
    s1,e1=[int(i) for i in input().split()]
    s.append(s1)
    e.append(e1)
for i in range(3):
    ans += s[i]*e[i]/10
print(int(ans))