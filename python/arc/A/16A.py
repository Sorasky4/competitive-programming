n,m = map(int,input().split())
for i in range(1,n+1):
    if i != m:
        ans = i
        break
print(ans)