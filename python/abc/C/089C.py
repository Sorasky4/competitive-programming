n = int(input())
s = [input() for _ in range(n)]
M = A = R = C = H = 0
for i in range(len(s)):
    if s[i][0] == 'M':
        M += 1
    if s[i][0] == 'A':
        A += 1
    if s[i][0] == 'R':
        R += 1
    if s[i][0] == 'C':
        C += 1
    if s[i][0] == 'H':
        H += 1
ans = (M*A*R) + (M*A*C) + (M*A*H) + (M*R*C) + (M*R*H) + (M*C*H) + (A*R*C) + (A*R*H) + (A*C*H) + (R*C*H)
print(ans)