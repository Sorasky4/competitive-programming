a,b,c,x,y = map(int,input().split())
ans = 0
if 2*c < a + b:
    ans += 2*c*min(x,y)
    if x > y:
        ans += (x-y)*a if a <= 2*c else (x-y)*(2*c)
    else:
        ans += (y-x)*b if b <= 2*c else (y-x)*(2*c)
else:
    ans += a*x + b*y
print(ans)