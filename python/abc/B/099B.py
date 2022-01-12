a,b = map(int,input().split())
x = b - a
ans = 0
for i in range(x+1):
    ans += i
print(ans - b)