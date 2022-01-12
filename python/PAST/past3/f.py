n = int(input())
a = []
ans = ''
for _ in range(n):
    a.append(list(input()))
if n == 1:
    print(a[0][0])
    exit()
for i in range(n//2):
    flag = False
    for j in range(n):
        for k in range(n):
            if a[i][j] == a[n-i-1][k]:
                ans += a[i][j]
                flag = True
                break
        if flag:
            break
if len(ans) < n//2:
    print(-1)
    exit()
rev = ans[::-1]
if n % 2 == 1:
    ans += a[n//2][0]
print(ans+rev)