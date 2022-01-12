n = int(input())
a = [int(i) for i in input().split()]
k = 1
ans = 0
for i in range(n):
    if a[i] == k:
        k += 1
    else:
        ans += 1
if ans == n:
    ans = -1
print(ans)