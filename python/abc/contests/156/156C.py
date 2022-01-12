n = int(input())
x = [int(i) for i in input().split()]
ave = sum(x) // n
ans1 = 0
ans2 = 0
for i in range(n):
    ans1 += (x[i] - ave) ** 2
    ans2 += (x[i] - (ave + 1)) ** 2
print(min(ans1, ans2))