n = int(input())
b = list(map(int,input().split()))
ans = b[0]
if n == 2:
    ans += b[0]
else:
    for i in range(n-2):
        ans += min(b[i],b[i+1])
    ans += b[-1]
print(ans)