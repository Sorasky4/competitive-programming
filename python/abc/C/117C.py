n,m = map(int,input().split())
x = sorted([int(i) for i in input().split()])
a = []
if n >= m:
    print(0)
else:
    for i in range(m-1):
        a.append(x[i+1]-x[i])
    ans = sum(sorted(a)[:m-n])
    print(ans)