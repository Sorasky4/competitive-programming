a,b,c = map(int,input().split())
d = min(a,b) + c
if max(a,b) < d:
    ans = abs(max(a,b) - d) // 2 + max(a,b)
else:
    ans = d
print(ans)