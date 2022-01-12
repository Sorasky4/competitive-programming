n,a,b = map(int,input().split())
ans = 0
for i in range(1,n+1):
    c = 0
    for j in range(len(str(i))):
        c += int(str(i)[j])
    if a <= c <= b:
        ans += i
print(ans)