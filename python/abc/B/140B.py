n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
for i in range(n):
    a[i] -= 1
ans = 0
for i in range(n-1):
    ans += b[a[i]]
    if a[i] + 1 == a[i+1]:
        ans += c[a[i]]
ans += b[a[-1]]
print(ans)