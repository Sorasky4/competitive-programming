n = int(input())
h = list(map(int,input().split()))
cnt = 0
ans = 0
for i in range(n-1):
    if h[i] >= h[i+1]:
        cnt += 1
    else:
        cnt = 0
    if ans < cnt:
        ans = cnt    
print(ans)