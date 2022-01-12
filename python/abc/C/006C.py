n,m=map(int,input().split())
a=b=c=0
if m%2 != 0:
    m -= 3
    b = 1
    for i in range(m//2+1):
        a = i
        c = n - b - a
        if a*2 + c*4 == m and a + b + c == n:
            print(a,b,c)
            exit(0)
else:
    for i in range(m//2+1):
        a = i
        c = n - a
        if a*2 + c*4 == m and a + c == n:
            print(a,b,c)
            exit(0)
print(-1,-1,-1)