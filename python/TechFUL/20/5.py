n = int(input())
t = sorted([int(i) for i in input().split()])
ans = 0
for i in range(1,2*n,2):
    ans += (t[i] - t[i-1])
print(ans)