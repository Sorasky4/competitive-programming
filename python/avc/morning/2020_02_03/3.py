n = input()
p = [10,10**2,10**3,10**4,10**5]
ans = 0
for i in range(len(p)):
    if int(n) == p[i]:
        ans = 10
        break
else:
    for i in range(len(n)):
        ans += int(n[i])
print(ans)