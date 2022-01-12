n,d = map(int,input().split())
x = list(map(int,input().split()))
ans = 0
l = x[0]
r = x[2]
densha = l - r > d
for i in range(1,len(x)-1):
    if x[i] - l <= d:
        if r - x[i] <= d and densha:
            ans += 1