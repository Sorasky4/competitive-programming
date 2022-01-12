n = int(input())
a = list(map(int, input().split()))

total = [0]*n
total[0] = abs(a[0])
fee = [0]*n
fee[0] = abs(a[0])

for i in range(1,n):
    fee[i] = abs(a[i-1]-a[i])
    total[i] = total[i-1] + fee[i]

dist = total[-1]

print(total[-1] - fee[0] - fee[1] + abs(a[1]) + abs(a[-1]))

for i in range(1,n-1):
    ans = dist - fee[i] - fee[i+1] + abs(a[i-1]-a[i+1])
    ans += abs(a[-1])
    print(ans)

print(total[-2] + abs(a[-2]))