n = int(input())
a = [int(i) for i in input().split()]
ans = 5*10**4
l = 0
num = [[0] for _ in range(9)]
for i in range(n):
    num[a[i]-1][0] += 1
    while [0] not in num:
        ans = min(ans,i-l+1)
        num[a[l]-1][0] -= 1
        l += 1
print(ans)