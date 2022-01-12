a,b = map(int,input().split())
ans = -(-(max(a,b) - min(a,b))//2) + min(a,b)
print(ans)